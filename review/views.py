from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from hospital.models import Hospital  # 병원 이름 출력용
from django.http import JsonResponse
from .models import Review, ReviewLike
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

print("✅ review/views.py loaded!")

@login_required
def create_review(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hospital = hospital
            review.user = request.user
            review.save()
            return HttpResponseRedirect(f'/reviews/search/?hospital_id={hospital.id}')
    else:
        form = ReviewForm()

    return render(request, 'review/create_review.html', {
        'form': form,
        'hospital': hospital
    })


def search_reviews(request):
    keyword = request.GET.get('keyword', '')
    hospital_id = request.GET.get('hospital_id')
    sort = request.GET.get('sort', 'created')  # 기본값: 최신순

    reviews = Review.objects.all()

    hospital = None
    if hospital_id:
        reviews = reviews.filter(hospital_id=hospital_id)
        hospital = get_object_or_404(Hospital, id=hospital_id)

    if keyword:
        reviews = reviews.filter(content__icontains=keyword)

    # 정렬
    if sort == 'rating':
        reviews = reviews.order_by('-rating')
    elif sort == 'cost':
        reviews = reviews.order_by('-cost_reasonable')
    elif sort == 'teen':
        reviews = reviews.order_by('-teen_friendly')
    else:
        reviews = reviews.order_by('-created_at')  # 최신순

    return render(request, 'review/search_reviews.html', {
        'reviews': reviews,
        'hospital': hospital,
        'keyword': keyword,
        'sort': sort,
        'star_range': range(1, 6),  # 1부터 5까지 숫자
    })


@require_POST
@login_required
def toggle_review_like(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    user = request.user

    like, created = ReviewLike.objects.get_or_create(user=user, review=review)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': review.likes.count()
    })

#내 리뷰 보기
@login_required
def my_reviews(request):
    reviews = Review.objects.filter(user=request.user).select_related('hospital').order_by('-created_at')
    return render(request, 'review/my_reviews.html', {
        'reviews': reviews
    })


#리뷰 수정
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review:my_reviews')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review/edit_review.html', {'form': form})

#리뷰 삭제
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review.delete()
        return redirect('review:my_reviews')

    return render(request, 'review/delete_review_confirm.html', {'review': review})

def hospital_reviews(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    reviews = Review.objects.filter(hospital=hospital).order_by('-created_at')

    return render(request, 'review/hospital_reviews.html', {
        'hospital': hospital,
        'reviews': reviews,
        'star_range': range(1, 6),
    })

