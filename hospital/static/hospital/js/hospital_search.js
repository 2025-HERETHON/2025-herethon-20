document.addEventListener("DOMContentLoaded", function () {
  const resultItems = document.querySelectorAll(".result-item");

  resultItems.forEach((item) => {
    item.addEventListener("click", function () {
      const hospitalId = this.dataset.id;
      if (hospitalId) {
        window.location.href = `/hospitals/hospital_detail/${hospitalId}/`;
      }
    });
  });
});
