
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const previewBtn = document.getElementById('preview-btn');
    const previewImage = document.getElementById('preview-image');
    const previewContainer = document.getElementById('preview-container');

    const downloadRotatedBtn = document.getElementById('download-rotated-btn');

    previewBtn.addEventListener('click', async () => {
        const formData = new FormData(form);
        const params = new URLSearchParams(formData);

        // Add action=preview to the query string
        const response = await fetch(`/generate?action=preview`, {
            method: 'POST',
            body: params
        });

        if (response.ok) {
            const imageBlob = await response.blob();
            const imageUrl = URL.createObjectURL(imageBlob);
            previewImage.src = imageUrl;
            previewContainer.style.display = 'block';
        } else {
            alert('Error generating preview.');
        }
    });

    downloadRotatedBtn.addEventListener('click', () => {
        // Create a hidden input to send the action to the backend
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'action';
        hiddenInput.value = 'download_rotated';
        form.appendChild(hiddenInput);

        // Submit the form
        form.submit();

        // Remove the hidden input after submission to avoid affecting subsequent submissions
        form.removeChild(hiddenInput);
    });
});
