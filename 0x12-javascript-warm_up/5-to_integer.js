#!/usr/bin/node
function typeArgument () {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Not a number');
  }

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args);

    if (isNaN(num)) {
      console.log('Not a number');
    } else {
      console.log('My number: ' + num);
    }
  }
}

typeArgument();
