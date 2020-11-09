// config
require('dotenv').config();
const Discord = require('discord.js');
const client = new Discord.Client();
const handleCommand = require('./commandHandler');

// connected and ready
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
    client.user.setActivity("!about");
});

// handle command
client.on('message', message => {
    handleCommand(client, message);
    
});

// login to discord application
client.login(`${process.env.TOKEN}`);