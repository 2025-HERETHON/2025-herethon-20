document.addEventListener("DOMContentLoaded", function () {
  // 1. 좋아요 기능
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

  // 2. 커스텀 정렬 드롭다운 기능
  const toggle = document.getElementById("sort-toggle");
  const options = document.getElementById("sort-options");
  const input = document.getElementById("sort-input");
  const form = document.getElementById("sort-form");

  if (toggle && options && input && form) {
    toggle.addEventListener("click", () => {
      options.hidden = !options.hidden;
    });

    options.addEventListener("click", (e) => {
      if (e.target.tagName === "LI") {
        const value = e.target.dataset.value;
        input.value = value;
        toggle.childNodes[0].textContent = e.target.textContent;
        options.hidden = true;
        form.submit(); // 자동 제출
      }
    });

    // 외부 클릭 시 드롭다운 닫기
    document.addEventListener("click", (e) => {
      if (!document.getElementById("sort-select").contains(e.target)) {
        options.hidden = true;
      }
    });
  }
});
