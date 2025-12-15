let gameHistory = [];

document.addEventListener('DOMContentLoaded', function() {
    sendCommand('start');
});

function sendCommand(command = null) {
    const input = document.getElementById('command-input');
    const cmd = command || input.value.trim();
    
    if (cmd === '') return;

    // Add user input to output
    if (cmd !== 'start') {
        addUserInput(cmd);
    }

    fetch('/game/action', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: cmd })
    })
    .then(response => response.json())
    .then(data => {
        updateGameOutput(data);
        input.value = '';
    })
    .catch(error => {
        const output = document.getElementById('game-output');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = 'An error occurred. Please try again.';
        output.appendChild(errorDiv);
        console.error('Error:', error);
    });
}

function addUserInput(command) {
    const output = document.getElementById('game-output');
    
    // Add separator
    const separator = document.createElement('div');
    separator.className = 'interaction-separator';
    output.appendChild(separator);
    
    // Add user command
    const inputDiv = document.createElement('div');
    inputDiv.className = 'user-input';
    inputDiv.textContent = '> ' + command;
    output.appendChild(inputDiv);
}

function updateGameOutput(data) {
    const output = document.getElementById('game-output');
    
    // Add story message
    const messageDiv = document.createElement('div');
    messageDiv.className = 'story-message';
    messageDiv.textContent = data.message;
    output.appendChild(messageDiv);
    
    // Add available choices
    if (data.choices && data.choices.length > 0) {
        const choicesDiv = document.createElement('div');
        choicesDiv.className = 'choices';
        choicesDiv.textContent = 'Available actions: ' + data.choices.join(', ');
        output.appendChild(choicesDiv);
    }
    
    // Scroll to bottom
    output.scrollTop = output.scrollHeight;
}

// Handle Enter key in input
document.getElementById('command-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendCommand();
    }
});
