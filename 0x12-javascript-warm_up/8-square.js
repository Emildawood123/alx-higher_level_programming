#!/usr/bin/node
const arg = process.argv[2]
if (arg === undefined || isNaN(parseInt(arg))) {
  console.log('Missing size');
} else if (parseInt(arg) < 0) {
  return;
} else {
  for (let i = 0; i < parseInt(arg); i++) {
    let str = '';
    for (let s = 0; s < parseInt(arg); s++) {
      str += 'X';
    }
    console.log(str);
  }
}
