const mongoose = require("mongoose");

const scanSchema = new mongoose.Schema({
  shop_id: String,
  scan_time: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model("Scan", scanSchema);