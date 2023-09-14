#!/usr/bin/node
// class Square that defines square and inherits from 5-square.js

const NewSquare = require('./5-square');

class Square extends NewSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let k = '';
      for (let j = 0; j < this.width; j++) {
        k += c;
      }
      console.log(k);
    }
  }
}

module.exports = Square;
