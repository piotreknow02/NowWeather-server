# NowWeather Server

Server-side code of NowWeather written in Flask

### Running

To install dependencies type

```bash
pip install -r requirements.txt
```

To run the server type

```bash
python3 Server.py
```

> Note that you should have [python](https://www.python.org/downloads/release/python-379/) installed

You can also run this app on [docker](https://www.docker.com)

To build container type

```bash
docker build -t now-weather .
```

And run the container by typing

```bash
docker run --neame now-weather -p 5000:5000 now-weather
```

Your server is running on [localhost:5000](http://localhost:5000)
