async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const messageEl = document.getElementById("message");

    if (!username || !password) {
        messageEl.textContent = "Please enter username and password";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        if (response.ok) {
            const data = await response.json();
            messageEl.style.color = "green";
            messageEl.textContent = `Login successful! Token: ${data.token}`;
            // You can store token in localStorage if needed
            // localStorage.setItem("token", data.token);
        } else if (response.status === 401) {
            messageEl.style.color = "red";
            messageEl.textContent = "Invalid credentials";
        } else {
            messageEl.style.color = "red";
            messageEl.textContent = "Login failed: " + response.statusText;
        }

    } catch (error) {
        messageEl.style.color = "red";
        messageEl.textContent = "Error connecting to server";
        console.error(error);
    }
}
