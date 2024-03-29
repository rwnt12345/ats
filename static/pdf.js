function extractTextFromPDF() {
  const form = document.getElementById('pdf-upload-form');
  const formData = new FormData(form);
  
  // Update the endpoint URL to match your server-side implementation
  const endpointURL = '/extract-text';

  fetch(endpointURL, {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Assuming the server responds with an object containing 'text' property
    if (data && data.text) {
      document.getElementById('extracted-text').innerText = data.text;
    } else {
      throw new Error('Invalid response from server');
    }
  })
  .catch(error => {
    // Improve error handling - Display an error message to the user
    console.error('Error:', error);
    alert('An error occurred while processing the request. Please try again later.');
  });
}
