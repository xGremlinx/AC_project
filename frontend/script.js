const API_URL = "http://aab6a415436674a68966e154c4a57142-1876901185.us-east-1.elb.amazonaws.com/users";

async function loadUsers() {

    const response = await fetch(API_URL);

    const users = await response.json();

    const table = document.getElementById("userTable");

    table.innerHTML = "";

    users.forEach(user => {

        const row = `
            <tr>
                <td>${user.id}</td>
                <td>${user.first_name}</td>
                <td>${user.last_name}</td>
                <td>${user.email}</td>
                <td>${user.age}</td>

                <td>
                    <button onclick="deleteUser(${user.id})">
                        Delete
                    </button>
                </td>
            </tr>
        `;

        table.innerHTML += row;
    });
}

async function saveUser() {

    const firstName =
        document.getElementById("firstName").value;

    const lastName =
        document.getElementById("lastName").value;

    const email =
        document.getElementById("email").value;

    const age =
        document.getElementById("age").value;

    await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            first_name: firstName,
            last_name: lastName,
            email: email,
            age: age
        })
    });

    document.getElementById("firstName").value = "";
    document.getElementById("lastName").value = "";
    document.getElementById("email").value = "";
    document.getElementById("age").value = "";

    loadUsers();
}

async function deleteUser(id) {

    await fetch(`${API_URL}/${id}`, {

        method: "DELETE"
    });

    loadUsers();
}

loadUsers();

const STATUS_URL = "http://localhost:30050/status";

async function loadStatus() {
    const response = await fetch(STATUS_URL);

    const data = await response.json();

    document.getElementById("backendStatus").innerText =
        "Backend Status: " + data.status;

    document.getElementById("serverTime").innerText =
        "Server Time: " + data.time;
}

setInterval(loadStatus, 1000);

window.onload = loadStatus;