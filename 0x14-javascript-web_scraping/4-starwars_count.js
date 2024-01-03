#!/usr/bin/node
const request = require('request');
const process = require('process');
request.get(process.argv[2], (err, res) => {
  if (err) {
    console.log(err);
  }
  let count = 0;
  const list = JSON.parse(res.body).results;
  for (let i = 0; i < list.length; i++) {
    for (let j = 0; j < list[i].characters.length; j++) {
      if (list[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
