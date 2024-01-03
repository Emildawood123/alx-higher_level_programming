#!/usr/bin/node
const request = require('request');
const process = require('process');
request.get(process.argv[2], (err, res) => {
  if (err) {
    console.log(err);
  }
  const list = JSON.parse(res.body);
  const obj = {};
  for (let i = 1; i < 11; i++) {
    obj[i] = 0;
  }
  for (let j = 0; j < list.length; j++) {
    if (list[j].completed === true) {
      obj[list[j].userId] = obj[list[j].userId] + 1;
    }
  }
  console.log(obj);
});
