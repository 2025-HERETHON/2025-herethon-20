document.addEventListener("DOMContentLoaded", function () {
  const copyBtn = document.getElementById("copy-phone"); // 복사 버튼
  const phoneText = document.getElementById("phone-text"); // 복사할 대상 텍스트

  copyBtn.addEventListener("click", function (e) {
    e.preventDefault(); // 링크 기본 동작 방지

    // 복사할 텍스트 가져오기
    const textToCopy = phoneText.textContent;

    // 클립보드 API 사용
    navigator.clipboard
      .writeText(textToCopy)
      .then(() => {
        alert("전화번호가 복사되었습니다!");
      })
      .catch((err) => {
        alert("복사에 실패했습니다: " + err);
      });
  });
});
