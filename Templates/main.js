// This code is not necessary for the page to work, but it adds some additional functionality.

window.onload = function() {
  // When the page loads, hide the menu drop down.
  document.getElementById("menu").style.display = "none";

  // When the user clicks on the logo, show the menu drop down.
  document.getElementById("logo").onclick = function() {
    document.getElementById("menu").style.display = "block";
  };

  // When the user clicks outside of the menu drop down, hide it.
  document.addEventListener("click", function(event) {
    if (event.target === document.getElementById("menu")) {
      document.getElementById("menu").style.display = "none";
    }
  });
};

