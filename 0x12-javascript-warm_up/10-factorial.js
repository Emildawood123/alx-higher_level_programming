#!/usr/bin/node
const arg = process.argv[2];
if (arg == undefined) {
  console.log(1);
  return;
}
const newArg = parseInt(arg);
function factorial(num) {
  if (num == 1){
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(newArg));
