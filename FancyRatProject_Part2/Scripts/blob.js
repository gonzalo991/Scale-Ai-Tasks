// Create a Blob from an image URL
const imageUrl = 'https://example.com/your-image.jpg'; // Replace with your image URL
fetch(imageUrl)
    .then(response => response.blob())
    .then(blob => {
        // Blob created, now send it via AJAX
        sendBlobViaAjax(blob);
    })
    .catch(error => {
        console.error('Error fetching the image:', error);
    });

// Function to send the Blob via AJAX
function sendBlobViaAjax(blob) {
    const xhr = new XMLHttpRequest();
    const url = 'https://example.com/your/endpoint'; // Replace with your server's URL

    xhr.open('POST', url, true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log('Image sent successfully');
        } else {
            console.error('Error sending the image:', xhr.status, xhr.statusText);
        }
    };

    xhr.onerror = function () {
        console.error('Network error while sending the image');
    };

    const formData = new FormData();
    formData.append('image', blob, 'image.jpg'); // 'image' is the field name; replace 'image.jpg' with the desired filename

    xhr.send(formData);
}