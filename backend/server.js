const express = require('express');
const path = require('path');
const app = express();
const detector = require('./detector');
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, '../frontend')));

app.post('/api/check', (req, res) => {
    const { url } = req.body;
    const isPhishing = detector.detectPhishing(url);
    res.json({ url, isPhishing });
});

app.listen(PORT, () => {
    console.log(`Phishing API running at http://localhost:${PORT}`);
});
