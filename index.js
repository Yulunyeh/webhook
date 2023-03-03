const express = require('express');
const line = require('@line/bot-sdk');

const config = {
    channelAccessToken: 'cjdsY5UFfcFL5iFWtKGBgZA5XuRNimer8zhHqGWGg4pDzzVIBEe+CahXeBYQQm9oN6JoVhgUhw0rxSEgJ4Fz1x9lNBv4cTMrEMfAJtNs4mFXTOlDcFnKNikw4VDDMT0gImC875xyja2RRbCTBropEgdB04t89/1O/w1cDnyilFU=',
    channelSecret: 'ae1838d725d0d9321c4336c7ffda695f'
};

const app = express();

app.post('/webhook', line.middleware(config), (req, res) => {
    Promise
        .all(req.body.events.map(handleEvent))
        .then((result) => res.json(result));
});

const client = new line.Client(config);

function handleEvent(event) {
    if (event.type !== 'message' || event.message.type !== 'text') {
        return Promise.resolve(null);
    }

    return client.replyMessage(event.replyToken, {
        type: 'text',
        text: event.message.text
    });
}

app.listen(3000);
