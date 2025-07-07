// hospital_list.js

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
  const hospitalList = document.getElementById("hospital-list");
  let currentSido = null;
  let currentSggu = null;

  // 시도 옵션 렌더링
  for (const sidoCd in sgguData) {
    const li = document.createElement("li");
    li.textContent = sidoNames[sidoCd];
    li.dataset.value = sidoCd;
    sidoOptions.appendChild(li);
  }

  // 드롭다운 열기/닫기
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

  // 시도 선택 시
  sidoOptions.addEventListener("click", (e) => {
    if (e.target.tagName !== "LI") return;

    const sidoCd = e.target.dataset.value;
    currentSido = sidoCd;
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

  // 시군구 선택 시
  sgguOptions.addEventListener("click", (e) => {
    if (e.target.tagName !== "LI") return;

    const sgguCd = e.target.dataset.value;
    currentSggu = sgguCd;
    sgguToggle.textContent = sgguNames[sgguCd];
    sgguOptions.style.display = "none";

    fetchHospitals(currentSido, currentSggu);
  });

  // 필터 버튼 처리
  const filterButtons = document.querySelectorAll(".filter-btn");
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      filterButtons.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");

      const text = this.textContent;
      let sortParam = null;
      if (text.includes("여성")) sortParam = "female";
      else if (text.includes("별점")) sortParam = "rating";
      else if (text.includes("10대")) sortParam = "teen";

      if (currentSido && currentSggu) {
        fetchHospitals(currentSido, currentSggu, sortParam);
      }
    });
  });

  // 병원 목록 불러오기
  function fetchHospitals(sidoCd, sgguCd, sort) {
    let url = `/hospitals/api/hospitals/?sidoCd=${sidoCd}&sgguCd=${sgguCd}`;
    if (sort) url += `&sort=${sort}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        hospitalList.innerHTML = "";
        if (data.length === 0) {
          hospitalList.innerHTML = "<p>병원이 없습니다.</p>";
          return;
        }

        data.forEach((hospital, idx) => {
          const card = document.createElement("div");
          card.className = "hospital-card";
          if (idx === data.length - 1) card.style.marginBottom = "1.5rem";

          card.innerHTML = `
            <div class="hospital-sample-image">
              <img src="/static/hospital/images/hospital_image_card.svg" alt="병원 샘플 이미지" id="hospital-image"/>
              <div class="hospital-info">
                <strong id="hospital-name">${hospital.name}</strong>
                <div class="hospital-address">
                  <img src="/static/hospital/images/location_icon.svg" alt="위치 아이콘" id="address-picture" />
                  <p id="address-text">${hospital.address}</p>
                </div>
              </div>
            </div>
          `;
          hospitalList.appendChild(card);
        });
      })
      .catch((err) => {
        hospitalList.innerHTML =
          "<p>병원 데이터를 불러오는 데 실패했습니다.</p>";
        console.error("병원 목록 API 오류:", err);
      });
  }
});
