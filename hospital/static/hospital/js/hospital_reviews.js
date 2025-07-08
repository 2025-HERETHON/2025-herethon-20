document.addEventListener("DOMContentLoaded", function () {
  const reviewList = document.querySelector(".review-list");

  const dummyReviews = [
    {
      rating: 5,
      doctor: "정예진 산부인과 전문의",
      disease: "생리불순, 질염 증상",
      content: `친구 추천으로 처음 방문한 병원인데 생각보다 훨씬 편안했어요. 정예진 선생님의 진료 하나하나 친절하게 들어주시고, 필요한 정보도 쉽게 설명해주셔서 정말 안심됐어요.`,
      keywords: [
        "😍 친절해요",
        "😄 10대 친화적이에요 (가격, 환경 등)",
        "🤗 과잉진료하지 않아요",
      ],
    },
    {
      rating: 3,
      doctor: "정예진 산부인과 전문의",
      disease: "불규칙한 생리",
      content: `병원 시설도 깨끗하고, 진료받는 동안 민망하지 않게 배려해주셔서 좋았어요. 여성 환자들에게 추천할만한 곳이에요.`,
      keywords: ["😍 친절해요"],
    },
    {
      rating: 2,
      doctor: "정예진 산부인과 전문의",
      disease: "임신",
      content: `나쁘지 않아요`,
      keywords: [],
    },
    {
      rating: 5,
      doctor: "정예진 산부인과 전문의",
      disease: "생리통",
      content: `의사 선생님이 친절하고 꼼꼼하게 진료를 봐주셨어요.`,
      keywords: ["🤗 과잉진료하지 않아요"],
    },
  ];

  dummyReviews.forEach((review) => {
    const card = document.createElement("div");
    card.className = "review-card";

    // 별점 이미지 5개 생성
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

    // 좋아요 기능 추가
    const likeIcon = card.querySelector(".like-icon");
    const likeCount = card.querySelector(".like-count");
    let liked = false;

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

    reviewList.appendChild(card);
  });
});
