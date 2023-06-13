#!/usr/bin/node
const myVar = 'C is fun';
const args = process.argv.slice(2);
const num = parseInt(args);

if (args.length === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(myVar);
  }
}
