function classifyText() {
    var text = document.getElementById("textInput").value.trim();

    if (text === "") {
        alert("Please enter some text to classify.");
        return;
    }

    fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        var resultDiv = document.getElementById("result");
        if (data.prediction === 1) {
            resultDiv.textContent = "The text is AI-generated.";
        } else {
            resultDiv.textContent = "The text is human-written.";
        }
    })
    .catch(error => console.error('Error:', error));
}
