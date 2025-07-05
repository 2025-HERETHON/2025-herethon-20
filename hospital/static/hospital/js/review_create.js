// 별점 등록
document.addEventListener("DOMContentLoaded", function () {
  const stars = document.querySelectorAll(".star");
  const fillStarSrc = "/static/hospital/images/star_fill.svg";
  const blankStarSrc = "/static/hospital/images/star_blank.svg";
  // 평점 저장하기 위한 변수
  const ratingInput = document.getElementById("rating-value");

  stars.forEach((star, index) => {
    star.addEventListener("click", () => {
      const clickedIndex = index;

      // stars 리스트에 있는 모든 별 요소를 하나씩 반복
      stars.forEach(function (star, index) {
        // 별의 인덱스가 클릭된 별의 인덱스보다 작거나 같으면
        if (index <= clickedIndex) {
          star.src = fillStarSrc;
        } else {
          // 그렇지 않으면 빈 별 이미지로 변경
          star.src = blankStarSrc;
        }
      });

      // 숨겨진 input에 값 저장 (1~5)
      ratingInput.value = clickedIndex + 1;
    });
  });
});

//드롭다운 구현
document.addEventListener("DOMContentLoaded", function () {
  const keywordSelect = document.getElementById("keywordSelect");
  const keywordOptions = document.getElementById("keywordOptions");
  const selectedKeywords = document.getElementById("selectedKeywords");
  const keywordsInput = document.getElementById("keywordsInput");

  // 드롭다운 열고 닫기
  keywordSelect.addEventListener("click", () => {
    keywordOptions.style.display =
      keywordOptions.style.display === "block" ? "none" : "block";
  });

  // 체크박스 변경 시
  keywordOptions
    .querySelectorAll("input[type='checkbox']")
    .forEach((checkbox) => {
      // 각 체크박스에 이벤트 등록
      checkbox.addEventListener("change", () => {
        // 체크된 체크박스들의 value만 추출해서 배열로 만들기
        const selected = Array.from(
          keywordOptions.querySelectorAll("input[type='checkbox']:checked")
        ).map((cb) => cb.value);

        selectedKeywords.textContent = selected.join(", "); // value들 ,로 연결해서 드롭다운 내용으로 넣어주기
        keywordsInput.value = selected.join(","); // 폼 제출시 서버로 전송
      });
    });

  // 바깥 클릭 시 닫기
  document.addEventListener("click", function (e) {
    if (
      !keywordSelect.contains(e.target) &&
      !keywordOptions.contains(e.target)
    ) {
      keywordOptions.style.display = "none";
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("reviewForm");
  const textarea = document.getElementById("details");
  const errorMessage = document.getElementById("error-message");
  const submitButton = document.getElementById("submit-button");

  submitButton.addEventListener("click", function () {
    const text = textarea.value.trim();

    // 1. 글자 수 검증
    if (text.length < 8) {
      errorMessage.style.display = "flex"; // 오류 메시지 보이기

      setTimeout(() => {
        errorMessage.style.display = "none";
      }, 1500);
      return;
    }

    // 2. 버튼 색상 변경 및 텍스트 수정
    submitButton.style.backgroundColor = " #A78BFA";
    submitButton.textContent = "제출완료";

    // 3. 폼 직접 제출
    form.submit();
  });
});
