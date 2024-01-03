#!/usr/bin/node
const request = require('request');
const process = require('process');
request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, res) => {
  if (err) {
    console.log(`code: ${err}`);
  }
  console.log(`${JSON.parse(res.body).title}`);
});
