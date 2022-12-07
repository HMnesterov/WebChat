## Simple web chat on Websockets and Django



## If you want to change  settings, you should edit the env file



Launch
------

```
git clone https://github.com/BenitoSwaggolini/WebChat.git
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cd config
python manage.py migrate
python manage.py runserver
```



Docker
------

```
https://github.com/BenitoSwaggolini/WebChat.git
docker-compose up -d
```




Opportunities:
------


* `chat/<room_name>` - Chat
* `log` - Authorization
* `item` - Registration

