const express = require('express');
const app = express();
const axios = require('axios');

app.post('/', async (req, res) => {
    axios.post('http://127.0.0.1:5000/process', {
        name: "gug",
        email: "terminal permission denied"
    }).then(data => {
        res.send(JSON.stringify(data));
    })
})

app.listen(3001, () => {
    console.log(`Example app listening on port 3001`)
})