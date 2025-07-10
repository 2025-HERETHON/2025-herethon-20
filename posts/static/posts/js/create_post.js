document.addEventListener('DOMContentLoaded', function () {
  const titleInput = document.getElementById('title');
  const contentTextarea = document.getElementById('content');
  const submitBtn = document.getElementById('submit-btn');

  function checkInputs() {
    const titleFilled = titleInput.value.trim().length > 0;
    const contentFilled = contentTextarea.value.trim().length > 0;

    if (titleFilled && contentFilled) {
      submitBtn.disabled = false;
      submitBtn.style.color = '#A78BFA'; // 활성화 색상
    } else {
      submitBtn.disabled = true;
      submitBtn.style.color = '#ddd6f3'; // 비활성화 색상
    }
  }

  titleInput.addEventListener('input', checkInputs);
  contentTextarea.addEventListener('input', checkInputs);

  checkInputs();
});