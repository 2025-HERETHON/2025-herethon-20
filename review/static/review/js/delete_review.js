document.addEventListener("DOMContentLoaded", () => {
  const overlay = document.getElementById("overlay");
  const alertForm = document.getElementById("alert");
  const cancelBtn = document.getElementById("cancel-delete");

  document.querySelectorAll(".trash-icon").forEach((icon) => {
    icon.addEventListener("click", () => {
      const reviewId = icon.dataset.reviewId;
      alertForm.action = `/reviews/delete/${reviewId}/`; // 폼 action 설정
      overlay.classList.remove("hidden");
      alertForm.classList.remove("hidden");
    });
  });

  cancelBtn.addEventListener("click", () => {
    overlay.classList.add("hidden");
    alertForm.classList.add("hidden");
  });
});
