#!/usr/bin/node
function add (a, b) {
  const args = process.argv.slice(2);
  a = parseInt(args[0]);
  b = parseInt(args[1]);
  const c = a + b;
  console.log(c);
}

add();
