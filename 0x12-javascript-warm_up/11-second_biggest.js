#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  let first = parseInt(args[0]);
  let second = parseInt(args[1]);

  if (second > first) {
    [first, second] = [second, first];
  }

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num !== first) {
      second = num;
    }
  }

  console.log(second);
}
