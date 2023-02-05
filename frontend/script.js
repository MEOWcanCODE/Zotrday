et serverUrl = 'https://paste-your-ngrok-link-here.ngrok.io';

function callBackend() {
    fetch(serverUrl)
        .then(res => res.json())
        .then(data => {
            document.getElementById('display').innerHTML = data.message
        })
}