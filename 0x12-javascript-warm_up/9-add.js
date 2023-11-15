#!/usr/bin/node
let a = process.argv[2];
let b = process.argv[3];

a = parseInt(a);
b = parseInt(b);

function add (a, b) {
  return a + b;
}

if (isNaN(a) || isNaN(b)) {
  console.log('Both arguments must be integers');
} else {
  console.log(add(a, b));
}
