const API_KEY = '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';
const API_URL = 'https://api.groq.com/openai/v1/chat/completions';

const chatDisplay = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-btn');

async function fetchGroqData(messages) {
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
            throw new Error(`API Error: ${response.status}`);
        }
        
        const data = await response.json();
        return data.choices[0]?.message?.content || 'No response from AI';
    } catch (error) {
        console.error('Fetch error:', error);
        return 'Error fetching response. Please try again later.';
    }
}

function appendMessage(content, isUser = false, isError = false) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = content;
    messageDiv.classList.add('chat-message');
    if (isUser) messageDiv.classList.add('user-message');
    else if (isError) messageDiv.classList.add('error-message');
    else messageDiv.classList.add('bot-message');
    
    chatDisplay.appendChild(messageDiv);
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}

async function handleUserInput() {
    const message = userInput.value.trim();
    if (!message) return;
    
    appendMessage(message, true);
    userInput.value = '';
    
    const messages = [{ role: 'user', content: message }];
    const botResponse = await fetchGroqData(messages);
    
    appendMessage(botResponse, false, botResponse.startsWith('Error'));
}

sendButton.addEventListener('click', handleUserInput);
userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') handleUserInput();
});

document.addEventListener('DOMContentLoaded', () => {
    chatDisplay.innerHTML = '';
    appendMessage('Hello, Siddharth.', false);
});
