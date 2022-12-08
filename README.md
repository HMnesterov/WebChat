# Simple web chat on Websockets and Django


Launch
----------

```bash
git clone https://github.com/BenitoSwaggolini/WebChat.git
cd WebChat
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cd config
python manage.py migrate
```

#### Create file `.env` or delete ```.example``` from ```.env.example```

#### Fill in the data in the file `.env`

### Example:

```dotenv
SECRET_KEY=MySecretKey
DOMAIN=127.0.0.1:8000
```

#### Run
```
python manage.py runserver
```

Docker
------

```bash
https://github.com/BenitoSwaggolini/WebChat.git
cd WebChat
```

```
docker-compose up -d
```

Opportunities:
------

* `chat/<room_name>` - Chat
* `log` - Authorization
* `item` - Registration

