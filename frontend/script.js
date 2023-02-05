let serverUrl = "https://2305-169-234-118-86.ngrok.io";

function callBackend() {
    fetch(serverUrl)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            document.getElementById('display').innerHTML = JSON.stringify(data)
        })
}