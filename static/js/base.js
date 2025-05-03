const profileLink = document.getElementById("profile-link");
const profilePanel = document.getElementById("profile-panel");
const profileContent = document.getElementById("profile-content");

profileLink.addEventListener("click", function (e) {
  e.preventDefault();
  fetch(window.profileUrl)  // <-- теперь работает!
    .then(response => response.text())
    .then(html => {
      const container = document.createElement('div');
      container.innerHTML = html;
      const content = container.querySelector('.profile-content');
      const currentContent = profileContent.querySelector('.profile-content');
      if (currentContent) currentContent.remove();
      profileContent.appendChild(content);
      profilePanel.classList.add("open");
    });
});

// ✖ кнопка
document.getElementById("close-profile-panel").addEventListener("click", function () {
  profilePanel.classList.remove("open");
});

// Клик вне панели
document.addEventListener("click", function (e) {
  if (profilePanel.classList.contains("open") &&
      !profilePanel.contains(e.target) &&
      e.target !== profileLink) {
    profilePanel.classList.remove("open");
  }
});
