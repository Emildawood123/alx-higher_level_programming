#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a = '';
    for (let i = 0; i < this.width; i++) {
      a += 'X';
    }
    for (let s = 0; s < this.height; s++) {
      console.log(a);
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
