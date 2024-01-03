#!/usr/bin/node
import fs from 'fs';
import { argv } from 'process';
fs.readFile(argv[1], 'utf-8', (err, res) => {
  try {
    console.log(res);
  } catch {
    console.log(err);
  }
});
