#!/usr/bin/node
/*
 Factorial
 */

function factorial (n) {
  if (!NaN(n)) {
    return (n * factorial(n - 1));
  } else {
    return (1);
  }
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
