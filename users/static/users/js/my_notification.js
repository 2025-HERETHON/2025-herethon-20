// 알림 페이지용 JS: 모두 읽음 처리 및 개별 읽음 처리

document.addEventListener("DOMContentLoaded", function () {
  // '모두 읽음 처리' 버튼 클릭 이벤트
  const readAllButton = document.getElementById("read-all");
  readAllButton.addEventListener("click", function () {
    const allItems = document.querySelectorAll(".notification-item.unread");
    // 모두 읽음 처리
    allItems.forEach((item) => {
      item.classList.remove("unread");
    });

    // 백엔드에 모든 알림 읽음 처리 요청
    // 문제 부분 주석 처리
    /*
    fetch("/users/notifications/mark_all_read/", {
      method: "POST",
      headers: {
        "X-CSRFToken": getCSRFToken(),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ action: "mark_all_read" }),
    });
    */
  });

  // 개별 알림 클릭 이벤트
  const notificationLinks = document.querySelectorAll(".notification-item a");
  notificationLinks.forEach((link) => {
    link.addEventListener("click", function () {
      const listItem = link.closest(".notification-item");
      if (listItem.classList.contains("unread")) {
        listItem.classList.remove("unread");

        // 알림 id 가져오기 (data-id 속성)
        const notificationId = listItem.dataset.id;

        // 백엔드에 알림 읽음 처리 요청
        // 문제 부분 주석 처리
        /*
        const notificationId = listItem.dataset.id;
        fetch(`/users/notifications/read/${notificationId}/`, {
          method: "POST",
          headers: {
            "X-CSRFToken": getCSRFToken(),
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ read: true }),
        });
        */
      }
    });
  });

  // HTML 내의 CSRF 토큰 추출
  function getCSRFToken() {
    const cookies = document.cookie.split("; ");
    for (let cookie of cookies) {
      if (cookie.startsWith("csrftoken=")) {
        return cookie.split("=")[1];
      }
    }
    return "";
  }
});
