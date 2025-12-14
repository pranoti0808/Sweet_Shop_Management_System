const registerApi = "http://127.0.0.1:8000/api/auth/register";

async function registerUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) {
        alert("Username and password required");
        return;
    }

    try {
        const response = await fetch(registerApi, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);
        } else {
            alert(data.detail);
        }

    } catch (err) {
        console.error(err);
        alert("Server error");
    }
}
