const Discord = require('discord.js');

function Embed() {
    // generate random colour
    var embedColour = [3];
    for (var i = 0; i < 3 ; i++) {
        embedColour[i] = Math.floor(Math.random() * 255);
    }

    const embed = new Discord.MessageEmbed()
        .setAuthor("kaø jr.", "https://cdn.discordapp.com/app-icons/770470835768655894/a2ddb301462fba45072b8edc6f00d323.png")
        .setTitle("Abøut Me")
        .setDescription("I was written and developed by Kaø.")
        .setColor(embedColour)
        .addFields({ name: "There is where I live!", value: "[GitHub](https://github.com/maaxodell/kaojr)" })

    return embed;
}

module.exports = Embed;