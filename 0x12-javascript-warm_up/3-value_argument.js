#!/usr/bin/node
function numberArgument () {
  const args = process.argv.slice(2);
  const numArgs = args.length;
  if (numArgs === 0) {
    console.log('No argument');
  } else {
    console.log(args[0]);
  }
}

numberArgument();
