# hospital/views.py
from django.shortcuts import render
from .models import Hospital
import requests
from django.conf import settings

def hospital_list(request):
    region = request.GET.get('region')
    hospitals = Hospital.objects.all()
    if region:
        hospitals = hospitals.filter(sidoCd=region)

    return render(request, 'hospital/hospital_list.html', {'hospitals': hospitals})


# 병원 공공 API에서 데이터 받아오기
def fetch_hospitals_from_api(region_code):
    SERVICE_KEY = settings.PUBLIC_API_KEY
    url = "https://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1"

    params = {
        'ServiceKey': SERVICE_KEY,
        'pageNo': 1,
        'numOfRows': 100,
        'sidoCd': region_code,
        '_type': 'json'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json().get('response', {}).get('body', {}).get('items', {}).get('item', [])
        for item in items:
            Hospital.objects.update_or_create(
                yadmCd=item.get('yadmCd'),
                defaults={
                    'name': item.get('yadmNm'),
                    'address': item.get('addr'),
                    'sidoCd': item.get('sidoCd'),
                    'sgguCd': item.get('sgguCd'),
                    'tel': item.get('telno'),
                    'is_female_doctor': False  # 기본값 설정 (추후 업데이트 가능)
                }
            )
