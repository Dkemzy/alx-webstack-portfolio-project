// logout.js

// Function to handle the logout process
function logout() {
  // Send a request to the logout route
  fetch('/logout', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // Optionally, you can send additional data in the request body
    // body: JSON.stringify({}),
  })
    .then(response => {
      // Check if the logout was successful
      if (response.ok) {
        // Redirect the user to the login page or any other desired location
        window.location.href = '/login.html';
      } else {
        // Handle the error case, such as displaying an error message
        console.error('Logout failed');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

// Attach an event listener to the logout button
document.addEventListener('DOMContentLoaded', function() {
  var logoutBtn = document.getElementById('logoutBtn');
  logoutBtn.addEventListener('click', logout);
});
