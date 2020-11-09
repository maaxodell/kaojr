const aboutEmbed = require('./commands/about');
const hello = require('./commands/hello');

const prefix = "!";
const badPerms = "you do not have permission to do that!";

const kao_id = process.env.KAO_ID;

function handleCommand(client, message) {
    // check if command prefix is supplied
    if (!message.content.startsWith(prefix)) return;
    
    // fetch the command and any arguments
    const command = message.content.slice(1);
    const commandElements = command.split(" ");

    // !about - for information on the bot
    if (command == "about") {
        message.react("❤️");
        embed = aboutEmbed();
        message.channel.send(embed);
    }

    // !cleardev - purely for clearing the development text channel (for my use only)
    if (command == "cleardev") {
        if (!message.author.id == kao_id) {
            message.reply(badPerms);
        } else {
            message.channel.messages.fetch().then(messages => { message.channel.bulkDelete(messages) });
        }
    }

    if (command == "hello" || command == "hey") {
        message.react("❤️");
        message.channel.send(hello(message.author.toString()));
    }

}

module.exports = handleCommand;