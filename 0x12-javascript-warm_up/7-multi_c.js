!/usr/bin/node

const args = process.argv.slice(2);

const parse = parseInt(args[0]);

if (isNaN(parse)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < parse; i++) {
        console.log("C is fun");
    }
}