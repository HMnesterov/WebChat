const roomName = JSON.parse(document.getElementById("room-name").textContent);
const username = JSON.parse(document.getElementById("username").textContent);

document.querySelector('#submit').onclick = function (e) {

    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;

    ChatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
    }));

    messageInputDom.value = '';
};

const ChatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

ChatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)

    console.log(data)

    document.querySelector('#chat-messages').value += (data.username + ': ' + data.message + '\n')
}