import { dummyReviews } from "./dummy_reviews.js";

document.addEventListener("DOMContentLoaded", function () {
  const reviewList = document.querySelector(".review-list");
  const queryParams = new URLSearchParams(window.location.search);
  const keyword = queryParams.get("q")?.trim() || "";

  reviewList.innerHTML = "";

  // 검색어 필터링: 키워드, 담당의, 질환, 리뷰 내용 전체 포함 여부 확인
  const filtered = dummyReviews.filter((review) => {
    const keywordLower = keyword.toLowerCase();
    return (
      review.doctor.toLowerCase().includes(keywordLower) ||
      review.disease.toLowerCase().includes(keywordLower) ||
      review.content.toLowerCase().includes(keywordLower) ||
      review.keywords.some((kw) => kw.toLowerCase().includes(keywordLower))
    );
  });

  // 검색 결과 개수 표시
  const resultCount = document.createElement("div");
  resultCount.className = "result-count";
  resultCount.innerHTML = `<p>검색 결과 <span id="bold-count">${filtered.length}</span>개</p>`;
  reviewList.before(resultCount);

  // 카드 생성
  filtered.forEach((review) => {
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
          <div id="like-info">
            <img src="/static/hospital/images/like_blank.svg" alt="좋아요" class="like-icon" />
            <span class="like-count">0</span>
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

    // 좋아요 기능
    const likeIcon = card.querySelector(".like-icon");
    const likeCount = card.querySelector(".like-count");
    let liked = false;

    likeIcon.addEventListener("click", () => {
      liked = !liked;
      likeIcon.src = liked
        ? "/static/hospital/images/like_fill.svg"
        : "/static/hospital/images/like_blank.svg";
      likeCount.textContent = liked ? "1" : "0";
    });

    reviewList.appendChild(card);
  });
});
