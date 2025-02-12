# Co się dzieje z requestem, gdy trafia do Django?

## 1. Przychodzący request
Gdy zapytanie HTTP trafia do Django, pierwszym krokiem jest utworzenie obiektu `HttpRequest`, który zawiera wszystkie informacje o żądaniu, takie jak:
- Metoda HTTP (GET, POST, itd.)
- Nagłówki
- Dane formularza
- Ciasteczka
- Ścieżka URL

## 2. Middleware
Request przechodzi przez **łańcuch middleware**. Middleware to funkcje pośredniczące, które mogą modyfikować request, np.:
- `AuthenticationMiddleware` – sprawdza, czy użytkownik jest zalogowany.
- `SessionMiddleware` – zarządza sesjami użytkownika.
- `CommonMiddleware` – dodaje standardowe funkcjonalności, np. obsługę przekierowań.

Middleware są przetwarzane **w kolejności zdefiniowanej w `MIDDLEWARE` w `settings.py`**.
Po przejściu przez middleware request kierowany jest do systemu routingu.

## 3. Routing i Widoki
Django porównuje URL requesta z wzorcami (`urlpatterns`) w `urls.py` i jeśli znajdzie dopasowanie:
- Wywoływana jest funkcja widoku (**FBV - Function Based View**) lub metoda klasy (**CBV - Class Based View**).
- Jeśli widok wymaga danych z bazy, wykonuje zapytania przez **Django ORM**.

## 4. Serializery (jeśli używamy DRF)
Jeśli używamy **Django REST Framework (DRF)**, widok może przetworzyć request przez **serializer** (np. `serializers.ModelSerializer`).
- **Serializer** sprawdza poprawność danych wejściowych oraz konwertuje dane na format JSON.

## 5. Przetwarzanie Modeli (ORM)
Jeśli widok komunikuje się z bazą danych, zapytania są wykonywane poprzez **Django ORM**.
- Django obsługuje zapytania, pobiera lub zapisuje dane i zwraca je do widoku.

## 6. Odpowiedź i powrót przez Middleware
- Po przetworzeniu żądania widok zwraca odpowiedź (`HttpResponse` lub `JsonResponse`).
- Odpowiedź przechodzi przez **middleware w odwrotnej kolejności** (od ostatniego do pierwszego).
- Middleware mogą modyfikować odpowiedź, np. dodając nagłówki lub kompresując dane.

## 7. Wysłanie odpowiedzi do klienta
Po przejściu przez middleware, odpowiedź jest zwracana do serwera HTTP, który przesyła ją do użytkownika.
