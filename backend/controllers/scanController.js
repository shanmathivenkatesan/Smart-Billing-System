const Scan = require("../models/scan");

exports.handleScan = async (req, res) => {
  const shopId = req.query.shop_id;

  await Scan.create({ shop_id: shopId });

  res.send(`QR scanned for shop ${shopId}`);
};