document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const firstName = document.getElementById('firstName').value.trim();
    const lastName = document.getElementById('lastName').value.trim();
    const email = document.getElementById('email').value.trim();

    // Validate that all fields are filled
    if (!firstName || !lastName || !email) {
        alert('Please fill out all fields.');
        return;
    }

    // Validate email format
    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    const formData = {
        firstName,
        lastName,
        email
    };

    // Disable submit button and show loading state
    const submitButton = document.getElementById('submit'); // Make sure this id matches the HTML
    submitButton.disabled = true;
    submitButton.textContent = 'Submitting...';

    fetch('https://9n333lv0gb.execute-api.ap-south-1.amazonaws.com/prod', { // Replace with your API Gateway URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        document.getElementById('message').textContent = 'Registration successful!';
        document.getElementById('registrationForm').reset(); // Reset form
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('message').textContent = 'Registration failed. Please try again.';
    })
    .finally(() => {
        // Re-enable submit button and reset text
        submitButton.disabled = false;
        submitButton.textContent = 'Submit';
    });
});

// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
