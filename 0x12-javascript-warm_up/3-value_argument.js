#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg === undefined) {
  console.log('no argument');
} else {
  console.log(arg[0], arg[1]);
}
