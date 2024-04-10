const chatInput = document.getElementById('chat-input');
const sendButton = document.getElementById('send-button');
const messageList = document.querySelector('.message-list');

sendButton.addEventListener('click', sendMessage);

function sendMessage() {
    const message = chatInput.value.trim();

    if (message) {
        addUserMessage(message);
        chatInput.value = ''; // Clear input

        // Placeholder for bot response
        setTimeout(addBotMessage, 1000, "I'm still learning. How can I help you?"); 
    }
}

function addUserMessage(message) {
    const li = createMessageElement(message, 'user');
    messageList.appendChild(li);
}

function addBotMessage(message) {
    const li = createMessageElement(message, 'bot');
    messageList.appendChild(li);
}

function createMessageElement(message, className) {
    const li = document.createElement('li');
    li.classList.add(className);
    li.textContent = message;
    return li;
}
