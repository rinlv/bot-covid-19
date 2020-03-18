# bot-covid-19

Simple BOT using [Bot Framework](https://dev.botframework.com), collect information about COVID-19 (support Vietnamese) 

## Concepts introduced in this sample

```bash
    "commands": [
              {
                "title": "*string*",
                "description": "Hiển thị các tỉnh thành ở Việt Nam ghi nhận ca nhiễm COVID 19"
              },
              {
                "title": "news",
                "description": "Hiển thị tin tức mới nhất về COVID-19"
              },
              {
                "title": "world",
                "description": "Hiển thị số ca nhiễm trên thế giới"
              },
              {
                "title": "all",
                "description": "Hiển thị danh sách các nước ghi nhận ca nhiễm COVID-19"
              },
              {
                "title": "*country*",
                "description": "Hiển thị thông tin ca nhiễm COVID-19 theo tên nước (Eng)"
              }
```

- Run scheduler job to notify if have latest news

## Running the sample
- Clone the repository
```bash
git clone https://github.com/Microsoft/botbuilder-samples.git
```
- Open with visual studio 2019 and activate your desired virtual environment

## Testing the bot using Bot Framework Emulator
[Microsoft Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework emulator from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to bot using Bot Framework Emulator
- Launch Bot Framework Emulator
- File -> Open Bot
- Paste this URL in the emulator window - http://localhost:3978/api/messages

With the Bot Framework Emulator connected to your running bot, the sample will now respond to an HTTP GET that will trigger a proactive message.  The proactive message can be triggered from the command line using `curl` or similar tooling, or can be triggered by opening a browser windows and nagivating to `http://localhost:3978/api/notify`.

### This step is specific to Microsoft Teams

- **Edit** the `manifest.json` contained in the `teams_app_manifest` folder to replace your Microsoft App Id (that was created when you registered your bot earlier) *everywhere* you see the place holder string `<<YOUR-MICROSOFT-APP-ID>>` (depending on the scenario the Microsoft App Id may occur multiple times in the `manifest.json`)
- **Zip** up the contents of the `teams_app_manifest` folder to create a `manifest.zip`
- **Upload** the `manifest.zip` to Teams (in the Apps view click "Upload a custom app")

## Deploy the bot to Heroku

To learn more about deploying a bot to Heroku, see [Deploy your bot to Heroku](https://devcenter.heroku.com/categories/deployment) for a complete list of deployment instructions.

# Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Send proactive messages](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-proactive-message?view=azure-bot-service-4.0&tabs=js)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Timeline COVID-19 (Vietnamese)](https://ncov.moh.gov.vn/dong-thoi-gian)
- [Realtime Monitoring COVID-19 - By Kompa Group](https://corona.kompa.ai/)