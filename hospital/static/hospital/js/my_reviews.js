import { dummymyReviews } from "./dummy_myreviews.js";

document.addEventListener("DOMContentLoaded", function () {
  const reviewList = document.querySelector(".review-list");

  // 알림창 요소 가져오기
  const alertBox = document.getElementById("alert");
  const confirmBtn = document.getElementById("confirm-delete");
  const cancelBtn = document.getElementById("cancel-delete");
  let targetCardToDelete = null;

  reviewList.innerHTML = "";

  // 내 리뷰 불러오기 (임시: 전체 dummyReview 다 보여줌)
  const myReviews = dummymyReviews; // 실제 로그인 사용자 기반 필터링 가능

  myReviews.forEach((review) => {
    const card = document.createElement("div");
    card.className = "review-card";

    const starIcons = Array.from({ length: 5 }, (_, i) => {
      const filled = i < review.rating;
      return `<img src="/static/hospital/images/${
        filled ? "star_fill_small" : "star_blank_small"
      }.svg" alt="별점" class="star-icon" />`;
    }).join("");

    card.innerHTML = `
      <div id="review-info">
        <div id="rating">
          <div class="rating-left">
            <strong class="bold-info">별점</strong>
            <div class="normal-info">${starIcons}</div>
          </div>
          <div id="trash-info">
            <img src="/static/hospital/images/trash_icon.svg" alt="삭제 이미지" class="trash-icon" />
          </div>
        </div>
        <div id="doctor">
          <strong class="bold-info">담당의</strong>
          <p class="normal-info">${review.doctor}</p>
        </div>
        <div id="disease">
          <strong class="bold-info">진료질환</strong>
          <p class="normal-info">${review.disease}</p>
        </div>
        <div id="contents">
          <p class="normal-info">${review.content}</p>
        </div>
        <div id="keyword">
          ${review.keywords
            .map((kw) => `<span class="keyword-tag">${kw}</span>`)
            .join(" ")}
        </div>
      </div>
    `;

    // 삭제 기능 연결

    const deleteIcon = card.querySelector(".trash-icon");
    deleteIcon.addEventListener("click", () => {
      alertBox.classList.remove("hidden");
      targetCardToDelete = card;
    });

    reviewList.appendChild(card);
  });

  confirmBtn.addEventListener("click", () => {
    if (targetCardToDelete) {
      reviewList.removeChild(targetCardToDelete);
      targetCardToDelete = null;
    }
    alertBox.classList.add("hidden");
  });

  cancelBtn.addEventListener("click", () => {
    targetCardToDelete = null;
    alertBox.classList.add("hidden");
  });
});
