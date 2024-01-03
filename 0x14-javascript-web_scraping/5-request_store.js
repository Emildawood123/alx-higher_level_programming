#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
request.get(`${process.argv[2]}`, (err, res) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(`${process.argv[3]}`, res.body, 'utf-8', (er) => {
    if (er) {
      console.log(er);
    }
  });
});
