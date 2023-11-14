#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0 || typeof h === 'number' || typeof w === 'number') {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
