// static/script.js
function toggleMenu() {
  const menu = document.getElementById("navMenu");
  menu.classList.toggle("active");
}
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert("Copied to clipboard!");
  });
}
