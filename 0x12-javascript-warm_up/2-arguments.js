const arl = process.argv.length;

if (arl === 2) {
	console.log('No argument');
} else if (arl ===3){
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
