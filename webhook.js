
const express = require("express");
const app = express();
app.use(express.json());


app.post("/Webhook", (req, res) => {

    console.log("Webhook Recieved!");
    console.log("Data: ", req.body);


    res.status(200).json({message: "Webhook recieved Successfully"});
});

app.listen (3000, () => {
    console.log("Webhook server running on port 3000");

});