#!/usr/bin/node
function add(a, b) {
	const r = a + b;
	console.log(r);
}
add(Number(process.argv[2]), Number(process.argv[3]));
