# Q2: platforma danych AWS

Jak rozumieć pytanie, porównywać scenariusze i prowadzić dopytania

**Data Platform Engineer / AWS DevOps · przewodnik po polsku · aktualizacja 18 października 2026**

Materiał dla prowadzącego bez doświadczenia DevOps. Wyjaśnia od podstaw drogę
pliku do danych dostępnych analitykowi, możliwe odpowiedzi kandydata, dostęp
między kontami oraz koszt. Pytania do kandydata są po angielsku.

Przykłady, wolumeny i czasy są dydaktyczne, a nie opisem infrastruktury Capgemini
lub osiągnięć kandydata. W Q2 masz 10 minut: około 6 na platformę, 3 na dostęp
i 1 na koszt. Wybierz dopytania; nie odczytuj całego przewodnika podczas rozmowy.

**Oceniaj związek między wymaganiem, rozwiązaniem i sprawdzeniem wyniku.**
Istnieje więcej niż jedna poprawna architektura. Kandydat nie musi wymienić
każdej usługi ani budować złożonej platformy, jeśli prostsza spełnia wymagania.

## 1. Pytanie główne i trzy rzeczy, które oceniasz

> “A supplier delivers CSV and JSON files to S3. Data engineers need to process
> them, and analysts need to query the prepared data. We have separate dev,
> test, and production environments. New data must be ready for consumption
> within 15 minutes of arrival. How would you provision and operate this AWS
> platform? Start by asking about missing requirements, then sketch the flow.”

Po polsku: dostawca przysyła pliki, zespół je przetwarza, analityk potrzebuje
wyniku. Kandydat ma wyjaśnić przygotowanie i utrzymanie platformy, która
udostępni dane w ciągu 15 minut, z oddzielnymi środowiskami.

Pytanie obejmuje: **spójny przepływ**, **kontrolowany dostęp** i **uzasadniony koszt**.
Nie prosisz o napisanie transformacji Spark ani kodu wszystkich komponentów.
W tej roli ważne jest też, jak data engineer dostanie gotowy, powtarzalny
sposób wdrażania i utrzymania swojego zadania.

| Część Q2 | Czego słuchasz |
| --- | --- |
| Platforma | Jak plik staje się sprawdzonym wynikiem i skąd wiemy, że jest gotowy |
| Bezpieczeństwo | Kto wykonuje operację, do jakich danych i klucza ma dostęp |
| Koszt | Co kosztuje w wybranym projekcie i jak sprawdzono kompromis z czasem |

To pytanie projektowe: kandydat opisuje, co by zrobił. Własne wdrożenie potwierdzaj
później konkretnym przykładem; spójna propozycja nie jest jeszcze dowodem
doświadczenia produkcyjnego.

## 2. Q2: karta założeń i odpowiedzi po angielsku

**Szybkie odwołanie podczas rozmowy:** kandydat pyta o obszar, Ty odczytujesz
odpowiedni wiersz. To jeden stały profil ćwiczenia. Najpierw pozwól mu zapytać;
jeśli nie pyta, podaj rozmiar, tempo i transformacje przed oceną wyboru usług.

| Topic / temat | Answer to give the candidate / odpowiedź po angielsku |
| --- | --- |
| File size | 1-50 MB per uncompressed file; average about 10 MB. |
| Arrival rate | About 10,000 files per day in production; peaks of up to 1,000 files over five minutes, included in that daily total. |
| Formats | UTF-8 CSV with a header, or newline-delimited JSON. |
| Transformations | Schema, type and required-field checks, light mappings and filtering. Files are independent; no large joins or external API calls. |
| Consumers | Analysts run SQL over prepared datasets; assume up to ten concurrent queries. |
| Latency | Valid new deliveries must be queryable within 15 minutes of a completed S3 upload, including at the stated peak. BI refresh is outside this target. |
| Environments | Separate dev, test and production accounts, deployed from the same IaC pattern. Only production has full traffic; dev/test use synthetic samples. |
| Security | KMS encryption at rest, TLS in transit, and least-privilege IAM roles. The security follow-up adds an analyst in a separate account. |
| Failures | Reject and record the whole invalid file; never publish part of it. Keep raw data, alert and support controlled replay. Flag invalid files within 15 minutes. |
| Duplicates | The supplier provides a stable delivery_id in object metadata. Resends keep that ID, even under another file name, and must not duplicate the output. |

Nie odczytuj całej tabeli jako dodatkowych pytań. Kilka trafnych pytań kandydata
i jasne założenia wystarczą. Ten profil obowiązuje przy porównywaniu każdej
proponowanej architektury.

### Czy te wymagania są dobre dla Regular/Mid?

Tak. Łączą niewielkie pojedyncze pliki z realną skalą dobową, prostym kodem,
operacjami i bezpieczeństwem. Pozwalają ocenić projekt bez wymagania Sparka
lub rozbudowanej architektury. Nie są dowodem, że dowolna konfiguracja usługi
spełni cel. Kandydat powinien zaproponować pomiar i kontrolę obciążenia.

| Doprecyzowanie względem początkowej propozycji | Dlaczego jest potrzebne |
| --- | --- |
| Średnia 10 MB, pliki bez kompresji | Sam zakres 1-50 MB nie określa typowego wolumenu ani narzutu rozpakowania |
| Szczyt 1000 plików w pięć minut | „Okresowe skoki” nie pozwalają uczciwie ocenić bufora i przepustowości |
| Gotowość w SQL, z wyłączeniem odświeżania BI | Wspólny początek i koniec pomiaru |
| Odrzucenie całego błędnego pliku | Kandydat nie musi zgadywać, czy wolno opublikować część rekordów |
| Stały delivery_id | Rozróżnienie nowej dostawy i ponowienia pod inną nazwą |
| Pełny ruch tylko w produkcji | Dev i test mają działać, ale nie muszą stale kopiować produkcyjnego wolumenu |

