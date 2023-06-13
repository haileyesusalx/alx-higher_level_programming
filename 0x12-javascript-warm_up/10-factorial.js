#!/usr/bin/node
function factorial () {
  const args = process.argv.slice(2);
  const num = parseInt(args);
  if (num < 0) {
    console.log('try again');
  } else {
    let result = 1;
    for (let i = 2; i <= num; i++) {
      result *= i;
    }
    console.log(result);
  }
}

factorial();
