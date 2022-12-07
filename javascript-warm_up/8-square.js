#!/usr/bin/node
/*
 script that prints a square
 */

const number = parseInt(process.argv[2]);

if (!number) {
  console.log('Missing size');
} else if (number < 0) {
  console.log('');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
