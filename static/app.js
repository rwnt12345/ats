const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

	document.addEventListener("DOMContentLoaded", function() {
    // Find the login button by its id
    var loginBtn = document.getElementById("login-btn");

    // Add click event listener to login button
    loginBtn.addEventListener("click", function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();
        
        // Redirect to the index page
        window.location.href = "index.html";
    });

    document.addEventListener("DOMContentLoaded", function() {
    // Find the signup button by its id
    var signupBtn = document.getElementById("signup-btn");

    // Add click event listener to signup button
    signupBtn.addEventListener("click", function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();
        
        // Simulate a successful signup by showing an alert or message
        alert("Signup successful! You will now be redirected to the login page.");

        // Redirect to the login page after a short delay
        setTimeout(function() {
            window.location.href = "login.html";
        }, 2000); // 2000 milliseconds = 2 seconds
    });
});
});