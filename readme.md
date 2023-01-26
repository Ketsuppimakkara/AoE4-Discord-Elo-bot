AOE4 Elo bot gets the ranked 1v1 matchmaking ELO of the wanted player from aoe4world.com/dumps when mentioned on the server.

Installation:
1. Enable developer mode on your profile-> advanced settings
2. Create a new application on https://discord.com/developers/applications
3. Rename .env.example to .env, and replace 'YOUR_DISCORD_BOT_TOKEN' with your bot's token in the .env file.
4. Back in the discord application website, go to OAuth2 -> URL generator.
5. Check the 'Bot' Scope and give the bot permissions. It needs at least  'Read Messages/View Channels' and 'Send Messages' permissions.
6. Use the generated URL to add the bot to your server.

Usage:
1. Run the bot.pyw file to activate the bot. You may want to run the bot.pyw file on startup so you don't need to restart the bot whenever your computer shuts down
2. Mention the bot in a message containing the user you want to search for. Note that the search is case sensitive and only considers exact matches.

![alt text](https://github.com/ketsuppimakkara/AoE4-Discord-elo-bot/blob/main/example.png?raw=true)

Note that the bot is running locally on your computer. If you shut down your computer, the bot will stop working. You can see that the bot user goes offline in that case.

