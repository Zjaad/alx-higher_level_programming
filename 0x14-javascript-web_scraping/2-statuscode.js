#!/usr/bin/node

const request = require('request');

const link = process.argv[2];

request(link, (e, r) => {
	if (e) {
		console.error('error:', e);
	} else {
		console.log(`code: ${r.statusCode}`);
	}
})
