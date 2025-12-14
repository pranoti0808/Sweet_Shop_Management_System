const apiUrl = "http://127.0.0.1:8000/api/auth/register";

// Register function
async function registerUser() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        alert("Please enter both username and password.");
        return;
    }

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.message);
            // Redirect to login page after successful registration
            window.location.href = "login.html";
        } else {
            const errorData = await response.json();
            alert(errorData.detail);
        }
    } catch (error) {
        console.error("Error registering user:", error);
        alert("An error occurred. Please try again.");
