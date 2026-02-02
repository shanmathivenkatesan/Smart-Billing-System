function generateBill() {
  fetch("http://localhost:5000/api/bill", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      item: document.getElementById("item").value,
      price: document.getElementById("price").value
    })
  })
  .then(res => res.json())
  .then(data => alert("Bill Generated Successfully"))
  .catch(() => alert("Error generating bill"));
}