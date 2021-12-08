var express = require('express');
var router = express.Router();
const path = require("path");
const {Router} = require("express");
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

/* GET about page. */
router.get('/About', function(req, res, next) {
  res.render('about');
});

/* GET viewMore1 page. */
router.get('/viewMore1', function(req, res, next) {
  res.render('viewMore1');
});

/* GET viewMore2 page. */
router.get('/viewMore2', function(req, res, next) {
  res.render('viewMore2');
});

/* GET viewMore3 page. */
router.get('/viewMore3', function(req, res, next) {
  res.render('viewMore3');
});

/* GET WhiteBoard page. */
router.get('/WhiteBoard', function(req, res, next) {
  router.use(express.static(path.join(__dirname, '../build')));
  res.sendFile(path.join(__dirname,'../build','index.html'));
});

module.exports = router;
