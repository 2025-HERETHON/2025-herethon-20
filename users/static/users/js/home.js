document.addEventListener("DOMContentLoaded", function () {
  const card = document.getElementById("cardnews1");
  const popup = document.getElementById("popup");
  const popupImage = document.getElementById("popupImage");

  card.addEventListener("click", function () {
    popup.style.display = "flex";
  });

  popupImage.addEventListener("click", function () {
    popup.style.display = "none";
  });
});
