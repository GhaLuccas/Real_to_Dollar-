document.getElementById('convert-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const amount = parseFloat(document.getElementById('amount').value);
    const resultDiv = document.getElementById('result');

    if (isNaN(amount) || amount <= 0) {
        resultDiv.textContent = 'Please enter a valid amount.';
        return;
    }

    try {
        const response = await fetch('http://localhost:8000/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ amount }),
        });

        if (!response.ok) {
            throw new Error('Failed to convert currency.');
        }

        const data = await response.json();
        resultDiv.textContent = `${data.brl_amount} BRL = ${data.usd_converted} USD`;
    } catch (error) {
        resultDiv.textContent = 'Error: ' + error.message;
    }
});
