let serverUrl = "https://b587-169-234-118-86.ngrok.io/";

function callBackend() {
    fetch(serverUrl)
        .then(res => res.json())
        .then(data => {
            document.getElementById('display').innerHTML = data.message
        })
}