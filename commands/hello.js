const fs = require('fs');

function hello(author) {
    var greetingsDoc = fs.readFileSync("./commands/greetings.txt").toString('utf-8');
    const greetings = greetingsDoc.split(" // ");
    const index = Math.floor(Math.random() * greetings.length);
    const greeting = greetings[index].replace("*", author);
    
    return greeting;
}

module.exports = hello;