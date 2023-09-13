#!/usr/bin/node
const firstArg = parseInt(args[0]);

if (!isNaN(firstArg)) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log("Not a number");
}