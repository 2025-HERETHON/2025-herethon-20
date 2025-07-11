document.addEventListener("DOMContentLoaded", () => {
  const popup = document.getElementById("popup-message");

  // 모든 복사 버튼에 이벤트 등록
  const copyButtons = document.querySelectorAll(".copy-phone");

  copyButtons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();

      // 전화번호 요소 탐색
      const phone = btn
        .closest(".doctor-tel-row")
        .querySelector(".phone-text").textContent;

      // 복사 동작
      navigator.clipboard.writeText(phone).then(() => {
        // 팝업 메시지 표시
        if (popup) {
          popup.style.display = "block";
          setTimeout(() => {
            popup.style.display = "none";
          }, 1000);
        }
      });
    });
  });
});
