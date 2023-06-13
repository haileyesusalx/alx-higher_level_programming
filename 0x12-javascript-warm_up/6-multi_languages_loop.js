#!/usr/bin/node
const myVar = 'C is fun';
const myVar2 = 'Python is cool';
const myVar3 = 'JavaScript is amazing';

for (let i = 0; i < 3; i++) {
  if (i === 0) {
    console.log(myVar);
  } else if (i === 1) {
    console.log(myVar2);
  } else {
    console.log(myVar3);
  }
}
