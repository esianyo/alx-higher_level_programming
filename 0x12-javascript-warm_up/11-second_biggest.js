#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
let max = -Infinity;
let secondMax = -Infinity;

if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax && args[i] < max) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