Przy średniej 10 MB: 10 000 plików to około **100 GB wejścia dziennie**.
Gdyby każdy miał 50 MB, byłoby 500 GB. Szczyt 1000 plików w pięć minut
oznacza średnio 200 plików/min w tym oknie, około 3,3/s. Liczba 1000 jest
częścią dziennych 10 000, nie dodatkowym stałym napływem. Nie zakładaj idealnie
równomiernych sekund; projekt powinien tolerować grupowanie dostaw.

To wartości ćwiczenia, nie gwarancje wydajności i nie potwierdzone parametry
pracodawcy. Nie wymagaj wyliczenia dokładnej liczby workerów bez zmierzenia
czasu i pamięci. Rozmiar 50 MB nie oznacza, że plik ma zostać wysłany w całości
jako payload zdarzenia: proces może odczytać go z S3.

### Dodatkowe pytania kandydata: gotowe odpowiedzi

**Retention / region:**

> “Keep raw files for 30 days and prepared data for 90 days. Use one AWS Region;
> cross-Region disaster recovery is outside this exercise.”

Raw 30 dni przy średniej daje około 3 TB samego wejścia, przed dodatkowymi
wersjami i narzutem. Wolumen curated zależy od filtracji i formatu, więc nie
wyliczaj go automatycznie jako tej samej liczby bajtów.

**What exactly means ready?**

> “A small authorised SQL check must be able to read the validated published
> result within 15 minutes of the completed upload. Include event delivery,
> queueing, processing, validation, publication and catalogue readiness.
> Dashboard refresh and a response-time guarantee for every analytical query
> are outside this target.”

Liczymy nową dostawę od jej pierwszego zakończonego zapisu do S3; ponowienie
nie resetuje zegara. Błędnego pliku nie da się obiecać naprawić w 15 minut bez
poprawnych danych. W tym czasie musi zostać rozpoznany i jawnie oznaczony;
przywrócenie po poprawie jest osobną kontrolowaną operacją.

**What is a duplicate?**

> “The same delivery_id means the same delivered content, including a resend
> under another object name. The supplier provides that ID in object metadata.
> A corrected invalid file gets a new delivery_id linked to the rejected
> delivery. Corrections to already published business data are outside the baseline.”

To założony kontrakt dostawcy, nie funkcja automatycznie nadawana przez S3.
Metadane użytkownika mogą przechowywać taki identyfikator.
[AWS: metadane obiektu](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html).
Replay tego samego wejścia po naprawie kodu trzeba odróżnić od przypadkowego
duplikatu i bezpiecznie zastąpić jego wynik, zamiast dopisać drugi.

**Schema / filtering:**

> “Required fields and types are agreed. Optional additions may be accepted
> under a documented policy. A missing required field or invalid type rejects
> the whole file. Filtering valid records by an agreed business rule is allowed.”

JSON po jednym rekordzie w wierszu ułatwia określenie sposobu odczytu, zamiast
zgadywania, czy cały plik jest jednym wielkim obiektem. Poprawny plik może po
filtrowaniu dać zero rekordów: nadal trzeba zapisać jego prawidłowy status.

**Existing stack / scaling:**

> “No processing engine is mandated. Propose an AWS design and explain how
> you would test representative 50 MB inputs and the stated arrival peak.”

Nie wprowadzaj bez zapowiedzi plików po kilka GB, dużych złączeń ani wyższych
szczytów, aby podważyć poprawną odpowiedź. Taką zmianę można omówić wyłącznie
jako jawne dodatkowe ćwiczenie, jeśli zostało na to miejsce.

## 3. Jeden plik od dostawcy do analityka: krok po kroku

Załóżmy, że plik zawiera 100 zamówień i został poprawnie zapisany w S3 o 10:00.
Cel 15 minut liczymy od tego momentu do możliwości odczytu sprawdzonego
wyniku jako analityk, zgodnie z kartą w rozdziale 2. Odświeżenie dashboardu
BI jest poza tym celem; sam zapis pliku wynikowego nie wystarcza.

```text
Dostawca -> S3 raw -> wyzwalanie / opcjonalna kolejka
         -> kod przetwarzania -> kontrola jakości
         -> S3 curated -> opis danych w katalogu -> zapytanie analityka
```

| Krok | Co rzeczywiście się dzieje | Czego sam krok nie dowodzi |
| --- | --- | --- |
| 1. Zapis do raw | Zachowujemy oryginalny plik i jego identyfikację | Że ktoś rozpoczął przetwarzanie |
| 2. Wyzwolenie | Zdarzenie lub harmonogram uruchamia ścieżkę pracy | Że zadanie skończyło się sukcesem |
| 3. Przetwarzanie | Kod czyta dane, sprawdza i przekształca rekordy | Że wynik nadaje się do publikacji |
| 4. Walidacja | Porównujemy wynik z uzgodnionymi regułami | Że docelowy odbiorca ma dostęp |
| 5. Publikacja | Udostępniamy uzgodniony, spójny zestaw wyników | Że każda aplikacja czyta właściwą wersję |
| 6. Odczyt | Analityk wykonuje zapytanie i widzi nowe dane | Że następne uruchomienia też zmieszczą się w czasie |

Przykładowy pomiar: 1 minuta na oczekiwanie, 4 na przetwarzanie i 1 na kontrolę
oraz publikację. Razem 6 minut. To ilustracja pomiaru, nie obietnica wydajności AWS.
W teście uwzględniaj także gorsze obciążenie i uzgodniony zapas na błędy.

