#!/usr/bin/node
// function that prints num of args already printed,
// and the new argument value

let newArg = 0;

exports.logMe = function (item) {
  console.log(newArg + ': ' + item);
  newArg++;
};
