#!/usr/bin/node
const myargs = process.argv.slice(2);
if (!process.argv[2]){
	console.log('No argument');
} else{
	console.log(myargs[0]);
}
