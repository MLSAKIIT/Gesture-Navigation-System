var express = require('express');
var router = express.Router();

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

/* GET contact page. */
router.get('/ContactUs', function(req, res, next) {
  res.render('contact');
});

module.exports = router;
