#!/usr/bin/node
first = process.argv[2];
second = process.argv[3];
if (process.argv.length < 4) {
  console.log(NaN);
} else {
  let sum = parseInt(first) + parseInt(second);
  console.log(sum);
}
