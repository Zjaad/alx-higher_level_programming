#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