### Co robią usługi, a co musi zapewnić kod

S3 przechowuje obiekty, Lambda lub Glue może wykonać kod, katalog opisuje dane,
a Athena uruchamia SQL. Sam wybór usług nie tworzy reguł jakości ani poprawnej
logiki biznesowej. Ktoś musi ją zaimplementować, wdrożyć i sprawdzić.

> “What observation would prove that this input is ready for the analyst?”

### Jak operator zauważy problem

Potrzebne są informacje o wejściu, uruchomieniu, błędzie i publikacji, najlepiej
powiązane identyfikatorem dostawy. Logi opisują zdarzenia, metryki pokazują
wartości w czasie, a alarmy uruchamiają reakcję. CloudWatch jest jedną z usług
AWS do takich sygnałów. Monitoring powinien mierzyć też świeżość i kompletność,
nie tylko brak błędów programu. Alarm potrzebuje właściciela i instrukcji reakcji.

Jeśli kandydat proponuje DLQ, chodzi o wydzielenie wiadomości nieskutecznie
obsłużonych według konfiguracji, a nie automatyczną naprawę danych. Szczegółową
obsługę paczek i odzyskiwanie pracy można pogłębić w Q6.

## 4. S3 raw, curated i bezpieczna publikacja

Raw to zachowane wejście; curated to przygotowany wynik. To warstwy logiczne,
które mogą używać osobnych bucketów lub odpowiednio oddzielonych lokalizacji.
Nazwanie dwóch prefixów nie tworzy jeszcze izolacji uprawnień.

### Przykład odtworzenia

W poniedziałek zapisano plik 100 zamówień. We wtorek odkryto błąd przeliczenia kwot.
Jeśli zachowano oryginalne wejście i wersję kodu, można ponownie wyliczyć wynik.
Jeśli nadpisano jedyną kopię wejścia, ustalenie prawidłowego wyniku jest trudniejsze.

