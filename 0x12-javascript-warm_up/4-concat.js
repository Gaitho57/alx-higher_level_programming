#!/usr/bin/node

const arguments = process.argv.slice(2);

let FirstVar = arguments[0];
let SecondVar = arguments[1];

FirstVar || 'undefined';
SecondVar || 'undefined';

console.log(`{FirstVar} is {SecondVar}`);
