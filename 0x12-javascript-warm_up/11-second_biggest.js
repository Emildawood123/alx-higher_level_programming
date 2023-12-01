#!/usr/bin/node
const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < len; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  console.log(arr.sort()[arr.length - 2]);
}
