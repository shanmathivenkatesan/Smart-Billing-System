const express = require("express");
const dotenv = require("dotenv");
const connectDB = require("./config/db");

dotenv.config();
connectDB();

const app = express();
app.use(express.json());

app.use("/api/shop", require("./routes/shopRoutes"));
app.use("/api/scan", require("./routes/scanRoutes"));
app.use("/api/transaction", require("./routes/transactionRoutes"));

app.get("/", (req, res) => {
  res.send("AIAG03 Backend Running");
});