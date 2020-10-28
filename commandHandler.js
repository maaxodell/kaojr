const prefix = "!";

//if (message.author.id != client.user.id) message.reply(commandElements);

function handleCommand(client, message) {
    // check if actually a command
    if (!message.content.startsWith(prefix)) return;
        
    const command = message.content.slice(1);
    const commandElements = command.split(" ");

    if (command == "about") {
        message.reply("I was written and developed by kaø and I live here -> `https://github.com/maaxodell/kaojr`")
    }
}

module.exports = handleCommand;