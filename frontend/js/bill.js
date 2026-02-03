async function generateBill() {
    const item = document.getElementById("item").value;
    const price = parseFloat(document.getElementById("price").value);
    const messageEl = document.getElementById("message");

    if (!item || isNaN(price)) {
        messageEl.style.color = "red";
        messageEl.textContent = "Please enter valid item name and price";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/generate_bill", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount: price })
});

        

        if (response.ok) {
            const data = await response.json();
            messageEl.style.color = "green";
            messageEl.innerHTML = `
                Bill generated successfully!<br>
                Bill ID: ${data.bill_id}<br>
                Amount: ${data.amount}<br>
                Status: ${data.status}<br>
                Time: ${data.timestamp}
            `;
        } else {
            messageEl.style.color = "red";
            messageEl.textContent = "Failed to generate bill: " + response.statusText;
        }

    } catch (error) {
        messageEl.style.color = "red";
        messageEl.textContent = "Error connecting to server";
        console.error(error);
    }
}
