#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];
if (process.argv.length < 4) {
  console.log(NaN);
} else {
  const sum = parseInt(first) + parseInt(second);
  console.log(sum);
}
