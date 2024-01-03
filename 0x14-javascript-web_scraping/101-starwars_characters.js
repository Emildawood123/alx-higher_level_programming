#!/usr/bin/node
const request = require('request');
const process = require('process');
request.get('https://swapi-api.alx-tools.com/api/films', (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  const obj = JSON.parse(res.body);
  const list = obj.results[process.argv[2] - 1].characters;
  for (let i = 0; i < list.length; i++) {
    request.get(list[i], (err, res) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(res.body).name);
    });
  }
});
