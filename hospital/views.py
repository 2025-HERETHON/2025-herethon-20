# hospital/views.py
from django.shortcuts import render, get_object_or_404
from .models import Hospital
import requests
from django.conf import settings
from rest_framework.generics import ListAPIView
from .models import Hospital
from django.db.models import Avg, Count, Q
from django.http import JsonResponse
from django.shortcuts import render
from review.models import Review

def hospital_list(request):
    hospitals = Hospital.objects.all().annotate(
        average_rating=Avg('reviews__rating'),
        cost_reasonable_count=Count('reviews', filter=Q(reviews__cost_reasonable=True)),
        teen_friendly_count=Count('reviews', filter=Q(reviews__teen_friendly=True)),
    )

    return render(request, 'hospital/hospital_list.html', {
        'hospitals': hospitals,
    })


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
def hospital_list(request):
    sido = request.GET.get('sidoCd')
    sggu = request.GET.get('sgguCd')
    sort = request.GET.get('sort')

    hospitals = Hospital.objects.all()

    if sido:
        hospitals = hospitals.filter(sidoCd=sido)
    if sggu:
        hospitals = hospitals.filter(sgguCd=sggu)

    hospitals = hospitals.annotate(
        average_rating=Avg('reviews__rating'),
        cost_reasonable_count=Count('reviews', filter=Q(reviews__cost_reasonable=True)),
        teen_friendly_count=Count('reviews', filter=Q(reviews__teen_friendly=True)),
    )

    if sort == 'rating':
        hospitals = hospitals.order_by('-average_rating')
    elif sort == 'cost':
        hospitals = hospitals.order_by('-cost_reasonable_count')
    elif sort == 'teen':
        hospitals = hospitals.order_by('-teen_friendly_count')
    elif sort == 'female':
        hospitals = hospitals.order_by('-is_female_doctor')

    return render(request, 'hospital/hospital_list.html', {
        'hospitals': hospitals,
    })

# 병원 검색 (임시)
def hospital_search(request):
    #html에서 보낸 input의 name 속성
    query = request.GET.get('q')
    hospitals = []

    if query:
        hospitals = Hospital.objects.filter(name__icontains=query)

    return render(request, 'hospital/hospital_search.html', {
        'query': query,
        'hospitals': hospitals
    })


# 병원 상세 정보 (임시)
def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, 'hospital/hospital_detail.html', {'hospital': hospital})

# 병원 리뷰 확인 페이지 (임시)
def hospital_reviews(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, 'hospital/hospital_reviews.html', {'hospital': hospital})

# 병원 내 리뷰 검색 페이지 (임시)
def review_search(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    query = request.GET.get('q')
    # 필터된 리뷰 결과를 여기에 구현할 수도 있음 (지금은 생략 가능)
    return render(request, 'hospital/review_search.html', {
        'hospital': hospital,
        'query': query})

# 간편 상담 예약 페이지 (임시)
def hospital_reserve(request):
    return render(request, 'hospital/hospital_reserve.html')

# 의사 검색 페이지 (임시)
def hospital_reserve_search(request):
    return render(request, 'hospital/hospital_reserve_search.html')

# 내 리뷰(임시)
def my_reviews(request):
    return render(request, 'hospital/my_reviews.html')

# 마이페이지(임시)
def my_page(request):
    return render(request, 'hospital/my_page.html')
