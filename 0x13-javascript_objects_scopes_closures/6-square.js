#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
   if (c === undefined) {
    const c = 'X';
   }
    console.log((c.repeat(this.width) + '\n').repeat(this.height - 1) = c.repeat(this.width));
  }
 }
module.exports = Square;
