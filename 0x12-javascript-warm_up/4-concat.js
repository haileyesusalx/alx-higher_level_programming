#!/usr/bin/node
function numberArgument () {
  const args = process.argv.slice(2);
  console.log(args[0] + ' is ' + args[1]);
}

numberArgument();
