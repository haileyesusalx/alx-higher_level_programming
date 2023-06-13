#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined) {
    console.log("no argument");
} else {
    console.log(arg);
}
