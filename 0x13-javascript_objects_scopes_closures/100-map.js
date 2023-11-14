#!/usr/bin/node
const list = require('./100-data');
console.log(list.list);
const newList = list.list;
const elselist = newList.map((n, i) => {
  return n * i;
});
console.log(elselist);
