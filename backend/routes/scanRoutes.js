const express = require("express");
const router = express.Router();
const { handleScan } = require("../controllers/scanController");

router.get("/", handleScan);

module.exports = router;