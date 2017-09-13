var shell = require('shelljs');
var path = require('path');

console.log("Installing bower");
shell.exec("bower install");

console.log("Updating pip modules");
shell.exec("pip install -r requirements.txt");
shell.exec("python ./src/manage.py db upgrade");

console.log("Setting up gulp");
gulpfile = path.join('node_modules', 'gulpfile', 'result', 'gulpfile.js');
shell.cp(gulpfile, 'gulpfile.js');
