#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg[0] === undefined) {
  console.log('No argument');
} else if (arg[1] === undefined) {
  console.log(arg[0]);
} else if (arg[2] === undefined) {
  console.log(arg[0], arg[1]);
} else {
  console.log(arg[0], arg[1], arg[2]);
}
