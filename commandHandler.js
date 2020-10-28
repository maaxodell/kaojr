const prefix = "!";
const badPerms = "you do not have permission to do that!";

const kao_id = process.env.KAO_ID;

//if (message.author.id != client.user.id) message.reply(commandElements);

function handleCommand(client, message) {
    // check if command prefix is supplied
    if (!message.content.startsWith(prefix)) return;
    
    // fetch the command and any arguments
    const command = message.content.slice(1);
    const commandElements = command.split(" ");

    // !about - for information on the bot
    if (command == "about") {
        message.react("❤️")
        message.reply("I was written and developed by kaø and I live here -> `https://github.com/maaxodell/kaojr`")
    }

    // !cleardev - purely for clearing the development text channel (for my use only)
    if (command == "cleardev") {
        if (!message.author.id == kao_id) {
            message.reply(badPerms);
        } else {
            message.channel.messages.fetch().then(messages => { message.channel.bulkDelete(messages) });
        }
    }
}

module.exports = handleCommand;