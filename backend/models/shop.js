const mongoose = require("mongoose");

const shopSchema = new mongoose.Schema({
  shop_id: String,
  shop_name: String,
  shop_type: String,
  created_at: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model("Shop", shopSchema);