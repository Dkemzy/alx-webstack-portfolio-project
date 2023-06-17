// Get the logout button element
const logoutBtn = document.getElementById('logoutBtn');

// Add a click event listener to the logout button
logoutBtn.addEventListener('click', logout);

// Logout function
function logout() {
  // Perform the logout operation here

  // Redirect to the home page
  window.location.href = 'index.html';
}
