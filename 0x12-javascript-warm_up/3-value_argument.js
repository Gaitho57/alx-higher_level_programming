#!/usr/bin/node

const arguments = process.argv.slice(2);

if (!arguments[0]){
    console.log("No argument");
}
else{
    console.log(arguments[0]);
} 