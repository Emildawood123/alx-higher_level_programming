#!/usr/bin/node
const fs = require('fs');
const process = require('process');
fs.readFile(process.argv[2], 'utf-8', (err, res) => {
  try {
    console.log(res);
  } catch {
    console.log(err);
  }
});
