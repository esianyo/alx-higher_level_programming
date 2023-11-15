#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);
let i = 0;

if (isNaN(x)) {
  console.log('Missing nuber of occurrences');
} else {
  for (; i < x; i++) {
    console.log('C is fun');
  }
}
