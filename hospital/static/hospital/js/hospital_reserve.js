// 더미 데이터
const doctorData = [
  {
    id: 1,
    name: "정예진",
    hospital: "OO병원",
    phone: "02-1234-5678",

    weeklyAnswers: 20,
  },
  {
    id: 2,
    name: "이다은",
    hospital: "OO병원",
    phone: "02-1234-5678",
    weeklyAnswers: 20,
  },
  {
    id: 3,
    name: "박다영",
    hospital: "OO병원",
    phone: "02-1234-5678",
    weeklyAnswers: 20,
  },
  {
    id: 4,
    name: "김나영",
    hospital: "OO병원",
    phone: "02-1234-5678",
    weeklyAnswers: 20,
  },
  {
    id: 5,
    name: "김가영",
    hospital: "OO병원",
    phone: "02-1234-5678",
    weeklyAnswers: 20,
  },
];
// 본격 js 코드
document.addEventListener("DOMContentLoaded", () => {
  const listContainer = document.getElementById("doctor-list");

  doctorData.forEach((doctor, index) => {
    const card = document.createElement("div");
    card.className = "doctor-card";

    card.innerHTML = `
  <div class="doctor-info">
    <div class="doctor-ranking">${index + 1}</div>
    <div class="doctor-image">
      <img src="/static/hospital/images/sample_doctor.svg" alt="의사 샘플 이미지">
    </div>
    <div class="doctor-details">
    <div class="doctor-name-row">
      <p class="doctor-name">${
        doctor.name
      } <span class="doctor-hospital-name">${doctor.hospital}</span></p>
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
    listContainer.appendChild(card);
  });
});
