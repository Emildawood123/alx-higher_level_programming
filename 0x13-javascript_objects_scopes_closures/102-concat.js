#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;
  const FirstFile = data.toString();
  fs.readFile(process.argv[3], (err, data) => {
    if (err) throw err;
    const SecondFile = data.toString();
    fs.writeFile(process.argv[4], FirstFile + '\n' + SecondFile + '\n', (err) => {
      if (err) throw err;
    });
  });
});