Trzeba ustalić, czy dostawca nadpisuje obiekt pod tą samą nazwą, czy tworzy nowy.
Wersjonowanie S3 może pomóc rozróżnić wersje; alternatywą jest uzgodniony sposób
niezmiennego zapisywania kolejnych dostaw. Retencja oznacza czas zachowania danych.
[AWS: obiekty i wersjonowanie S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

### Dlaczego wynik nie powinien być widoczny w połowie

Załóżmy, że wynik składa się z dziesięciu plików. Po zapisaniu trzech analityk
może zobaczyć niepełny zestaw, jeśli czyta wprost każdą nową zawartość lokalizacji.
Potrzebny jest uzgodniony sposób publikacji kompletnego wyniku, np. odrębna
wersja wyjścia i kontrolowane wskazanie, którą wersję wolno czytać.

Nie zakładaj, że zwykły zapis wielu obiektów S3 daje jedną transakcję obejmującą
cały zbiór. To kwestia procesu publikacji lub wybranego formatu tabelowego.
Nie trzeba projektować pełnego protokołu na rozmowie; kandydat powinien
rozumieć różnicę między częściowym zapisem a gotowym zestawem.

**Dopytaj przy:** „Wyślę wynik do curated i gotowe”. Zapytaj, czy odbiorca może
zobaczyć niekompletny zestaw i jak potwierdzono publikację.

> “How would you prevent consumers from seeing a partially written result?”

## 5. Scenariusz A: „użyłbym Lambdy i kolejki SQS”

### Jak działa taki wariant

1. Dostawca zapisuje plik w raw.
2. Skonfigurowane powiadomienie S3 wysyła informację o obiekcie do kolejki.
3. Integracja SQS–Lambda pobiera wiadomości i uruchamia funkcję.
4. Kod odczytuje właściwy plik z S3, waliduje/przetwarza go i zapisuje wynik.
5. Proces rejestruje rezultat i publikuje dane zgodnie z ustaloną regułą.

Wiadomość zwykle wskazuje plik; nie oznacza przesłania całej jego zawartości
w powiadomieniu. Samo połączenie usług nie implementuje transformacji.

S3 wymaga konfiguracji powiadomień i ich celu. Powiadomienia mogą być dostarczane
więcej niż raz. Przy zapisie wyników do tego samego miejsca wyzwalającego
trzeba też uważać na ponowne uruchamianie przez własne wyjście.
[AWS: powiadomienia S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html).

### Po co kolejka, jeśli można uruchomić funkcję zdarzeniem

SQS może buforować napływ pracy i oddzielać go od tempa przetwarzania.
Integracja z Lambdą pobiera wiadomości, także w paczkach. Ponowienia i duplikaty
są częścią projektu, a nie dowodem jednorazowego dostarczenia.
[AWS: Lambda i SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

Kolejka nie jest obowiązkowa w każdej małej architekturze. Kandydat może wybrać
bezpośrednie zdarzenie S3–Lambda i uzasadnić obsługę błędów, tempa i odzyskiwania.

> “What does the queue add in your design?”

> “What does the Lambda function actually do with the file?”

### Co oznacza sensowny wybór Lambdy

Kandydat wiąże ją z ograniczoną operacją, pasującym czasem, pamięcią i obciążeniem.
Sprawdza zależności, limity wykonania i zachowanie przy szczycie. Nie wystarczy
„Lambda jest serverless”, bo serverless nie oznacza braku limitów i kosztu.
[AWS: ograniczenia Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).

**Mocne dopytanie:** “What would make you choose a different processing engine?”

Jeśli Lambda tylko uruchamia Glue, to Glue wykonuje przetwarzanie. Poproś
o rozdzielenie tych dwóch ról; nie traktuj listy usług jako przepływu.

## 6. Scenariusz B: „użyłbym Glue i Atheny”

### Trzy różne elementy, których nie należy łączyć w jedno

| Element | Proste objaśnienie |
| --- | --- |
| Glue job | Zadanie wykonujące kod przetwarzania danych |
| Glue Data Catalog | Opis tabel, kolumn i lokalizacji danych; nie magazyn wszystkich wierszy |
| Athena | Silnik wykonujący zapytania SQL nad obsługiwanymi danymi |

Glue oferuje przetwarzanie i katalog, lecz samo utworzenie tabeli katalogowej
nie uruchamia transformacji. Crawler może rozpoznać strukturę i uzupełnić katalog;
nie jest automatycznie kompletną walidacją jakości biznesowej.
[AWS: komponenty Glue](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html).

### Przykład krok po kroku

Dostawca zapisuje CSV z zamówieniami i JSON z danymi referencyjnymi.
Skonfigurowany mechanizm uruchamia zadanie Glue. Kod czyta uzgodnione wejścia,
waliduje i lekko przekształca dane, a potem zapisuje wynik do curated. Duże
złączenia nie są wymaganiem bazowym. Kontrola jakości
potwierdza wymagane pola i zakres. Opis tabeli wskazuje właściwy wynik.
Analityk przez Athenę pyta SQL o przygotowane dane w S3.

To przykład, nie obowiązkowy stos. Athena pozwala wykonywać SQL nad danymi
w S3 przy odpowiedniej konfiguracji i opisaniu danych.
[AWS: czym jest Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

> “Which component performs the transformation, which stores the data, and which describes the table?”

> “How is the job triggered, and what tells you it completed successfully?”

### Czego oczekiwać od wyboru Glue

Większy silnik może być uzasadniony obliczeniami, złączeniami i potrzebną
równoległością. Nie akceptuj automatycznej gwarancji „Glue zawsze zmieści się
w 15 minutach”. Trzeba zmierzyć oczekiwanie, start, wykonanie i publikację
dla odpowiedniego obciążenia. Nie wymagaj limitów ani cen z pamięci.

Jeśli kandydat mówi „crawler zadba o schemat”, dopytaj, co stanie się
po zmianie typu kolumny i kto zdecyduje o zgodności z odbiorcami.
Automatyczne wykrycie struktury nie jest tą samą decyzją co bezpieczna publikacja.

## 7. Scenariusz C: harmonogram, zależności i Step Functions

### „Uruchamiałbym zadanie co 15 minut”

Harmonogram może być dobrym wyborem, ale sam interwał nie dowodzi spełnienia celu.
Plik przychodzi o 10:00:01, a następny start jest o 10:15. Jeśli przetwarzanie
i publikacja trwają kolejne 5 minut, wynik będzie gotowy około 10:20.
Cel 15 minut od przyjścia nie został spełniony.

> “What is the worst-case waiting time before processing starts?”

Kandydat może wybrać krótszy interwał, wyzwalanie zdarzeniem lub inny sposób
grupowania wejść. Ważny jest łączny czas i sposób pracy podczas zaległości,
a nie sam wybór harmonogramu.

### Co robi orkiestrator

Orkiestracja koordynuje kroki: uruchom zadanie, czekaj na właściwy wynik,
sprawdź dane, opublikuj lub zgłoś błąd. Step Functions jest jednym z narzędzi.
Może m.in. uruchomić Glue z integracją oczekującą na zakończenie zadania.
Nie wykonuje przez to automatycznie transformacji wewnątrz Glue.
[AWS: Glue z Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html).

> “Does the next step wait for completion, or only for successful submission?”

Identyfikator uruchomienia zwykle potwierdza rozpoczęcie/przyjęcie, a nie
gotowość danych. Kandydat powinien nazwać warunek przejścia do następnego kroku.
Może też wykorzystać istniejący orkiestrator zespołu; Step Functions nie jest
obowiązkową odpowiedzią.

W bazowym profilu pliki są niezależne. Gdyby w jawnym rozszerzeniu wynik
wymagał dwóch plików, nadejście pierwszego nie oznaczałoby kompletnego wejścia.
Byłaby wtedy potrzebna osobna reguła gotowości całej dostawy.

## 8. Scenariusze D–F: minimalny projekt, istniejąca platforma i replikacja

### D. „Wystarczy S3, katalog i Athena”

To może być sensowne, jeśli pliki już spełniają potrzeby odbiorcy i nie wymagają
osobnego ciężkiego przetwarzania. Nie wymagaj Glue job tylko dlatego, że występuje
w przykładzie architektury. Athena potrafi też wykonywać transformacje SQL;
jeśli to proponuje, niech opisze konkretną operację i publikację wyniku.

> “What preparation or validation is required, and where does it happen?”

Brak osobnego silnika obliczeniowego nie zwalnia z odpowiedzi o błędnych danych,
schemacie, dostępie i świeżości. „Tylko wskażemy folder” może być niepełne,
jeśli wymagane są sprawdzone i przygotowane dane.

### E. „Wykorzystałbym istniejącą platformę lub silnik”

Kandydat może zaproponować działające już środowisko Spark, Databricks,
kontenery lub platformę zapytań. Nie oceniaj negatywnie samej innej nazwy.
Poproś o źródło, kod, wyzwalanie, wynik, role i sposób wdrażania w AWS.

> “Which existing capability would you reuse, and what would you provision yourself?”

Jeśli nie znasz narzędzia, sprawdź rozumowanie i zapisz szczegóły do konsultacji.
Nie zakładaj równoważności funkcji bez wyjaśnienia, ale nie odrzucaj rozwiązania
za brak użycia konkretnej usługi z przewodnika.

### F. „Zrobiłbym replikację S3 do curated”

W Q1 replikacja mogła być właściwym mechanizmem migracji. W Q2 potrzebujesz
również wyjaśnienia przygotowania i sprawdzenia danych. Samo kopiowanie pliku
nie zmienia jego pól i nie weryfikuje reguł biznesowych.

> “What prepares and validates the data before the analyst uses it?”

Replikacja może być częścią większej ścieżki. W ustalonym profilu Q2 wymagane
są jednak walidacja i lekkie transformacje przed publikacją. Samo kopiowanie
nie spełnia całego zadania, nawet gdy przykładowy plik wygląda na poprawny.

## 9. Duplikaty i zmiana schematu: przykłady dla prowadzącego

### Ten sam plik dostarczono dwa razy

Plik zawiera zamówienie o wartości 100. Dwukrotne bezwarunkowe dopisanie podnosi
sumę do 200, choć nie było nowej sprzedaży. Idempotencja oznacza, że powtórzenie
tej samej operacji nie daje dodatkowego niezamierzonego skutku.

W tym ćwiczeniu mamy stabilny `delivery_id` od dostawcy. Bucket, nazwa i wersja
pomagają odnaleźć fizyczny obiekt, ale sam klucz obiektu nie rozpozna ponownej
dostawy pod nową nazwą. Kandydat powinien użyć uzgodnionej tożsamości wejścia
i zapobiec podwójnemu skutkowi. Powtórzenie zdarzenia S3 może wystąpić niezależnie
od powtórnego wysłania pliku przez dostawcę.

> “What identifies the same input, and what prevents a second business effect?”

Trwały stan operacji lub odpowiedni sposób zapisu może pomagać w bezpiecznym
ponowieniu. Zbiór w pamięci jednej Lambdy nie chroni wszystkich wykonań
i restartów. Pełny protokół współbieżności jest dodatkową głębią na tym etapie.

### Sto rekordów, z czego dwa są błędne

Polityka ćwiczenia jest już ustalona: odrzucamy cały błędny plik. Nie publikujemy
98 rekordów jako gotowego wyniku. Zachowujemy raw, zapisujemy powód i status,
alarmujemy i umożliwiamy kontrolowane wznowienie. „Kwarantanna” oznacza taki
wydzielony stan/lokalizację do wyjaśnienia; nie musi wymagać przeniesienia
fizycznego obiektu do kolejnego bucketa.

### Zmiana schematu

Schemat opisuje pola i typy. Dodanie opcjonalnego pola może być zgodne,
jeśli taka jest uzgodniona polityka. Brak wymaganego `order_id` lub tekst
w kolumnie wymagającej liczby może blokować przetwarzanie.

> “Which schema changes can you accept, and which would stop publication?”

Nie wymagaj jednego uniwersalnego mechanizmu. Oczekuj reguł, świadomej reakcji
i testu. „Zawsze włączymy automatyczne aktualizowanie schematu” wymaga wyjaśnienia
wpływu na odbiorców.

## 10. Backfill jednego dnia: jak uniknąć podwójnych danych

Backfill to ponowne przeliczenie lub uzupełnienie historycznego zakresu.
Replay oznacza odtworzenie wskazanych wejść/zdarzeń. Oba wymagają uzgodnienia,
co ma stać się z dotychczasowym wynikiem.

### Konkretny przykład

Wtorek zawiera 100 zamówień o sumie 1000. Po poprawce kodu prawidłowa suma
tych samych zamówień to 1200. Jeśli dopiszemy nowy wynik do starego, raport
może pokazać 200 rekordów i sumę 2200. Nie powstało przecież 100 nowych zamówień.

Rozwiązaniem może być kontrolowane zastąpienie wyniku za wtorek albo aktualizacja
po uzgodnionych kluczach. Wybór zależy od formatu danych i sposobu zapisu.
Sama nazwa trybu overwrite lub merge nie wystarcza bez wskazania zakresu.

> “Which data would you replace or merge, and how would you verify only that scope changed?”

Warto znać dokładne wejścia, wersję kodu i identyfikator uruchomienia. Jeśli
bieżące przetwarzanie przyjmuje spóźnione wtorkowe zamówienie, trzeba też
zapobiec konfliktowi z backfillem. Nie wymagaj pełnej implementacji blokad,
ale oczekuj świadomości tego ryzyka.

### Gdy kandydat mówi „Glue bookmarks załatwią powtórzenia”

Job bookmarks pomagają śledzić przetworzone wejście w obsługiwanych źródłach.
Nie rozwiązują automatycznie całej semantyki wyniku. Po cofnięciu lub wyzerowaniu
bookmarka Glue nie usuwa za Ciebie wcześniejszych plików docelowych.
[AWS: Glue job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html).

> “What happens to the existing output when you reprocess that input?”

To pytanie sprawdza rozumienie, nie pamięć konfiguracji. Kandydat może zaproponować
inne rozwiązanie, jeśli wyjaśni bezpieczny wynik i jego sprawdzenie.

## 11. Dev, test, prod i gotowy moduł dla data engineera

### Co znaczy oddzielne środowisko

Dev służy tworzeniu, test sprawdzaniu, a prod rzeczywistym odbiorcom.
Zmiana testowa nie powinna przypadkiem nadpisywać produkcyjnych danych lub
uzyskiwać nieograniczonego dostępu do nich. W karcie przyjmujemy oddzielne konta
AWS dla dev, test i prod oraz wspólny wzorzec IaC. Pełny wolumen dotyczy produkcji;
dev i test używają danych syntetycznych, a test szczytu jest zaplanowany osobno.

Nazwy `dev` i `prod` same nie blokują pomyłki. Pytaj o role, lokalizacje,
konfigurację, stany IaC i ścieżkę wdrożenia. Szczegóły stanu Terraform omawiasz w Q3.

> “What stops a test deployment from changing production data?”

### Co powinien dostać data engineer

Przykładowy moduł przyjmuje wersję kodu, środowisko, dozwolone wejścia i wyjścia,
parametry wykonania oraz reguły monitoringu. Zapewnia powtarzalne tworzenie
potrzebnych ról, zadania, wyzwalania, logów i alarmów. Dokumentacja pokazuje,
jak wdrożyć, sprawdzić, znaleźć błąd i odtworzyć dane.

To przykład wspólnej możliwości platformy, nie wymóg określonego modułu.
Każde zadanie nie powinno automatycznie otrzymywać roli administratora.

> “What can the data engineer configure, and which safeguards are built into the template?”

**Dobry kierunek:** kandydat odróżnia zasoby, które wdroży w IaC, artefakt
z kodem transformacji, konfigurację środowiska i kontrolę działania po wdrożeniu.
W Q2 wystarczy spójny opis. Proces PR, plan i promocję pogłębiasz w Q3–Q4.

## 12. Bezpieczeństwo: analityk z innego konta i KMS

> “The processing job runs in the platform account, while the analyst uses
> another AWS account. The data is encrypted with a KMS key. How would you
> restrict the analyst to an approved dataset, and how would you investigate
> AccessDenied when they try to read it?”

Uwierzytelnienie ustala tożsamość, autoryzacja pozwala na konkretną operację.
Principal to tożsamość wykonująca żądanie. Rola procesora i rola analityka
mają różne zadania; nie muszą otrzymywać tego samego dostępu.

### Dwa możliwe wzorce

**Dostęp bezpośredni:** rola z konta analityka czyta zatwierdzony zasób platformy.
Trzeba ocenić właściwe uprawnienia tożsamości i polityki zasobów dla dostępu
między kontami, a przy szyfrowaniu także KMS.

**Przejęcie roli:** analityk z konta B przejmuje uzgodnioną rolę w koncie A.
Trust policy określa, kto może to zrobić; polityki uprawnień roli określają,
co uzyskana sesja może wykonać. Dostęp do danych oceniamy dla tej sesji.
[AWS: role między kontami](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html).

> “Does the analyst access the data directly, or assume a role in the platform account?”

### Przykład najmniejszych potrzebnych uprawnień

Analityk może czytać zatwierdzony zbiór zamówień w curated, ale nie modyfikować
raw ani odczytywać danych innego zespołu. Należy ustalić potrzebne operacje,
lokalizacje i sposób korzystania z danych. Prawo listowania bucketa i odczytu
obiektu to różne operacje; nie trzeba znać pełnej polityki z pamięci.

KMS zarządza użyciem kluczy kryptograficznych. Prawo pobrania obiektu S3
może nie wystarczyć do odszyfrowania jego treści. Przy bezpośrednim użyciu
klucza KMS z innego konta potrzebne jest współdziałanie polityki klucza
i uprawnień IAM wywołującego. Przy przejęciu roli zmienia się tożsamość do oceny.
[AWS: KMS między kontami](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html).

Jeśli rozwiązanie używa Atheny lub Lake Formation, uwzględnij też ich rzeczywisty
model dostępu. Samo pozwolenie na użycie usługi zapytań nie oznacza dostępu
do każdego źródła, katalogu i miejsca zapisu wyników. Lake Formation może dodawać
zarządzanie uprawnieniami do danych; nie jest obowiązkowym elementem tej odpowiedzi.
[AWS: rola Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html).

## 13. AccessDenied: trzy scenariusze i sposób dopytywania

Najpierw ustal: **kto, jaką operację, na jakim zasobie i w jakim kontekście**.
Nie wystarczy „sprawdzę IAM”. Jawna odmowa w mającej zastosowanie polityce
może blokować operację mimo Allow w innej. Dodatkowe granice mogą wynikać
m.in. z polityk organizacji, sesji lub endpointu.
[AWS: ocena polityk](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

### A. Rola nie odczytuje obiektu

> “Which role is making the request, and is the denied operation listing or reading?”

Szukaj ustalenia konkretnej tożsamości, operacji i zasobu oraz odpowiednich
polityk. Błąd w nazwie lub kontekście zasobu również trzeba rozważyć;
nie zakładaj od razu jednego brakującego uprawnienia.

### B. Uprawnienia S3 wyglądają poprawnie, ale obiekt jest szyfrowany

> “Which KMS key encrypted this object, and can the calling identity use it?”

Kandydat powinien powiązać tożsamość i operację z właściwym kluczem. Zmiana
ogólnej polityki S3 nie naprawia automatycznie odmowy użycia KMS.

### C. Analityk uruchamia zapytanie, ale nie otrzymuje wyniku

Zapytanie może wymagać dostępu do kilku elementów. Trzeba ustalić, czy odmowa
dotyczy uruchomienia zapytania, katalogu, danych źródłowych, ich szyfrowania
czy lokalizacji wyników. Nie oczekuj zgadywania jednego winnego komponentu.
[AWS: IAM w Athenie](https://docs.aws.amazon.com/athena/latest/ug/security-iam-athena.html).

### Jak sprawdzić poprawkę

Odtwórz dozwoloną operację jako rzeczywisty odbiorca i potwierdź odmowę dla
niedozwolonego zakresu. Test administratora nie dowodzi dostępu analityka.
Test negatywny musi wykazać właściwą odmowę, a nie przypadkowo brakujący plik.

**Dopytaj przy:** propozycji stałego AdministratorAccess. Najpierw wyjaśnij,
czy to skrót, krok diagnostyczny czy docelowe rozwiązanie. Timeout i AccessDenied
są różnymi objawami; szczegóły łączności zostaw na Q6, jeśli problem jest sieciowy.

## 14. Koszt oraz rzeczywisty cel 15 minut

### Rozdziel oczekiwanie od wykonania

Cel powinien obejmować całą uzgodnioną drogę: oczekiwanie na start, kolejkę,
uruchomienie obliczeń, przetwarzanie, kontrolę i publikację. Jeśli proces
działa 13 minut, a wcześniej czekał 4, całość trwa 17 minut.

Początek pomiaru też ma znaczenie. „Od otrzymania pliku” nie jest automatycznie
„od chwili zdarzenia biznesowego w danych”. Dostawca może przysłać spóźnione dane.
Uzgodnij także, jak traktować błędne wejścia wymagające poprawy dostawcy.

> “How would you measure end-to-end readiness, including waiting and publication?”

### Co może kosztować

| Składnik | O co możesz dopytać |
| --- | --- |
| Obliczenia | Czas, przydzielone zasoby, współbieżność i niepotrzebne uruchomienia |
| Powtórzenia | Czy cały zbiór jest przeliczany mimo małej zmiany? |
| S3 | Objętość, retencja, wersje i liczba operacji |
| Zapytania | Ile danych trzeba przeczytać i czy można pominąć niepotrzebny zakres? |
| Ruch danych | Czy rozwiązanie nie przesyła danych niepotrzebnie między lokalizacjami? |
| Obsługa | Ilość logów, ich retencja i ręczna praca przy błędach |

Nie pytaj o aktualne ceny z pamięci. Koszt zależy od wybranego rozwiązania
i modelu rozliczenia. Oczekuj sposobu pomiaru i testowania hipotezy.

### Prosty przykład zapytań

Jeśli analityk pyta tylko o wtorek i dwie kolumny, odpowiedni układ danych może
pozwolić czytać mniej niż cały miesiąc i wszystkie pola. Partycjonowanie dzieli
dane np. według daty; format kolumnowy, np. Parquet, może ograniczać odczyt
potrzebnych kolumn. Efekt trzeba sprawdzić dla rzeczywistych zapytań.
[AWS: optymalizacja danych dla Atheny](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

Nie ma reguły „więcej partycji zawsze lepiej” ani „mniej zasobów zawsze taniej”.
Zbyt długie oczekiwanie na większą paczkę może obniżyć koszt operacji,
ale naruszyć cel czasu. Porównuj koszt i jakość usługi przy tym samym obciążeniu.

## 15. Możliwe odpowiedzi i ich interpretacja

### Ogólna lista usług

> “I would use S3, Glue, Lambda and Athena.”

To początek, nie pełny przepływ. Zapytaj, kto co robi, co uruchamia pracę
i co potwierdza gotowość. Nie zakładaj braku wiedzy przed dopytaniem.

### Spójny wariant na regular/mid

> “First I would clarify file volume, transformations and what ready means.
> I would keep source data separately, choose processing based on the workload,
> and deploy the environment with Terraform. The processor and analyst would
> have scoped roles. I would record invalid inputs, make retries safe, and
> verify the complete path within the 15-minute target.”

To dobry kierunek, jeżeli kandydat potrafi go skonkretyzować. Nie musi mieć
każdej zaawansowanej funkcji. Poproś o jeden mechanizm publikacji lub jeden
test, który sprawdziłby proponowane zachowanie.

### Mocniejsza odpowiedź

Dodatkowo wyjaśnia spójny zestaw danych, granice schematu, konflikt backfillu
z bieżącą pracą, dowody uprawnień i pomiar przy szczycie. Szczegóły są powiązane
z wymaganiami. To dodatkowa głębia, a nie obowiązkowy projekt całej organizacji.

| Gdy usłyszysz | Dopytaj |
| --- | --- |
| „Lambda zrobi wszystko” | “What operation does it perform, and what workload did you size it for?” |
| „Glue zajmie się danymi” | “Which code, trigger and completion check does that require?” |
| „Crawler sprawdzi dane” | “Which business-quality rules does it validate?” |
| „Uruchamiamy co 15 minut” | “How much time can an input wait before that run?” |
| „SQS zapobiegnie duplikatom” | “What prevents a duplicate effect when processing is repeated?” |
| „Wyzerujemy bookmark” | “What happens to previously written output?” |
| „IAM Allow wystarczy” | “Which identity, resource policies, key and applicable restrictions are involved?” |
| „Optymalizacja obniży koszt” | “What will you measure before and after, including delivery time?” |

Nie traktuj samodzielnej korekty po wyjaśnieniu jak utrzymującego się nieporozumienia.
Zapisz zakres pomocy. Jeśli nie znasz alternatywnej technologii, zanotuj jej
uzasadnienie do konsultacji zamiast wymagać własnej ulubionej architektury.

## 16. Jak poprowadzić Q2 w dziesięć minut

| Czas | Co robisz |
| --- | --- |
| 0:00–1:00 | Scenariusz główny, doprecyzowanie wymagań i odpowiedzi na pytania |
| 1:00–3:00 | Kandydat szkicuje źródło, wyzwalanie, przetwarzanie i wynik |
| 3:00–6:00 | Wybierasz dwa dopytania, np. duplikaty/schemat i bezpieczny backfill |
| 6:00–9:00 | Osobny scenariusz analityka z innego konta, KMS i AccessDenied |
| 9:00–10:00 | Główne koszty i pomiar wpływu optymalizacji na czas |

Nie rozbijaj każdego elementu na osobny egzamin. Jeśli w trakcie odpowiedzi
kandydat wyjaśnił monitoring lub izolację, nie pytaj o to samo tylko po to,
żeby odczytać listę. Zachowaj czas na bezpieczeństwo i koszt.

> “Could you sketch the simplest design that meets these assumptions?”

Jeśli odpowiedź jest ogólna, wybierz jeden plik i poproś o przeprowadzenie
przez całą drogę. Jeśli robi się zbyt szczegółowa, wróć do mechanizmu i dowodu.
Pełny proces Terraform należy do Q3, CI/CD do Q4, a długa diagnoza sieci do Q6.

### Notatka po Q2

```text
Uzgodnione wymagania i definicja gotowości:
Źródło -> wyzwalanie -> obliczenia -> wynik -> odbiorca:
Uzasadnienie wyboru usług:
Obsługa duplikatów, schematu i błędnych danych:
Backfill i reguła zapisu wyniku:
Środowiska / moduł dla data engineera:
Tożsamość analityka i model dostępu między kontami:
Rola KMS i plan diagnozy AccessDenied:
Koszt oraz dowód spełnienia 15 minut:
Podpowiedzi i obszary nieocenione:
```

## 17. Co zapisać w ocenie i czego nie wymagać

Szukaj samodzielnego wyjaśnienia typowego przepływu, prawidłowego rozumowania
o dostępie, świadomości błędów i sensownej weryfikacji. Nie sumuj liczby nazw usług.

| Obszar | Wystarczający konkret | Dodatkowa głębia |
| --- | --- | --- |
| Wymagania | Pyta o wolumen, operację i wynik | Wyjaśnia granice pomiaru i szczyt obciążenia |
| Przepływ | Umie powiedzieć, co wykonuje każdy krok | Oddziela przetwarzanie, kontrolę i publikację |
| Błędy danych | Jawne odrzucenie/oznaczenie i bezpieczne ponowienie | Uwzględnia wersje, współbieżność i zgodność schematu |
| Środowiska | Wie, jak ograniczyć przypadkową zmianę produkcji | Proponuje wspólne wzorce i kontrolę ich użycia |
| Dostęp | Ustala tożsamość, operację, zasób i KMS | Rozróżnia wzorce kont oraz dodatkowe warstwy polityk |
| Koszt i czas | Wskazuje istotny koszt i sposób pomiaru | Uzasadnia kompromisy i test w trudniejszych warunkach |

Dokumentacja przy szczegółach usług jest dopuszczalna. Brak znajomości konkretnej
nazwy API nie jest tym samym co brak rozumienia. Jeśli ważnego obszaru nie
sprawdzono, oznacz N/O. Propozycja oceny regular/mid nie jest oficjalnym progiem
zatrudnienia Capgemini.

Gdy kandydat nie zna Glue, może nadal wykazać poprawne kryteria wyboru silnika.
Zapisz osobno lukę produktową i wykazaną umiejętność projektowania. Gdy nie umie
powiązać żadnego elementu z wynikiem mimo dopytania, zapisz konkretny brak dowodu.

## 18. Ściąga prowadzącego i słownik

**Założenia znajdziesz w rozdziale 2:** 1-50 MB, średnio 10 MB; 10 000 plików/dzień,
szczyt 1000 w pięć minut; niezależne lekkie transformacje; poprawny wynik w SQL
do 15 minut; całe błędne pliki do kwarantanny; stały delivery_id, bez podwójnego
skutku. Dev/test/prod na osobnych kontach, pełny ruch tylko w prod.

### Sześć pytań, do których możesz wrócić

> “What does ready mean, and how would you measure it?”

> “Which component performs this operation?”

> “What happens if the same input is processed twice?”

> “How would you backfill without adding the old result again?”

> “Which identity is making the denied request?”

> “How would you prove that a cheaper design still meets the delivery target?”

### Krótki słownik

| Termin | Znaczenie |
| --- | --- |
| Raw / curated | Zachowane dane wejściowe / przygotowane dane wynikowe |
| Schema / crawler / catalog | Struktura danych / mechanizm wykrywania / przechowywany opis |
| Job / trigger / orchestration | Zadanie / wyzwalanie / koordynacja etapów |
| SQS / batch | Kolejka pracy / paczka rekordów |
| Idempotencja / backfill | Bezpieczny skutek powtórzenia / przeliczenie historii |
| Quarantine / publication | Wydzielenie błędnego wejścia / udostępnienie wyniku |
| Principal / trust / permissions | Tożsamość / zasady przejęcia roli / dozwolone operacje |
| KMS / least privilege | Użycie kluczy kryptograficznych / najmniejsze potrzebne uprawnienia |
| Partition / Parquet | Podział danych, np. po dacie / format kolumnowy |
| IaC / artifact / retention | Infrastruktura w kodzie / wdrażalna wersja kodu / czas zachowania |

Linki przy sekcjach prowadzą do oficjalnej dokumentacji. Szczegóły zweryfikowano
18 października 2026. Nazwy wariantów, limity i opcje sprawdzaj dla rzeczywiście
używanej usługi. Przykładowe czasy nie są gwarancjami AWS.

[Plan rozmowy](data_platform_engineer_devops_60min_pl.md) ustala pytania i czas.
[Ogólny przewodnik](przewodnik_dla_prowadzacego_aws_devops_pl.md) wyjaśnia wszystkie
bloki, a [przewodnik Q1](q1_migracja_s3_przewodnik_scenariusze_pl.md) omawia migrację.
Ten dokument pogłębia scenariusze Q2.
