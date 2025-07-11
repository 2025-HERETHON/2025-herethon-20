document.addEventListener("DOMContentLoaded", function () {
  // .review-list 내 모든 리뷰 카드에 대해 좋아요 기능만 활성화
  const reviewCards = document.querySelectorAll(".review-card");

  reviewCards.forEach((card) => {
    const likeIcon = card.querySelector(".like-icon");
    const likeCount = card.querySelector(".like-count");
    let liked = false;

    if (likeIcon && likeCount) {
      likeIcon.addEventListener("click", () => {
        liked = !liked;
        if (liked) {
          likeIcon.src = "/static/hospital/images/like_fill.svg";
          likeCount.textContent = parseInt(likeCount.textContent) + 1;
        } else {
          likeIcon.src = "/static/hospital/images/like_blank.svg";
          likeCount.textContent = parseInt(likeCount.textContent) - 1;
        }
      });
    }
  });
});
