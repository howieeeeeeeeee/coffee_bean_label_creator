
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const previewBtn = document.getElementById('preview-btn');
    const previewImage = document.getElementById('preview-image');
    const previewPlaceholder = document.getElementById('preview-placeholder');
    const downloadRotatedBtn = document.getElementById('download-rotated-btn');

    // Initial state: hide image, show placeholder
    previewImage.style.display = 'none';
    previewPlaceholder.style.display = 'block';

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
            previewImage.style.display = 'block'; // Show image
            previewPlaceholder.style.display = 'none'; // Hide placeholder
        } else {
            alert('Error generating preview.');
            previewImage.style.display = 'none'; // Hide image on error
            previewPlaceholder.style.display = 'block'; // Show placeholder on error
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
