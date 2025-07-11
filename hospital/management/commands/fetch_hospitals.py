import ssl
import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from hospital.models import Hospital
from django.conf import settings
from requests.adapters import HTTPAdapter

# ✅ SSL 보안 설정 낮추는 Adapter
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
        kwargs['ssl_context'] = ctx
        return super().init_poolmanager(*args, **kwargs)

# ✅ 여성 전문의 여부 판단 함수 (진료과 mdeptGdrCnt 기반)
def has_female_doctor(item):
    try:
        # 'mdeptGdrCnt'는 진료과 소속 여성 전문의 수
        value = item.findtext('mdeptGdrCnt')
        if value and int(value) > 0:
            return True
    except:
        pass
    return False

class Command(BaseCommand):
    help = "공공 API에서 산부인과 병원 리스트를 가져와 DB에 저장하고 XML 응답 출력"

    def add_arguments(self, parser):
        parser.add_argument('--sidoCd', type=str, required=True, help='시도 코드 (예: 110000)')
        parser.add_argument('--sgguCd', type=str, required=True, help='시군구 코드 (예: 110001)')

    def handle(self, *args, **kwargs):
        sidoCd = kwargs['sidoCd']
        sgguCd = kwargs['sgguCd']
        self.stdout.write(f"📡 {sidoCd}-{sgguCd} 지역 산부인과 병원 리스트를 불러오는 중...")

        url = "https://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList"
        params = {
            'ServiceKey': settings.PUBLIC_API_KEY,
            'pageNo': 1,
            'numOfRows': 100,
            'sidoCd': sidoCd,
            'sgguCd': sgguCd,
            'dgsbjtCd': '10',  # 산부인과 진료과목 코드
        }

        try:
            session = requests.Session()
            session.mount("https://", TLSAdapter())
            response = session.get(url, params=params, timeout=30)
            response.raise_for_status()
            # ✅ XML 원문 출력
            self.stdout.write("📦 API 응답 원문 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            self.stdout.write(response.content.decode('utf-8'))
            self.stdout.write("📦 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")

        except requests.exceptions.RequestException as e:
            self.stderr.write(f"❌ 요청 오류: {e}")
            return

        try:
            root = ET.fromstring(response.content)
            items = root.find('.//items')

            if items is None:
                self.stdout.write("✅ 응답은 성공했지만 병원 데이터가 없습니다.")
                return

            raw_items = items.findall('item')
            if not raw_items:
                item = items.find('item')
                raw_items = [item] if item is not None else []

            count = 0
            for item in raw_items:
                ykiho = item.findtext('ykiho')
                name = item.findtext('yadmNm') or ''
                yadmCd = item.findtext('yadmCd')

                if not ykiho or not name:
                    continue

                # 키워드 필터링 (정상 동작하는 조건 유지)
                if not any(word in name for word in ['산부인과', '여성병원', '여성의원', '여성', '부인과']):
                    continue

                # mdeptGdrCnt 기준 여성 전문의 확인
                is_female = has_female_doctor(item)
                print(f"🏥 {name} | 여성 전문의: {is_female}")

                Hospital.objects.update_or_create(
                    yadmCd=ykiho,
                    defaults={
                        'name': name,
                        'address': item.findtext('addr'),
                        'sidoCd': sidoCd,
                        'sgguCd': sgguCd,
                        'tel': item.findtext('telno'),
                        'is_female_doctor': is_female,
                    }
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"✅ {count}개 산부인과 병원 저장 완료"))

        except Exception as e:
            self.stderr.write(f"❌ XML 파싱 오류: {e}")
