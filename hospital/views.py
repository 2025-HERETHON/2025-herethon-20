# hospital/views.py
from django.shortcuts import render, get_object_or_404
from .models import Hospital
import requests
from django.conf import settings
from rest_framework.generics import ListAPIView
from .models import Hospital
from .serializers import HospitalSerializer
from django.db.models import Avg, Count, Q
from django.http import JsonResponse

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
class HospitalListAPIView(ListAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        sido = self.request.query_params.get('sidoCd')
        sggu = self.request.query_params.get('sgguCd')
        sort = self.request.query_params.get('sort')

        queryset = Hospital.objects.all()

        if sido:
            queryset = queryset.filter(sidoCd=sido)
        if sggu:
            queryset = queryset.filter(sgguCd=sggu)

        #queryset = queryset.annotate(
        #    average_rating=Avg('reviews__rating'),
        #    cost_reasonable_count=Count('reviews', filter=Q(reviews__cost_reasonable=True)),
        #    teen_friendly_count=Count('reviews', filter=Q(reviews__teen_friendly=True)),
        #)

        if sort == 'rating':
            queryset = queryset.order_by('-average_rating')
        elif sort == 'cost':
            queryset = queryset.order_by('-cost_reasonable_count')
        elif sort == 'teen':
            queryset = queryset.order_by('-teen_friendly_count')
        elif sort == 'female':
            queryset = queryset.order_by('-is_female_doctor')

        return queryset
    
# 병원 검색 (임시)
def hospital_search(request):
    return render(request, 'hospital/hospital_search.html')

# 리뷰 작성 (임시)
def review_create(request):
    return render(request, 'hospital/review_create.html')

# 병원 상세 정보 (임시)
def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, 'hospital/hospital_detail.html', {'hospital': hospital})

# 병원 리뷰 확인 페이지 (임시)
def hospital_reviews(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, 'hospital/hospital_reviews.html', {'hospital': hospital})

# 병원 내 리뷰 검색 페이지 (임시)
def review_search(request):
    return render(request, 'hospital/review_search.html')