const apiUrl = "http://127.0.0.1:8000/api/sweets";

// Load all sweets and display in table
async function loadSweets() {
    try {
        const response = await fetch(apiUrl);
        const sweets = await response.json();
        const tbody = document.getElementById("sweetTableBody");
        tbody.innerHTML = "";

        sweets.forEach(sweet => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${sweet.id}</td>
                <td>${sweet.name}</td>
                <td>${sweet.price}</td>
                <td>${sweet.quantity}</td>
                <td>
                    <button onclick="editSweet(${sweet.id})">Edit</button>
                    <button onclick="deleteSweet(${sweet.id})">Delete</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error("Error loading sweets:", error);
    }
}

// Show/hide add sweet form
function showAddForm() {
    const form = document.getElementById("addForm");
    form.style.display = form.style.display === "none" ? "block" : "none";
}

// Add a new sweet
async function addSweet() {
    const name = document.getElementById("sweetName").value;
    const price = parseFloat(document.getElementById("sweetPrice").value);
    const quantity = parseInt(document.getElementById("sweetQuantity").value);

    if (!name || isNaN(price) || isNaN(quantity)) {
        alert("Please fill all fields correctly.");
        return;
    }

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, price, quantity })
        });
        const data = await response.json();
        alert(data.message);
        document.getElementById("sweetName").value = "";
        document.getElementById("sweetPrice").value = "";
        document.getElementById("sweetQuantity").value = "";
        loadSweets();
    } catch (error) {
        console.error("Error adding sweet:", error);
    }
}

// Edit a sweet
async function editSweet(id) {
    const name = prompt("Enter new sweet name:");
    const price = parseFloat(prompt("Enter new price:"));
    const quantity = parseInt(prompt("Enter new quantity:"));

    if (!name || isNaN(price) || isNaN(quantity)) {
        alert("All fields are required and must be valid.");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, price, quantity })
        });
        const data = await response.json();
        alert(data.message);
        loadSweets();
    } catch (error) {
        console.error("Error editing sweet:", error);
    }
}

// Delete a sweet
async function deleteSweet(id) {
    if (!confirm("Are you sure you want to delete this sweet?")) return;

    try {
        const response = await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
        const data = await response.json();
        alert(data.message);
        loadSweets();
    } catch (error) {
        console.error("Error deleting sweet:", error);
    }
}

// Load sweets on page load
loadSweets();
