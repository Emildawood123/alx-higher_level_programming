#!/usr/bin/node
const request = require('request');
const process = require('process');
request.get(process.argv[2], (err, res) => {
  if (err) {
    console.log(`code: ${err}`);
  }
  console.log(`code: ${res.statusCode}`);
});
