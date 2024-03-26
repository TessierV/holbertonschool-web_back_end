const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 7865;

app.get('/', (req, res) => res.end('Welcome to the payment system'));
app.get('/cart/:id(\\d+)', (req, res) => {
    const cartId = req.params.id;
    res.end(`Payment methods for cart ${cartId}`);
});
app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});
app.post('/login', (req, res) => {
    const { userName } = req.body;
    res.end(`Welcome ${userName}`);
});
app.listen(port, () => console.log(`API available on localhost port ${port}`));
