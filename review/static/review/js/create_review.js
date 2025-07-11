//create_review.js

document.addEventListener("DOMContentLoaded", function () {
  // 별점 등록
  const stars = document.querySelectorAll(".star");
  const fillStarSrc = "/static/hospital/images/star_fill.svg";
  const blankStarSrc = "/static/hospital/images/star_blank.svg";
  const ratingInput = document.getElementById("rating-value");

  stars.forEach((star, index) => {
    star.addEventListener("click", () => {
      const clickedIndex = index;
      stars.forEach((star, index) => {
        star.src = index <= clickedIndex ? fillStarSrc : blankStarSrc;
      });
      ratingInput.value = clickedIndex + 1;
    });
  });

  // 키워드 드롭다운 구현
  const keywordSelect = document.getElementById("keywordSelect");
  const keywordOptions = document.getElementById("keywordOptions");
  const selectedKeywords = document.getElementById("selectedKeywords");
  const keywordsInput = document.getElementById("keywordsInput");

  keywordSelect.addEventListener("click", () => {
    keywordOptions.style.display =
      keywordOptions.style.display === "block" ? "none" : "block";
  });

  keywordOptions
    .querySelectorAll("input[type='checkbox']")
    .forEach((checkbox) => {
      checkbox.addEventListener("change", () => {
        const selected = Array.from(
          keywordOptions.querySelectorAll("input[type='checkbox']:checked")
        ).map((cb) => cb.value);

        selectedKeywords.textContent = selected.join(", ");
        keywordsInput.value = selected.join(",");
      });
    });

  document.addEventListener("click", function (e) {
    if (
      !keywordSelect.contains(e.target) &&
      !keywordOptions.contains(e.target)
    ) {
      keywordOptions.style.display = "none";
    }
  });

  // 글자수 검사 후 제출 + 3초 후 페이지 이동
  const form = document.getElementById("reviewForm");
  const textarea = document.getElementById("details");
  const errorMessage = document.getElementById("error-message");
  const submitButton = document.getElementById("submit-button");

  submitButton.addEventListener("click", function (e) {
    e.preventDefault(); // 기본 제출 막기
    const text = textarea.value.trim();

    if (text.length < 8) {
      errorMessage.style.display = "flex";
      setTimeout(() => {
        errorMessage.style.display = "none";
      }, 1500);
      return;
    }

    submitButton.style.backgroundColor = " #A78BFA";
    submitButton.textContent = "제출완료";

    // 1. 색상 바꾼 뒤 1초 정도 기다렸다가
    setTimeout(() => {
      // 2. 폼 제출
      form.submit();
    }, 1000);
  });
});
