#!/usr/bin/node
function largestNumber () {
  const args = process.argv.slice(2);

  if (args.length <= 1) {
    console.log(0);
    return;
  }

  let result = parseInt(args[0]);
  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (!isNaN(num) && num > result) {
      result = num;
    }
  }

  console.log(result);
}

largestNumber();
