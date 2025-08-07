// COPY BUTTON FUNCTIONALITY
function copyToClipboard(textId) {
    const text = document.getElementById(textId).innerText;
    navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard!");
    });
}

// DOWNLOAD BUTTON FUNCTIONALITY
function downloadContent(textId, filename = "yt-tool-output.txt") {
    const text = document.getElementById(textId).innerText;
    const element = document.createElement('a');
    const file = new Blob([text], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = filename;
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

// MOBILE MENU TOGGLE
function toggleMenu() {
    const menu = document.getElementById("mobileMenu");
    menu.classList.toggle("hidden");
}
