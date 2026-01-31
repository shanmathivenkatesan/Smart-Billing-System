const Shop = require("../models/shop");
const generateQR = require("../utils/qrGenerator");

exports.registerShop = async (req, res) => {
  try {
    const shopId = "SHOP_" + Date.now();

    const shop = new Shop({
      shop_id: shopId,
      shop_name: req.body.shop_name,
      shop_type: req.body.shop_type
    });

    await shop.save();
    const qrCode = await generateQR(shopId);

    res.json({
      message: "Shop registered successfully",
      shop,
      qrCode
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};