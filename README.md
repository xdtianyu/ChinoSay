# ChinoSay bot

## config

Move `config.py.example` to `config.py`, and modify `base_url` and `token`.
 
## Run

Clone the code first:

```shell
cd /opt
git clone https://github.com/xdtianyu/chinosay
cd chinosay
```

Run

```shell
virtualenv -p python3 venv
pip install -r requirements.txt
python bot.py
```

## Systemd

```shell
chown -R nobody:nogroup /opt/chinosay
cp /opt/chinosay/chinosay.service /etc/systemd/system
systemctl enable chinosay
systemctl start chinosay
```

## nginx config to expose `https://bot.example.org/data`

```shell
    location /data {
        allow all;
        alias /opt/chinosay/data;
    }
```