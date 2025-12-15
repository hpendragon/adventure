let gameHistory = [];

function sendCommand() {
    const input = document.getElementById('command-input');
    const command = input.value.trim();
    
    if (command === '') return;

    fetch('/game/action', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: command })
    })
    .then(response => response.json())
    .then(data => {
        updateGameOutput(data);
        input.value = '';
    })
    .catch(error => console.error('Error:', error));
}

function updateGameOutput(data) {
    const output = document.getElementById('game-output');
    const newEntry = document.createElement('div');
    newEntry.textContent = data.response;
    output.appendChild(newEntry);
    output.scrollTop = output.scrollHeight;
}

// Initialize game
document.addEventListener('DOMContentLoaded', function() {
    // Initial game setup
});
