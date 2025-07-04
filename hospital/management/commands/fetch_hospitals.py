import ssl
import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from hospital.models import Hospital
from django.conf import settings
from requests.adapters import HTTPAdapter


# SSL 보안 설정용 Adapter
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
        kwargs['ssl_context'] = ctx
        return super().init_poolmanager(*args, **kwargs)


# (일단 사용 안함) 여성 전문의 확인 함수
# def check_female_doctor(yadmCd):
#     try:
#         url = "https://apis.data.go.kr/B551182/spclMdclMdclListInfoService/getSpclMdcList"
#         params = {
#             'ServiceKey': settings.PUBLIC_API_KEY,
#             'yadmCd': yadmCd,
#         }
#         response = requests.get(url, params=params, timeout=10)
#         response.raise_for_status()
#         root = ET.fromstring(response.content)
#         items = root.find('.//items')
#         if items is not None:
#             for doc in items.findall('item'):
#                 if doc.findtext('sdrSexCd') == '2':
#                     return True
#     except Exception as e:
#         print(f"[⚠] 여성 전문의 확인 오류 (병원코드: {yadmCd}): {e}")
#     return False


class Command(BaseCommand):
    help = "공공 API에서 병원 리스트를 가져와 DB에 저장합니다."

    def add_arguments(self, parser):
        parser.add_argument('--sidoCd', type=str, required=True, help='시도 코드 (예: 110000: 서울)')
        parser.add_argument('--sgguCd', type=str, required=True, help='시군구 코드 (예: 110001: 강남구)')

    def handle(self, *args, **kwargs):
        sidoCd = kwargs['sidoCd']
        sgguCd = kwargs['sgguCd']
        self.stdout.write(f"📡 {sidoCd}-{sgguCd} 지역 병원 리스트를 불러오는 중...")

        url = "https://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList"
        params = {
            'ServiceKey': settings.PUBLIC_API_KEY,
            'pageNo': 1,
            'numOfRows': 100,
            'sidoCd': sidoCd,
            'sgguCd': sgguCd,
            'detyGdrCd': '10',  # 표시과목코드: 산부인과
        }

        try:
            session = requests.Session()
            session.mount("https://", TLSAdapter())
            response = session.get(url, params=params, timeout=30)
            response.raise_for_status()
            self.stdout.write(f"📦 응답 원문:\n{response.content.decode('utf-8')}")
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
                ykiho = item.findtext('ykiho')  # yadmCd 대신 ykiho 사용
                if not ykiho:
                    continue

                Hospital.objects.update_or_create(
                    yadmCd=ykiho,
                    defaults={
                        'name': item.findtext('yadmNm'),
                        'address': item.findtext('addr'),
                        'sidoCd': sidoCd,
                        'sgguCd': sgguCd,
                        'tel': item.findtext('telno'),
                        'is_female_doctor': False,  # 여성 전문의 확인은 일단 생략
                    }
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"✅ {count}개 병원 저장 완료"))

        except Exception as e:
            self.stderr.write(f"❌ XML 파싱 오류: {e}")
