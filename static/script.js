// Hamburger Menu Toggle for Mobile View
document.querySelector('.hamburger').addEventListener('click', function() {
    document.querySelector('.mobile-nav').classList.toggle('active');
});

// Copy Button Functionality
function copyToClipboard(id) {
    var textToCopy = document.getElementById(id).textContent;
    navigator.clipboard.writeText(textToCopy).then(function() {
        alert("Copied to clipboard!");
    }).catch(function(err) {
        alert("Error copying text: " + err);
    });
}

// Download Button Functionality for Thumbnails
function downloadThumbnail(url) {
    var a = document.createElement('a');
    a.href = url;
    a.download = "thumbnail.jpg"; // You can specify the name you want for the file here.
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Form submit for various tools (Tag generator, etc.)
document.querySelectorAll('form').forEach(function(form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();  // Prevent the form from refreshing the page
        var actionUrl = form.action;
        var formData = new FormData(form);

        fetch(actionUrl, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Handle the response and display the generated data
                document.getElementById('result').innerHTML = data.result;
            } else {
                alert('There was an issue with the tool. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Something went wrong. Please try again.');
        });
    });
});
