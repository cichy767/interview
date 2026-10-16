WSGI (Web Server Gateway Interface):

WSGI to standard interfejsu między serwerami webowymi a aplikacjami webowymi napisanymi w Pythonie. Nginx może współpracować z serwerami WSGI, takimi jak Gunicorn lub uWSGI.
Nginx działa jako serwer proxy, który odbiera żądania od klientów i przekazuje je do serwera WSGI, który obsługuje aplikację Pythonową.

* Gunicorn:

Gunicorn (Green Unicorn) to popularny serwer WSGI dla aplikacji Pythonowych.
Konfiguracja: Nginx działa jako reverse proxy, przekazując żądania do Gunicorna, który następnie przetwarza je w aplikacji Pythonowej.

Przykład konfiguracji nginx
```
server {
    listen 80;
    server_name myapp.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Gunicorn uruchamiany jest np. komendą: gunicorn myapp:app.

uWSGI:

uWSGI to inny serwer aplikacyjny zgodny z WSGI, często używany razem z Nginx.
Konfiguracja jest podobna do Gunicorna, gdzie Nginx działa jako proxy, a uWSGI obsługuje aplikację Pythonową.

Przykład konfiguracji nginx
```
server {
    listen 80;
    server_name myapp.com;

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
    }
}
```
Do powyższego `uwsgi_pass` uruchom backend z protokołem uwsgi:

```sh
uwsgi --socket 127.0.0.1:8000 --module myapp:app
```

Jeżeli uruchamiasz backend przez `--http 127.0.0.1:8000`, użyj w Nginx
`proxy_pass http://127.0.0.1:8000;`, tak jak w przykładzie z Gunicornem.
`uwsgi_pass` i `proxy_pass` używają różnych protokołów i nie są zamienne.
WSGI jest interfejsem aplikacji Pythona; uwsgi jest protokołem komunikacji z serwerem uWSGI.

Źródło: [Konfiguracja uWSGI i Nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html).
