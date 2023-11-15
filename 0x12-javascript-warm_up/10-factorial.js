#!/usr/bin/node
let n = process.argv[2];
n = parseInt(n);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(n));
