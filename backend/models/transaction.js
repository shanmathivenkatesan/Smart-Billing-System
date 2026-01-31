const mongoose = require("mongoose");

const transactionSchema = new mongoose.Schema({
  shop_id: String,
  amount: Number,
  payment_mode: String,
  created_at: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model("Transaction", transactionSchema);