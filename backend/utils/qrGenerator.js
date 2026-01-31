const QRCode = require("qrcode");

const generateQR = async (shopId) => {
  const url = `http://localhost:5000/api/scan?shop_id=${shopId}`;
  const qr = await QRCode.toDataURL(url);
  return qr;
};

module.exports = generateQR;