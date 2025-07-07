document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".filter-btn");

  filterButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      filterButtons.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");
    });
  });
});

// 문서가 완전히 로드된 후에 실행 (DOMContentLoaded 이벤트 사용)
document.addEventListener("DOMContentLoaded", function () {
  // 시도(select) 요소와 시군구(select) 요소를 각각 변수에 저장
  const sidoSelect = document.getElementById("sido-box");
  const sgguSelect = document.getElementById("sggu-box");

  // 시도별 시군구 리스트 (임시 데이터)
  const sgguData = {
    a: ["ㄱ", "ㄴ"],
    b: ["ㄷ", "ㄹ"],
    c: ["ㅁ", "ㅂ"],
    d: ["ㅅ", "ㅇ"],
  };

  // 시도 선택 시 실행되는 이벤트 핸들러
  sidoSelect.addEventListener("change", function () {
    const selectedSido = this.value; // 사용자가 선택한 시도 코드
    const relatedSgguList = sgguData[selectedSido] || []; // 해당 시도의 시군구 목록 불러오기

    // 시군구 드롭다운 초기화 (기본 안내 옵션만 남기고 지움)
    sgguSelect.innerHTML =
      '<option value="" selected disabled hidden>시/군/구</option>';

    // 시군구 드롭다운 활성화 (처음엔 disabled 상태이므로 enable로 변경)
    sgguSelect.disabled = false;

    // 시군구 목록을 기반으로 option 태그를 생성해 드롭다운에 추가
    relatedSgguList.forEach((name) => {
      const option = document.createElement("option"); // <option> 태그 생성
      option.value = name; // value 설정
      option.textContent = name; // 사용자에게 보이는 텍스트
      sgguSelect.appendChild(option); // <select>에 option 추가
    });
  });
});
