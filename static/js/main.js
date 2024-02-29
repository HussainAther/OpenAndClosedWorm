function analyzeData() {
    fetch('/analyze', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        alert(data.message);
    })
    .catch(error => console.error('Error:', error));
}

