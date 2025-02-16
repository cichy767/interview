# Ingress Controller w Kubernetes – Co to jest i jak działa?
W Kubernetes, Ingress Controller to komponent, który zarządza ruchem sieciowym kierowanym do usług (ang. Services) działających w klastrze Kubernetes. Jest to zaawansowany sposób na zarządzanie ruchem HTTP/S, oferujący więcej funkcji niż podstawowe Service typu LoadBalancer czy NodePort.

1. Dlaczego potrzebujemy Ingress Controllerów?
Zarządzanie ruchem HTTP/S w Kubernetes: Kubernetes obsługuje ruch sieciowy przy użyciu Service, ale standardowe metody (ClusterIP, NodePort, LoadBalancer) mają ograniczenia:

ClusterIP działa tylko wewnątrz klastra.
NodePort otwiera porty na każdym węźle, ale jest trudny w użyciu w środowiskach produkcyjnych.
LoadBalancer tworzy osobny publiczny adres IP dla każdej usługi, co jest droższe i mniej skalowalne.
Ingress Controller pozwala skonfigurować jeden LoadBalancer dla całego klastra, a następnie zarządzać ruchem na poziomie aplikacji.

2. Jak działa Ingress Controller?
Ingress Controller działa jako reverse proxy, przekierowując ruch HTTP/S do odpowiednich usług w klastrze.

Odbiera ruch z internetu (lub innej sieci).
Na podstawie reguł Ingress kieruje go do odpowiednich usług.
Może obsługiwać funkcje takie jak:
* SSL/TLS (HTTPS)
* Load Balancing (równoważenie ruchu między podami)
* Rewrite URL (zmiana ścieżek URL)
* Rate Limiting (ograniczanie liczby żądań)
* Autoryzacja i uwierzytelnianie


Jak działa Reverse Proxy?
Klient (np. przeglądarka) wysyła żądanie do domeny example.com.
Reverse Proxy (np. Nginx, HAProxy, Traefik) odbiera to żądanie.

Reverse Proxy:
Sprawdza reguły routingu i przekazuje żądanie do właściwego serwera backendowego.
Może modyfikować żądanie (np. zmieniać nagłówki, dodawać SSL).
Może równoważyć ruch między wieloma serwerami backendowymi.
Serwer backendowy przetwarza żądanie i zwraca odpowiedź przez Reverse Proxy.
Reverse Proxy odsyła odpowiedź do klienta.
