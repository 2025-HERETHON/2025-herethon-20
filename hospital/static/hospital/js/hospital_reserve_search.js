// // 더미 데이터
// const doctorData = [
//   {
//     id: 1,
//     name: "정예진",
//     hospital: "가가병원",
//     phone: "02-1234-5678",

//     weeklyAnswers: 20,
//   },
//   {
//     id: 2,
//     name: "이다은",
//     hospital: "가나병원",
//     phone: "02-1234-5678",
//     weeklyAnswers: 20,
//   },
//   {
//     id: 3,
//     name: "박다영",
//     hospital: "가다병원",
//     phone: "02-1234-5678",
//     weeklyAnswers: 20,
//   },
//   {
//     id: 4,
//     name: "김나영",
//     hospital: "가라병원",
//     phone: "02-1234-5678",
//     weeklyAnswers: 20,
//   },
//   {
//     id: 5,
//     name: "김가영",
//     hospital: "가마병원",
//     phone: "02-1234-5678",
//     weeklyAnswers: 20,
//   },
// ];

// 검색 결과 렌더링
document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const query = params.get("q");
  const main = document.querySelector("main");

  // 검색창 input에 검색어 유지
  const searchInput = document.querySelector("input[name='q']");
  if (query && searchInput) {
    searchInput.value = query;
  }
  if (!query) return;

  // 검색어로 필터링
  const filtered = doctorData.filter(
    (doc) => doc.name.includes(query) || doc.hospital.includes(query)
  );

  // 검색 결과 없으면 안내문
  if (filtered.length === 0) {
    main.innerHTML = `<p class="no-result">검색 결과가 없습니다.</p>`;
    return;
  }

  // 검색 결과 타이틀
  const resultCount = document.createElement("p");
  resultCount.className = "result-count";
  resultCount.innerHTML = `검색 결과 <span id="bold-count">${filtered.length}</span>개`;
  main.appendChild(resultCount);

  // 결과 목록 생성
  filtered.forEach((doctor, index) => {
    const card = document.createElement("div");
    card.className = "doctor-card";

    card.innerHTML = `
      <div class="doctor-info">
        <div class="doctor-ranking">${index + 1}</div>
        <div class="doctor-image">
          <img src="/static/hospital/images/sample_doctor.svg" alt="의사 샘플 이미지" />
        </div>
        <div class="doctor-details">
          <div class="doctor-name-row">
            <p class="doctor-name">${doctor.name}
              <span class="doctor-hospital-name">${doctor.hospital}</span>
            </p>
          </div>
          <div class="doctor-tel-row">
            <img src="/static/hospital/images/call_icon.svg" alt="전화 아이콘" />
            <p class="phone-text">${doctor.phone}</p>
            <a href="#" class="copy-phone">복사</a>
          </div>
          <div class="doctor-answer-row">
            <p class="answer-count">🔥 최근 일주일 간 답변 수 ${
              doctor.weeklyAnswers
            }개</p>
          </div>
        </div>
      </div>
    `;
    // 복사 이벤트 등록
    card.querySelector(".copy-phone").addEventListener("click", (e) => {
      e.preventDefault();
      const phone = card.querySelector(".phone-text").textContent;
      navigator.clipboard.writeText(phone).then(() => {
        alert(`전화번호가 복사되었습니다: ${phone}`);
      });
    });
    main.appendChild(card);
  });
});
