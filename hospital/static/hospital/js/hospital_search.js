document.addEventListener("DOMContentLoaded", function () {
  const resultItems = document.querySelectorAll(".result-item");

  // 검색어 유지 코드
  const params = new URLSearchParams(window.location.search);
  const query = params.get("q");

  const searchInput = document.querySelector('input[name="q"]');
  if (searchInput && query) {
    searchInput.value = query;
  }

  resultItems.forEach((item) => {
    item.addEventListener("click", function () {
      const hospitalId = this.dataset.id;
      if (hospitalId) {
        window.location.href = `/hospitals/hospital_detail/${hospitalId}/`;
      }
    });
  });
});
