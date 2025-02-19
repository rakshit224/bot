// Description: This file contains the JavaScript code for the chatbot.
const API_KEY = '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'; 
const API_URL = 'https://api.groq.com/openai/v1/chat/completions';

const chatDisplay = document.getElementById('chat-display');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-btn');

async function fetchAIResponse(messages) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`
            },
            body: JSON.stringify({
                model: 'mixtral-8x7b-32768',
                messages: messages
            })
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.statusText}`);
        }

        const data = await response.json();
        return data.choices?.[0]?.message?.content || 'No response received.';
    } catch (error) {
        console.error('Error fetching response:', error);
        return 'Error fetching response. Please try again later.';
    }
}

function appendMessage(content, isUser = false, isError = false) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = content;
    messageDiv.classList.add('chat-message');

    if (isUser) {
        messageDiv.classList.add('user-message');
    } else if (isError) {
        messageDiv.classList.add('error-message');
    } else {
        messageDiv.classList.add('bot-message');
    }

    chatDisplay.appendChild(messageDiv);
    chatDisplay.scrollTop = chatDisplay.scrollHeight; // Auto-scroll to latest message
}

async function handleUserInput() {
    const message = userInput.value.trim();
    if (!message) return;

    appendMessage(message, true);
    userInput.value = '';

    appendMessage('Thinking...', false); // Temporary loading message

    const messages = [{ role: 'user', content: message }];
    const botResponse = await fetchAIResponse(messages);

    // Remove the "Thinking..." message
    chatDisplay.removeChild(chatDisplay.lastChild);
    
    appendMessage(botResponse, false, botResponse.includes('Error'));
}

// Event Listeners
sendButton.addEventListener('click', handleUserInput);
userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        handleUserInput();
    }
});
