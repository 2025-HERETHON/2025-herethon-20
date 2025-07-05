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
