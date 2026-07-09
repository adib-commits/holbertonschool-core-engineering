const socket = new WebSocket("ws://localhost:8000/ws");

const messages = document.querySelector("#messages");
const input = document.querySelector("#messageInput");
const button = document.querySelector("#sendButton");


function displayMessage(message) {
    const div = document.createElement("div");

    div.classList.add("message");
    div.textContent = message;

    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}


socket.onopen = () => {
    displayMessage("Connected to server");
};


socket.onmessage = (event) => {
    displayMessage("Server: " + event.data);
};


socket.onclose = () => {
    displayMessage("Connection closed");
};


button.addEventListener("click", () => {
    const message = input.value;

    if (message !== "") {
        socket.send(message);
        displayMessage("You: " + message);
        input.value = "";
    }
});


input.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        button.click();
    }
});
