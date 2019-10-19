const express = require('express')
var cors = require("cors");
const app = express()

const PORT = process.env.PORT || 3000

app.use(express.json())
app.use(cors())

app.post('/', async (req, res) => {
    const d = req.body
    const spawn = require('child_process').spawn
    const process = spawn('python', ["./knn_prediction.py", d.sepal, d.swidth, d.petal, d.pwidth])
    process.stdout.on('data', function (data) {
        res.send(data.toString());
    })
})

app.listen(PORT, () => {
    console.log('Server has started on ' + PORT)
})