document.addEventListener("DOMContentLoaded", function () {
  const splashScreen = document.getElementById("splashScreen");

  if (splashScreen) {
    setTimeout(() => {
      splashScreen.classList.add("hidden");
    }, 1500);
  }
});