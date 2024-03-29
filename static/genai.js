    // Function to send resume data to GenAI API
    function sendToGenAI() {
        // Get resume data from file or textarea
        const resumeData = document.getElementById('resume-file').files[0] || document.getElementById('resume-text').value;

        // Make HTTP request to GenAI API
        axios.post(
            'https://api.genai.ai/v1/check-resume',
            {
                resumeData: resumeData
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer AIzaSyD2oLQHkz9sYQvKZN6VaZ7ZI2t2N79wefQ' // Replace YOUR_API_KEY with your actual GenAI API key
                }
            }
        )
        .then(response => {
            // Handle API response
            console.log(response.data);
        })
        .catch(error => {
            // Handle error
            console.error(error);
        });
    }
