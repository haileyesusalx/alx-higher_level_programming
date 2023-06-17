#!/usr/bin/node
const myVar = 'X';
const args = process.argv.slice(2);
const num = parseInt(args);

if (args.length === 0) {
  console.log('Missing size');
} else if (isNaN(num)) {
  console.log('Missing size');
} else {
  let j = 0;
  while (j < num) {
    for (let i = 0; i < args.length; i++) {
      console.log(myVar.repeat(num));
    }
    j++;
  }
}
