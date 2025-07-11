document.addEventListener("DOMContentLoaded", function () {
  const sidoNames = {
    110000: "서울특별시",
    410000: "경기도",
  };

  const sgguNames = {
    110001: "강남구",
    110002: "강동구",
    110003: "강북구",
    110004: "강서구",
    110005: "관악구",
    110006: "광진구",
    110007: "구로구",
    110008: "금천구",
    110009: "노원구",
    110010: "도봉구",
    110011: "동대문구",
    110012: "동작구",
    110013: "마포구",
    110014: "서대문구",
    110015: "서초구",
    110016: "성동구",
    110017: "성북구",
    110018: "송파구",
    110019: "양천구",
    110020: "영등포구",
    110021: "용산구",
    110022: "은평구",
    110023: "종로구",
    110024: "중구",
    110025: "중랑구",
    410001: "수원시",
    410002: "성남시",
  };

  const sgguData = {
    110000: [
      110001, 110002, 110003, 110004, 110005, 110006, 110007, 110008, 110009,
      110010, 110011, 110012, 110013, 110014, 110015, 110016, 110017, 110018,
      110019, 110020, 110021, 110022, 110023, 110024, 110025,
    ],
    410000: [410001, 410002],
  };

  const sidoToggle = document.getElementById("sido-toggle");
  const sidoOptions = document.getElementById("sido-options");
  const sgguToggle = document.getElementById("sggu-toggle");
  const sgguOptions = document.getElementById("sggu-options");
  const filterButtons = document.querySelectorAll(".filter-btn");

  let currentSido = null;
  let currentSggu = null;
  let currentSort = null;


  // URL에서 선택된 값 가져오기
  const urlParams = new URLSearchParams(window.location.search);
  currentSido = urlParams.get("sidoCd");
  currentSggu = urlParams.get("sgguCd");
  currentSort = urlParams.get("sort");

  // 선택된 시도 텍스트 표시
  if (currentSido && sidoNames[currentSido]) {
    sidoToggle.textContent = sidoNames[currentSido];
    sgguToggle.disabled = false;

    // 시군구 옵션도 렌더링
    sgguOptions.innerHTML = "";
    sgguData[currentSido]?.forEach((sgguCd) => {
      const li = document.createElement("li");
      li.textContent = sgguNames[sgguCd];
      li.dataset.value = sgguCd;
      sgguOptions.appendChild(li);
    });
  }

  // 선택된 시군구 텍스트 표시
  if (currentSggu && sgguNames[currentSggu]) {
    sgguToggle.textContent = sgguNames[currentSggu];
  }

  // 선택된 정렬 버튼 표시
  if (currentSort) {
    filterButtons.forEach((btn) => {
      const text = btn.textContent;
      if (
        (currentSort === "female" && text.includes("여성")) ||
        (currentSort === "rating" && text.includes("별점")) ||
        (currentSort === "teen" && text.includes("10대"))
      ) {
        btn.classList.add("active");
      }
    });
  }

  // 시도 렌더링
  for (const sidoCd in sgguData) {
    const li = document.createElement("li");
    li.textContent = sidoNames[sidoCd];
    li.dataset.value = sidoCd;
    sidoOptions.appendChild(li);
  }

  // 드롭다운 토글
  sidoToggle.addEventListener("click", () => {
    sidoOptions.style.display =
      sidoOptions.style.display === "block" ? "none" : "block";
    sgguOptions.style.display = "none";
  });

  sgguToggle.addEventListener("click", () => {
    sgguOptions.style.display =
      sgguOptions.style.display === "block" ? "none" : "block";
    sidoOptions.style.display = "none";
  });

  // 시도 선택 시 시군구 옵션 표시
  sidoOptions.addEventListener("click", (e) => {
    if (e.target.tagName !== "LI") return;

    const sidoCd = e.target.dataset.value;
    currentSido = sidoCd;
    currentSggu = null;
    sidoToggle.textContent = sidoNames[sidoCd];
    sidoOptions.style.display = "none";

    sgguToggle.disabled = false;
    sgguToggle.textContent = "시/군/구";
    sgguOptions.innerHTML = "";

    sgguData[sidoCd].forEach((sgguCd) => {
      const li = document.createElement("li");
      li.textContent = sgguNames[sgguCd];
      li.dataset.value = sgguCd;
      sgguOptions.appendChild(li);
    });
  });

  // 시군구 선택 시 URL 이동
  sgguOptions.addEventListener("click", (e) => {
    if (e.target.tagName !== "LI") return;

    const sgguCd = e.target.dataset.value;
    currentSggu = sgguCd;
    sgguToggle.textContent = sgguNames[sgguCd];
    sgguOptions.style.display = "none";

    const queryParams = new URLSearchParams();
    if (currentSido) queryParams.append("sidoCd", currentSido);
    if (currentSggu) queryParams.append("sgguCd", currentSggu);
    if (currentSort) queryParams.append("sort", currentSort);

    window.location.href = `/hospitals/list/?${queryParams.toString()}`;

  });

  // 병원 카드 클릭 시 상세 페이지 이동
  document.querySelectorAll(".hospital-card").forEach((card) => {
    const hospitalId = card.dataset.id;
    if (hospitalId) {
      card.addEventListener("click", () => {
        window.location.href = `/hospitals/hospital_detail/${hospitalId}/`;
      });
    }

  });

  // 정렬 버튼 클릭 시 URL 이동
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      filterButtons.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");

      const text = this.textContent;
      let sortParam = null;
      if (text.includes("여성")) sortParam = "female";
      else if (text.includes("별점")) sortParam = "rating";
      else if (text.includes("10대")) sortParam = "teen";

      currentSort = sortParam;

      const queryParams = new URLSearchParams();
      if (currentSido) queryParams.append("sidoCd", currentSido);
      if (currentSggu) queryParams.append("sgguCd", currentSggu);
      if (currentSort) queryParams.append("sort", currentSort);

      window.location.href = `/hospitals/list/?${queryParams.toString()}`;
    });
  });
});
