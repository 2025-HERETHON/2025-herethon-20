document.addEventListener("DOMContentLoaded", function () {
  const reviewList = document.querySelector(".review-list");

  // 알림창 요소
  const alertBox = document.getElementById("alert");
  const confirmBtn = document.getElementById("confirm-delete");
  const cancelBtn = document.getElementById("cancel-delete");
  let targetCardToDelete = null;

  // 모든 삭제 아이콘에 이벤트 연결
  const deleteIcons = document.querySelectorAll(".trash-icon");
  deleteIcons.forEach((icon) => {
    icon.addEventListener("click", () => {
      alertBox.classList.remove("hidden");
      targetCardToDelete = icon.closest(".review-card");
    });
  });

  // 삭제 확인 시 해당 카드 제거
  confirmBtn.addEventListener("click", () => {
    if (targetCardToDelete) {
      reviewList.removeChild(targetCardToDelete);
      targetCardToDelete = null;
    }
    alertBox.classList.add("hidden");
  });

  // 삭제 취소
  cancelBtn.addEventListener("click", () => {
    targetCardToDelete = null;
    alertBox.classList.add("hidden");
  });
});
