#!/usr/bin/node
/*
 script that prints My number: <first argument converted in integer>
 */

const number = parseInt(process.argv[2]);

if (!number) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
