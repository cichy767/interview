API - Application Programming Interface

interfejs - rodzaj połączenia umożliwjającego komunikację

REST Representational state transfer - standard określający zasady projektowania API
WEB API opiera się o protokół HTTP
najbardziej popularne akcje to create, read, update, delete ( CRUD )

1. Uniform interface - Jednolity interfejs komunikacyjny
interfejs powinien zapewniać ustandaryzowaną komunikację pomiędzy klientem a serwerem

2. Client-server
wyraźny podział pomiędzy aplikacją działającą po stronie klienta i serwera
Interfejsy API REST wymagają, aby aplikacje klienckie i serwerowe były całkowicie niezależne od siebie.
Klient powinien znać jedynie pełną nazwę zasobu, którego potrzebuje w przestrzeni wirtualnej dozwolonej przez API.
W przeciwnym razie, jedyną wiedzą, jaką klient i serwer dysponują o sobie nawzajem są dane przesyłane przez transakcje API.

3. Stateless
każde zapytanie musi posiadać komplet informacji koniecznych do jego poprawnego zakończenia
serwer nie może przechowywać informacji o stanie klienta

4. Cacheable
api powinno wspierać cachowanie danych w celu zwiększenia wydajności

5. Layered system
system powinien być zaprojektowany w taki sposób aby klient wysyłający zapytanie mógł uzyskać odpowiedź bez konieczności posiadania wiedzy o tym co się dzieje po drugiej stronie
klient może wysłać zapytanie do serwera, a serwer może zrobić coś po swojej stronie np. odpytać się innego api, i klient nie musi o tym wiedzieć

6. Code on demand
przewiduje możliwość wysłania fragmentów kodu (np. Javascript), który może zostać wykonany po stronie klienta


Resource - zasób, będący rzeczownikiem w liczbie mnogiej, unikatowy, posiada adres URI
zasoby są przeststawiane w formacie JSON, YAML, XML


https://restfulapi.net/idempotent-rest-apis/
Idempotency essentially means that the effect of a successfully performed request on a server resource is independent of the number of times it is executed.

For example, in arithmetic, adding zero to a number is an idempotent operation.
POST and PATCH are NOT idempotent.
GET, PUT, DELETE, HEAD, OPTIONS and TRACE are idempotent.


kody odpowiedzi HTTP:
200 (OK) – oznacza, że żądanie zostało pomyślnie przetworzone i serwer zwrócił odpowiedź.
201 (Created) – oznacza, że serwer utworzył nowy zasób i przesłał informacje o tym do przeglądarki.
204 (No Content) – oznacza, że serwer przetworzył żądanie, ale nie zwrócił żadnej zawartości.
301 (Moved Permanently) – oznacza, że żądany zasób został przeniesiony na nowy adres URL i będzie dostępny pod nowym adresem.
302 (Found) – oznacza, że żądany zasób jest tymczasowo dostępny pod innym adresem URL.
307 (Temporary Redirect) – oznacza, że żądany zasób jest tymczasowo dostępny pod innym adresem URL i przeglądarka powinna wysłać nowe żądanie.
400 (Bad Request) – oznacza, że żądanie jest nieprawidłowe lub niekompletne.
401 (Unauthorized) – oznacza, że klient nie ma dostępu do zasobu i musi podać prawidłowe dane uwierzytelniające.
403 (Forbidden) - oznacza, że serwer zrozumiał zapytanie, ale uznał, że dana osoba nie ma dostępu do zasobu
404 (Not Found) – oznacza, że żądany zasób nie został odnaleziony na serwerze.
500 (Internal Server Error) – oznacza, że wystąpił nieoczekiwany błąd po stronie serwera i żądanie nie mogło zostać przetworzone.
502 (Bad Gateway) – oznacza, że serwer, który działa jako pośrednik, otrzymał nieprawidłową odpowiedź od serwera docelowego.
503 (Service Unavailable) – oznacza, że serwer jest chwilowo niedostępny i nie może przetwarzać żądań.

The "401 Unauthorized" status code indicates that the request lacks valid authentication credentials. 
On the other hand, the "403 Forbidden" status code signifies that the server understands the request but refuses to fulfill it.