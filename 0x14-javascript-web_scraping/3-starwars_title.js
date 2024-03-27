#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(link, (e, r, b) => {
	if (e) {
		console.error('error:', e);
		return;
	}
	const d = JSON.parse(b);
	console.log(d.title);
});
