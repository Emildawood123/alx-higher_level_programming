#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let a = '';
    for (let i = 0; i < this.width; i++) {
      a += c;
    }
    for (let s = 0; s < this.height; s++) {
      console.log(a);
    }
  }
}
module.exports = Square;
