# Przykładowe odpowiedzi — Data Platform Engineer / AWS DevOps

Materiał dla prowadzącego. Polska wersja pomocnicza do przygotowania rozmowy,
opracowana 17 października 2026 r. Sama rozmowa pozostaje prowadzona po angielsku.
Korzystaj razem z [planem rozmowy na 60 minut](data_platform_engineer_devops_60min_pl.md)
i osobnym [zadaniem dla kandydata](zadanie_python_dla_kandydata_pl.md).
Nie udostępniaj kandydatowi tego klucza odpowiedzi podczas zadania.

## Jak korzystać z dokumentu

To przykłady poprawnego rozumowania, a nie wypowiedzi, które kandydat ma powtarzać.
Przykłady dotyczące doświadczenia są hipotetycznymi szablonami, a nie
zweryfikowanymi informacjami o tej osobie. Fragmenty w nawiasach kwadratowych
zastąp dowodami z jej odpowiedzi. Nie wymagaj odpowiedzialności za całą platformę,
jeśli kandydat potrafi wykazać kompetencje w części, którą rzeczywiście dostarczył.

- **Poziom bazowy regular/mid:** zrozumienie wystarczające do typowego zadania w tej roli.
- **Mocniejsza odpowiedź:** dodatkowa głębia; nie jest obowiązkową listą wymagań.
- **Dopytaj:** odpowiedź niepełna lub niejednoznaczna, wymagająca wyjaśnienia.
- **Niepokojące po potwierdzeniu:** błędne rozumienie utrzymujące się po wyjaśnieniu.

Zadaj pytanie główne, a następnie wybierz pytania uzupełniające. Materiał obejmuje
więcej zagadnień, niż zmieści się w godzinie. Nie zamieniaj każdego przykładu
w dodatkowe pytanie. Komunikację oceniaj przez całą rozmowę po angielsku,
bez osobnego testu językowego. Nie obniżaj oceny za akcent lub pojedyncze błędy gramatyczne.

| Blok rozmowy | Oczekiwany poziom bazowy |
| --- | --- |
| Q1 — Odpowiedzialność | Wskazuje własną pracę, decyzję i zweryfikowany wynik |
| Q2 — Platforma i bezpieczeństwo | Wyjaśnia spójny przepływ danych, granice dostępu i obsługę błędów |
| Q3 — Terraform | Rozumie stan, przegląd zmian i częściowe niepowodzenia |
| Q4 — CI/CD | Wyjaśnia działający proces wdrażania i tymczasowy dostęp do AWS |
| Q5 — Python | Wyjaśnia return, wspólną wartość domyślną i filtrowanie logiczne w dwóch krótkich zadaniach, następnie omawia własną automatyzację i jej weryfikację |
| Q6 — Utrzymanie | Bada problem na podstawie dowodów, przywraca przetwarzanie i komunikuje wpływ |
| Pytania rezerwowe | Wykorzystuj zależnie od potrzeb; nie wymagaj omówienia każdego tematu |

## Q1. Odpowiedzialność za projekt AWS

### Pytanie główne

> W CV opisujesz migrację S3 między kontami prowadzoną od początku do końca.
> Czy możesz naszkicować przepływ danych i wskazać komponenty, które osobiście
> zaprojektowałeś, wdrożyłeś lub utrzymywałeś?

**Przykładowa odpowiedź regular/mid — hipotetyczny szablon:**

> Dane źródłowe znajdowały się na [koncie źródłowym], a odbiorcy potrzebowali
> dostępu przez [konto docelowe lub platformę]. Podstawowa konfiguracja kont
> i sieci już istniała. Odpowiadałem za [konkretne zmiany Terraform i automatyzację
> w Pythonie], natomiast [inny zespół] zajmował się [pozostałymi komponentami].
> Wdrożyłem [konkretną zmianę], przetestowałem ją na [środowisku] i sprawdziłem
> [raport migracji oraz odczyt wykonany jako docelowy odbiorca]. Zbadałem też
> [rzeczywistą awarię] i udokumentowałem ponowne uruchamianie nieudanych operacji.

**Wystarczające na tym poziomie:** wyraźne określenie własnego zakresu oraz jeden
konkretny przykład wdrożenia i jego weryfikacji. Przybliżona skala jest wystarczająca.

**Mocniejsza odpowiedź:** wyjaśnia wybór rozwiązania, zmiany wynikające z testów
oraz obserwowalny wynik, na podstawie którego potwierdzono sukces.

### Odpowiedzi na pytania uzupełniające

| Pytanie | Przykład akceptowalnej odpowiedzi |
| --- | --- |
| Jaka była skala migracji? | „Około [liczba obiektów / wolumen / liczba kont]. Dokładne dane sprawdziłbym w raporcie migracji. Głównym ograniczeniem było [tempo transferu, okno czasowe lub uprawnienia].” |
| Co już istniało? | „Zespół miał proces tworzenia kont i moduł bazowy. Dodałem [konkretne zasoby lub proces]. Nie projektowałem całej architektury.” |
| Jaką decyzję podjąłeś? | „Porównałem [dwie realne opcje] z [wymaganiem]. Wybraliśmy [opcję] ze względu na [powód], akceptując [kompromis].” |
| Co było najtrudniejsze? | „Zaobserwowałem [objaw], sprawdziłem [hipotezę], znalazłem [dowód], usunąłem [przyczynę] i z powodzeniem powtórzyłem wcześniej nieudaną operację.” |
| Jaką pracę techniczną wykonywałeś wcześniej? | „Zbudowałem [rzeczywistą automatyzację SQL/Python/raportowania], utrzymywałem ją dla [użytkowników] i sprawdzałem zmiany przez [proces]. Ta praca obejmowała / nie obejmowała infrastruktury chmurowej.” |

**Dopytaj:** „Używaliśmy Terraform i Lambdy”. Zapytaj: „Który plik, zasób lub
proces zmieniłeś i jak to sprawdziłeś?”.

**Niepokojące po potwierdzeniu:** mimo prośby o konkretny przykład nie potrafi
opisać własnego wkładu ani odróżnić wdrożonego rozwiązania od propozycji.

## Q2. Platforma danych AWS i bezpieczeństwo

### Główny scenariusz platformy

> Dostawca przesyła pliki CSV i JSON do S3. Inżynierowie danych je przetwarzają,
> analitycy odpytują przygotowane dane, a nowe dane muszą być dostępne w ciągu
> 15 minut. Jak wdrożysz i będziesz utrzymywać rozwiązanie w dev, test i produkcji?

**Stały profil tego pytania:** korzystaj z karty w [planie rozmowy](data_platform_engineer_devops_60min_pl.md):
pliki 1-50 MB bez kompresji, średnio około 10 MB, 10 000/dzień, szczyt 1000
w pięć minut w ramach tej liczby dobowej. CSV i JSON po rekordzie w wierszu;
niezależna walidacja schematu, typów i wymaganych pól oraz lekkie transformacje,
bez dużych złączeń i wywołań zewnętrznego API. Pełny ruch dotyczy produkcji;
dev/test używają danych syntetycznych na oddzielnych kontach. Do dziesięciu
analityków równocześnie odpytuje przygotowane dane.

15 minut dotyczy poprawnych nowych dostaw: od zakończenia zapisu do S3 do
dostępności wyniku dla uprawnionego SQL, razem z kolejką i publikacją przy
podanym szczycie. Odświeżanie BI jest poza celem. Błędny plik ma być oznaczony
w ciągu 15 minut, zachowany i odrzucony w całości, z alertem. Stały `delivery_id`
od dostawcy identyfikuje ponowienia także pod inną nazwą. Retencja raw 30 dni,
wyniku 90 dni; jeden region, KMS w spoczynku i TLS podczas przesyłania.
Zobacz [Q2: założenia i scenariusze](q2_platforma_aws_przewodnik_scenariusze_pl.md).

**Przykładowa odpowiedź regular/mid po doprecyzowaniu - tłumaczenie:**

> Potwierdzę profil i zachowam oryginalne dostawy w raw. Zdarzenia S3, kolejka
> i Lambda są jednym z wariantów dla niezależnego, lekkiego przetwarzania,
> ale przed doborem zasobów zmierzę pliki 50 MB i podany szczyt dostaw.
> Zdarzenia powinny wskazywać obiekty, zamiast przenosić cały plik. Sprawdzę
> pełne wejście przed publikacją, odrzucę błędne pliki z powodem i alertem,
> a stabilny identyfikator dostawy oraz trwały mechanizm ochronią przed
> podwójnym skutkiem. Opublikuję wynik dostępny dla SQL, zautomatyzuję
> wdrożenia na odizolowanych kontach, użyję ograniczonych ról i szyfrowania.
> Zmierzę czas od zapisu do odczytu. Sukces zadania nie wystarczy, jeśli
> poprawne dane nie są dostępne w 15 minut również podczas szczytu.

Odpowiednio grupowane przetwarzanie Glue również jest poprawne, jeśli cały
przepływ spełnia ten sam cel, a kandydat uzasadnia obsługę i koszt.
Nie wymagaj Lambdy, Sparka, SQS ani Atheny jako odpowiedzi z pamięci.

**Krótkie dopytanie związane z profilem:** “A thousand files arrive over five
minutes. What would you measure to check your design still meets the target?”
Słuchaj o wieku kolejki, przepustowości, błędach i faktycznej dostępności SQL,
kontrolowanej współbieżności i teście szczytu. Przy średniej 10 MB otrzymujemy
około 100 GB/dzień; 500 GB/dzień to przypadek samych plików po 50 MB. Te liczby
same nie określają czasu wykonania, pamięci ani kosztu zapytań.

**Wystarczające na tym poziomie:** spójny przepływ, uzasadniony dobór usług,
automatyzacja wdrożenia oraz świadomość uprawnień i błędów. Nie trzeba wymieniać
wszystkich usług ani projektować całej platformy korporacyjnej.

**Mocniejsza odpowiedź:** definiuje „gotowość” danych, oddziela przetwarzanie od
publikacji, omawia ponowne przetwarzanie i zgodność schematu oraz proponuje moduł
zadania dla inżynierów danych. Odróżnia uruchomienie zadania od jego zakończenia
i zweryfikowania zbioru wynikowego.

Glue może zapewniać integrację i przetwarzanie danych oraz Data Catalog; Athena
jest jedną z możliwych warstw zapytań. To przykład, a nie wymagany zestaw usług.
[Wprowadzenie do AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

### Pytania uzupełniające o platformę

**Gdzie przechowasz dane źródłowe i przygotowane?**

> Zachowam oryginalne wejście, żeby można było powtórzyć przetwarzanie.
> Przygotowane dane otrzymają osobną lokalizację i reguły publikacji. Osobno
> określę retencję i dostęp do każdego obszaru. Jeżeli pliki źródłowe mogą być
> nadpisywane, uzgodnię identyfikację dokładnej wersji użytej przez uruchomienie.

**Co uruchamia przetwarzanie i obsługuje zależności?**

> Wybiorę zdarzenia lub harmonogram zależnie od sposobu dostarczania danych
> i charakteru zadania. Kolejka może buforować dostawy i oddzielać odbiór od
> przetwarzania. Przy zależnych krokach muszę śledzić ich zakończenie i błędy;
> samo wysłanie kolejnego zadania nie oznacza jego poprawnego zakończenia.

**Jak wybierzesz między Lambdą a Glue?**

> Lambda może pasować do ograniczonej operacji wyzwalanej zdarzeniem lub kroku
> orkiestracji. Glue może odpowiadać większemu przetwarzaniu danych, szczególnie
> gdy jego silnik i równoległość pasują do transformacji. Sprawdzę czas wykonania,
> pamięć, rozmiar wejścia, przepustowość i koszt. Znajomość jednej usługi nie
> będzie jedynym kryterium.

Nie wymagaj limitów usług z pamięci. Brak znajomości konkretnej usługi może być
luką do uzupełnienia, mimo poprawnych kryteriów wyboru.

**Jak obsłużysz duplikaty plików lub zmianę schematu?**

> Określę stabilny identyfikator wejścia i zapewnię bezpieczne powtórzenie
> przetwarzania. Sprawdzę wymagane pola i typy. Błędne lub niezgodne dane zapiszę
> i odizoluję, z alertem, zamiast publikować je bez informacji o problemie.
> Zgodne rozszerzenia mogą być obsługiwane według udokumentowanych zasad schematu.

**Jak ponownie przetworzysz dane z jednego dnia?**

> Wybiorę ograniczony zakres źródeł i zapiszę identyfikator uruchomienia oraz
> wersję kodu. Zapis wyników musi bezpiecznie zastąpić lub scalić odpowiednie
> dane, zamiast bezwarunkowo je dopisywać. Zweryfikuję wynik przed publikacją
> i sprawdzę, czy równoległe przetwarzanie bieżące nie może go uszkodzić.

**Jaką wspólną funkcjonalność udostępnisz inżynierom danych?**

> Wersjonowany moduł lub szablon przyjmujący artefakt zadania, środowisko,
> zatwierdzone wejścia i wyjścia oraz ustawienia operacyjne. Zapewni spójne role,
> wyzwalanie, logi i alarmy, z opisanym procesem wdrażania i instrukcją obsługi.
> Każde zadanie nie powinno wymagać roli administratora.

### Dostęp między kontami i KMS

> Jak ograniczysz analitykowi z innego konta dostęp do zatwierdzonych,
> zaszyfrowanych danych i jak zbadasz błąd AccessDenied?

**Przykładowa odpowiedź regular/mid:**

> Ustalę dokładną rolę wykonującą żądanie oraz to, czy uzyskuje dostęp bezpośrednio,
> czy przejmuje rolę na koncie platformy. Nadam tylko potrzebne operacje do
> zatwierdzonej lokalizacji. Sprawdzę uprawnienia tożsamości i politykę zasobu S3,
> a przy zaszyfrowanych obiektach także uprawnienia KMS. Odtworzę nieudany odczyt
> jako odbiorca, zapiszę błąd i kontekst żądania oraz sprawdzę obowiązujące jawne
> odmowy, zamiast szeroko rozszerzać uprawnienia.

**Mocniejsza odpowiedź:** odróżnia zaufanie do roli od dostępu do danych, dostęp
bezpośredni między kontami od przejęcia roli oraz uwzględnia istotne ograniczenia
SCP, permissions boundary, sesji i endpointów. Lake Formation rozważa, jeśli
rozwiązanie rzeczywiście go używa.

Przy bezpośrednim użyciu klucza KMS z innego konta operację muszą dopuszczać
polityka klucza oraz polityka IAM na koncie wywołującego. Przejęcie roli zmienia
tożsamość podlegającą ocenie.
[Dostęp KMS między kontami](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html).

**Dopytaj:** „Sprawdzę IAM”. Zapytaj: „Którą tożsamość, operację, zasób i politykę
sprawdzisz jako pierwsze?”.

**Niepokojące po potwierdzeniu:** uznaje Allow po jednej stronie za nadrzędne
wobec każdego Deny lub proponuje stały szeroki dostęp jako rozwiązanie końcowe.

### Pytanie o koszty

> Co może generować największe koszty i jak ochronisz wymagany czas dostarczenia danych?

**Przykładowa odpowiedź:**

> Najpierw zmierzę koszty według procesów i środowisk. Sprawdzę czas i zasoby
> przetwarzania, zbędne powtórzenia, przechowywanie i retencję, ilość danych
> skanowanych przez zapytania oraz transfer. Zmianę przetestuję pod kątem kosztu
> przetworzenia zbioru i świeżości danych od źródła do odbiorcy, przy reprezentatywnym
> szczytowym obciążeniu. Tańsza konfiguracja musi nadal spełniać uzgodniony termin.

Oczekuj istotnych czynników kosztowych i pomiarów, a nie aktualnych cen z pamięci.

## Q3. Terraform w zespole

### Pytanie główne

> Opisz zmianę platformy od PR do produkcji. Gdzie przechowujesz stan i jak
> zapobiegasz konfliktującym zmianom?

**Przykładowa odpowiedź regular/mid:**

> Zmienię podlegający przeglądowi moduł i konfigurację środowiska w Git,
> uruchomię walidację i testy, a następnie przejrzę plan dla właściwego środowiska.
> Stan będzie w kontrolowanym zdalnym backendzie, poza laptopem programisty
> i repozytorium Git. Skonfiguruję blokadę oraz ograniczę dostęp do stanu.
> Wdrożenie produkcyjne będzie wymagać uzgodnionej akceptacji. Zapobiegnę
> równoczesnym, konfliktującym apply dla tego samego stanu. Po wdrożeniu sprawdzę
> konfigurację zasobów i reprezentatywny przepływ danych.

**Wystarczające na tym poziomie:** rozumie cel stanu, chroni go, przegląda plany,
oddziela środowiska i rozpoznaje ryzyko równoczesnych zmian.

**Mocniejsza odpowiedź:** omawia mniejsze zakresy stanu, wersje modułów i providerów,
pochodzenie zapisanego planu oraz osobne uprawnienia plan/apply, gdzie to uzasadnione.
Rozumie, że plan może się zdezaktualizować.

Backend S3 obsługuje opcjonalną blokadę przez `use_lockfile`; sam wybór S3 jej
nie włącza. Starsze blokowanie przez DynamoDB jest oznaczone jako przestarzałe.
Akceptuj poprawny opis starszego rozwiązania.
[Backend S3 Terraform](https://developer.hashicorp.com/terraform/language/backend/s3).

### Częściowo nieudane apply

> Bucket powstał, ale utworzenie polityki się nie udało. Co dalej? Czy cofnięcie
> zmiany w Git cofa infrastrukturę?

**Przykładowa odpowiedź regular/mid:**

> Sprawdzę błąd, faktycznie istniejące zasoby i aktualny stan Terraform.
> Część zmian mogła się zakończyć, więc nie zakładam automatycznego wycofania
> wszystkiego. Usunę przyczynę i przejrzę nowy plan przed ponownym apply.
> Cofnięcie commitu zmienia jedynie kod; nadal trzeba zaplanować i wykonać
> zamierzoną zmianę infrastruktury. Ochronię dane, które już się pojawiły.

**Mocniejsza odpowiedź:** uwzględnia nietypowy błąd zapisu stanu lub osierocone
zasoby i sprawdza sytuację przed importem lub uzgodnieniem stanu. Nie zakłada,
że każdy błąd apply wymaga importu lub ręcznej edycji stanu.

[Polecenie Terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply).

### Dodatkowe pytania Terraform

| Pytanie | Przykładowa odpowiedź regular/mid | Dodatkowa głębia |
| --- | --- | --- |
| Jak oddzielisz środowiska? | „Osobna konfiguracja i stan, odpowiednio ograniczone poświadczenia i jednoznaczny cel wdrożenia. Zmiana dev nie może domyślnie modyfikować produkcji.” | Oddzielne konta i mniejsze zakresy stanu, gdy uzasadnione; nazwy lub workspaces same nie tworzą granicy bezpieczeństwa. |
| Co ze zmianą wykonaną ręcznie w konsoli? | „Sprawdzę świeży plan, zidentyfikuję drift i uzgodnię zapis zmiany w kodzie albo przywrócenie konfiguracji deklarowanej. Nie nadpiszę bez wyjaśnienia zmiany produkcyjnej.” | Wyjaśnia odpowiedzialność, ślad audytowy i ograniczanie ponownego driftu. |
| Co jeśli plan usuwa zasób z danymi? | „Zatrzymam się i sprawdzę powód usunięcia lub zastąpienia, środowisko i tożsamość zasobu. Przed akceptacją ocenię ochronę oraz odtworzenie danych.” | Omawia zmiany providera, adresy zasobów, zabezpieczenia lifecycle i oddzielnie przetestowaną migrację. |
| Czy sensitive usuwa sekret ze stanu? | „Nie. Może ukryć wartość w zwykłym wyjściu, ale wartość nadal może trafić do stanu. Ograniczę i ochronię stan oraz dostęp do artefaktów planu.” | Mechanizmy ephemeral/write-only są odrębne; ich wsparcie zależy od zasobu i wersji Terraform. |

[Dane wrażliwe w Terraform](https://developer.hashicorp.com/terraform/language/manage-sensitive-data).

**Dopytaj:** „Uruchomię apply ponownie”. Zapytaj, co wcześniej sprawdzi.
Powtórzenie po zrozumieniu i usunięciu przyczyny może być poprawne.

**Niepokojące po potwierdzeniu:** rutynowe usuwanie stanu, wymuszanie odblokowania
bez sprawdzenia aktywnych uruchomień lub traktowanie apply jak atomowej transakcji
obejmującej wszystkie zasoby.

## Q4. CI/CD, OIDC i testy wdrożenia

### Pytanie główne

> Jak wdrażasz Terraform oraz wersjonowany skrypt Lambda lub zadanie Glue,
> testujesz zmianę i uzyskujesz dostęp do AWS z GitHub Actions?

**Przykładowa odpowiedź regular/mid:**

> PR uruchomi kontrole kodu, testy jednostkowe, walidację Terraform oraz utworzy
> plan do przeglądu dla danego środowiska. Workflow uzyska przez OIDC tymczasowe
> poświadczenia AWS dla odpowiednio ograniczonej roli. Wdrożę wersjonowany artefakt
> zadania z infrastrukturą i konfiguracją, sprawdzę cały przepływ poza produkcją
> i wypromuję zatwierdzoną wersję zgodnie z uzgodnionym procesem produkcyjnym.
> Nieudany test zatrzyma promocję. Zachowam dowody pozwalające ustalić, jaka wersja
> kodu i konfiguracji działa.

**Wystarczające na tym poziomie:** wiarygodna kolejność działań, testy, akceptacje,
tymczasowy dostęp, wersjonowane artefakty i weryfikacja po wdrożeniu.

### Pytania uzupełniające o OIDC

**Co zapobiega przejęciu roli przez inne repozytorium?**

> Polityka zaufania AWS musi ograniczać zaufanego wystawcę oraz odpowiednie
> claims tokenu, w tym audience i subject dla właściwego repozytorium i kontekstu
> wdrożenia. Ochrona środowiska produkcyjnego dodatkowo kontroluje zmiany mogące
> użyć tego kontekstu. Sprawdzę faktyczny format tokenu w tej konfiguracji,
> zamiast kopiować przykład z szerokim wildcardem.

**Polityka zaufania a polityka uprawnień?**

> Polityka zaufania określa, kto może przejąć rolę. Polityki uprawnień roli
> określają działania uzyskanej sesji. Skuteczne przejęcie roli nie oznacza
> możliwości odczytania każdego bucketa lub użycia każdego klucza KMS.

**Co daje `id-token: write`?**

> Pozwala zadaniu GitHub Actions poprosić o token OIDC. AWS nadal decyduje,
> czy token pozwala przejąć rolę i do czego ta rola ma dostęp.

**Mocniejsza odpowiedź:** omawia granice zaufania dla PR, chroni produkcję przed
niezaufanym kodem, ogranicza zakres roli i odróżnia akceptację środowiska od
walidacji claims tokenu. Dokładne ciągi claims nie są wymagane.

[OIDC GitHub w AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws).

### Testowanie i nieudane wdrożenie

| Pytanie | Przykład akceptowalnej odpowiedzi |
| --- | --- |
| Zasoby istnieją, ale odbiorca nie może odczytać danych. Jaki test to wykryje? | „Integracyjny odczyt jako docelowa rola odbiorcy, na reprezentatywnych zaszyfrowanych danych testowych, oraz sprawdzenie odmowy dostępu do niedozwolonych lokalizacji.” |
| Jak sprawdzisz zgodność zadania i schematu? | „Uruchomię nowy artefakt na reprezentatywnych danych i oczekiwanych schematach. Przed promocją sprawdzę pola wynikowe, reguły jakości i kompletność.” |
| Apply się udało, integracja nie. Co dalej? | „Zatrzymam promocję, określę wpływ i zbadam błąd. Wybiorę poprawkę lub kontrolowane wycofanie zależnie od zmiany i bezpieczeństwa danych.” |
| Co przenosisz między środowiskami? | „Sprawdzoną wersję lub digest artefaktu oraz uzgodnione wersje infrastruktury i konfiguracji. Wartości specyficzne dla środowiska są kontrolowaną konfiguracją.” |

**Dopytaj:** „Uruchamiamy pytest”. Zapytaj o tożsamość testową, sprawdzane
zachowanie oraz użycie mocków lub rzeczywistych zasobów AWS.

**Niepokojące po potwierdzeniu:** stałe klucze administratora jako domyślna opcja
CI bez uzasadnienia lub automatyczna promocja produkcyjna mimo nieudanego testu całego przepływu.

## Q5. Krótki przegląd Pythona i doświadczenie w automatyzacji

Ten blok wykorzystuje dwie krótkie funkcje i odpowiedzi ustne. Kandydat nie
musi implementować pełnego rozwiązania, pisać testów, konfigurować mocków ani
znać boto3. Przeznacz cztery minuty na zadanie 1, dwie na zadanie 2 i cztery
na rzeczywisty projekt. Zadanie 1 zawiera dwa błędy. Rekordy to ilustracyjne
dane testowe o ustalonej strukturze.

### Zrozumienie błędu i poprawka

> Co zwróci funkcja dla podanej listy i jak sprawić, aby sprawdziła wszystkie zadania?

Przyjmij świeżą definicję funkcji, bez wcześniejszych wywołań.

**Przykładowa odpowiedź regular/mid:**

> Pierwszy rekord ma status SUCCEEDED, więc jego nazwa nie trafia do listy.
> Instrukcja return nadal znajduje się wewnątrz pętli, dlatego funkcja kończy
> działanie po pierwszym rekordzie i zwraca pustą listę. Przesunę return failed
> poza pętlę, aby najpierw sprawdzić wszystkie zadania. To naprawia pierwszy
> błąd; nadal trzeba usunąć współdzielony akumulator domyślny.

### Kolejne wywołania po samej poprawce return

> Po przeniesieniu wyłącznie return poza pętlę, co zwrócą dwa kolejne wywołania
> failed_jobs(jobs) dla przykładowych danych? Przyjmij świeżą definicję funkcji
> i brak innych wywołań. Wyjaśnij drugi błąd i sposób naprawy.

To pytanie jest obowiązkowe. Każde wywołanie ma zwracać wyłącznie własne wyniki.

**Przykładowa odpowiedź regular/mid:**

> Lista domyślna powstaje raz, przy definiowaniu funkcji. Wywołania pomijające
> failed używają tej samej listy, a append ją zmienia. Pierwsze wywołanie zbiera
> dwie nazwy nieudanych zadań. Drugie dopisuje je ponownie, zamiast zaczynać
> od pustej listy. Usunę parametr failed i utworzę nową pustą listę wewnątrz
> funkcji przy każdym wywołaniu.

Po poprawieniu wyłącznie wcięcia return wartości wypisane natychmiast po każdym
wywołaniu, w podanej kolejności, wyglądają tak:

| Wywołanie | Wypisana wartość |
| --- | --- |
| Pierwsze `failed_jobs(jobs)` | `["load_orders", "load_products"]` |
| Drugie `failed_jobs(jobs)` | `["load_orders", "load_products", "load_orders", "load_products"]` |
| Następnie `failed_jobs([])` | Te same cztery stare nazwy, mimo pustego wejścia |

Pierwotny przedwczesny return ukrywa akumulację dla tych danych, bo pierwszy
rekord jest udany. Gdyby pierwszy rekord był błędny, także oryginalna funkcja
dopisywałaby wyniki między wywołaniami. Współdzielenie dotyczy domyślnego argumentu,
gdy go pominięto; nie wszystkich funkcji ani każdego argumentu podanego jawnie.

**Dodatkowa głębia:** oba wywołania zwracają ten sam obiekt listy. Zapisany pierwszy
wynik po drugim wywołaniu również zawiera cztery nazwy. Dlatego tabela opisuje
wartości wypisane natychmiast, a nie niezależne migawki zapisane wcześniej.

### Pełna poprawka

**Poprawiona funkcja — wyłącznie referencja dla prowadzącego:**

```python
def failed_jobs(jobs):
    failed = []
    for job in jobs:
        if job["status"] == "FAILED":
            failed.append(job["name"])
    return failed
```

Kandydat może wyjaśnić obie zmiany ustnie. Nie musi przepisywać funkcji.
Dopuszczalne są też domyślny `None` z nową listą w każdym wywołaniu, list comprehension
lub inne czytelne rozwiązanie dające niezależne wyniki. Pełna implementacja
ani zaawansowana składnia nie są wymagane.

### Przypadki wejściowe i oczekiwane wyniki

Każdy wiersz zakłada świeżą definicję funkcji. Kolumna po poprawce dotyczy
naprawienia obu błędów.

| Wejście | Oryginalna funkcja | Po poprawce |
| --- | --- | --- |
| Przykład: sukces, błąd, błąd | `[]` | `["load_orders", "load_products"]` |
| Pusta lista | `None`, bo pętla się nie wykona i funkcja dojdzie do końca | `[]` |
| Same udane zadania | `[]` po sprawdzeniu wyłącznie pierwszego zadania | `[]` po sprawdzeniu wszystkich zadań |
| Błąd, następnie kolejny błąd | Tylko nazwa pierwszego zadania | Obie nazwy |

**Przykładowa odpowiedź:**

> Po obu poprawkach puste wejście i lista bez błędnych zadań zwracają nową pustą
> listę, także po wcześniejszych nieudanych zadaniach.
> Oryginalna funkcja dla pustego wejścia zwraca None, ponieważ poza pętlą nie ma
> return. Sprawdziłbym też kilka błędnych zadań, aby potwierdzić, że funkcja
> nie kończy się po pierwszym wyniku.

Nie wymagaj pisania testów. Wystarczy wskazanie reprezentatywnych wejść
i oczekiwanych wyników. Brakujące pola są poza uzgodnionym kontraktem danych;
nie rozbudowuj zadania do tworzenia mechanizmu walidacji.

### Zadanie 2 - zadania do ponowienia

Skorzystaj z drugiego zadania w arkuszu kandydata. Wybieramy wyłącznie uruchomienia
ze statusem `FAILED` lub `TIMED_OUT`. Aktualny warunek to
`if job["status"] == "FAILED" or "TIMED_OUT":`.

**Co zwraca funkcja?**

> Zwraca wszystkie cztery nazwy: load_customers, load_orders, load_products
> i load_prices. Oczekiwany wynik zawiera tylko load_orders i load_products,
> bo wyłącznie te zadania mają status FAILED lub TIMED_OUT.

**Dlaczego warunek wybiera też zadania udane i anulowane?**

> Python sprawdza porównanie po lewej stronie or. Jeśli jest fałszywe, niepusty
> napis TIMED_OUT po prawej stronie jest traktowany jako prawda, więc ciało if
> nadal się wykona. Prawa strona nie jest kolejnym porównaniem statusu. Muszę
> porównać status z obiema wartościami lub sprawdzić przynależność.

**Kod referencyjny dla prowadzącego - poprawka:**

```python
def retryable_jobs(jobs):
    retryable = []
    for job in jobs:
        if job["status"] in ("FAILED", "TIMED_OUT"):
            retryable.append(job["name"])
    return retryable
```

Akceptuj również `job["status"] == "FAILED" or job["status"] == "TIMED_OUT"`
lub inne czytelne równoważne rozwiązanie. Wpisywanie kodu nie jest wymagane.

**Jakie wejścia warto sprawdzić?**

| Wejście | Oczekiwany wynik po poprawce |
| --- | --- |
| Cztery rekordy z przykładu | `["load_orders", "load_products"]` |
| Jeden rekord FAILED, następnie jeden TIMED_OUT | Obie nazwy, w kolejności wejściowej |
| Wyłącznie rekordy SUCCEEDED i CANCELLED | `[]` |
| Pusta lista | `[]` |

**Poziom bazowy:** przewiduje zwrócenie wszystkich nazw, wyjaśnia prawdziwość
niepustego napisu, proponuje poprawny warunek i reprezentatywne wejścia oraz wyniki.
Nie wymaga to znajomości implementacji operatorów ani pisania testów.

**Dopytaj:** „Czy napis po prawej stronie porównuje się ze statusem? Co się stanie,
gdy lewe porównanie jest fałszywe?”. Zapisz zakres pomocy. Sama zamiana `or` na `and`
nie realizuje wymaganego wyboru.

**Dodatkowa głębia:** wskazuje skrócone obliczanie warunku oraz to, że `or` zwraca
operand, niekoniecznie wartość Boolean. To opcjonalne. Brakujące pola, wykonanie
ponowień, backoff i integracja AWS są poza zakresem zadania.

### Własne doświadczenie z automatyzacją Python - 4 minuty

> Opisz automatyzację w Pythonie, którą osobiście wdrożyłeś. Co robiła,
> jak obsługiwałeś błędy i jak ją sprawdziłeś przed wdrożeniem?

**Przykładowa odpowiedź regular/mid — hipotetyczny szablon:**

> Napisałem [rzeczywisty skrypt lub Lambdę] wykonującą [konkretną operację].
> Wejściem było [źródło/konfiguracja], a wynikiem [rezultat]. Jawnie obsłużyłem
> [konkretny przewidywany błąd], a niepowodzenia były widoczne w [wyniku zadania,
> logu strukturalnym lub alercie]. Przed wdrożeniem sprawdziłem [reprezentatywne
> przypadki] i [rzeczywistą integrację] w środowisku testowym. Znalazłem
> [rzeczywisty błąd], a poprawkę potwierdziłem przez [dowód].

To podpowiedzi pomagające uzyskać dowody, a nie fakty o kandydacie.

**Pytanie uzupełniające: co z częściowym niepowodzeniem?**

> Ujawnię zakres udanych i nieudanych operacji, żeby wywołujący mógł zdecydować,
> czy przerwać, ponowić lub opublikować wynik. Samo wypisanie wyjątku
> i zgłoszenie pełnego sukcesu ukrywa problem przed operatorem.

**Pytanie uzupełniające: jak sprawdzisz kod używający usług zewnętrznych?**

> Kontrolowane odpowiedzi fake'a lub mocka pozwolą sprawdzić rozgałęzienia
> i obsługę błędów w moim kodzie. Oddzielny test integracyjny sprawdzi rzeczywistą
> konfigurację i uprawnienia usługi. Przykładowo sprawdzę zwykłe i puste wejście
> oraz błąd API. Każdy test jednostkowy nie musi odwoływać się do AWS.

**Pytanie uzupełniające: czy ponowienie po timeout jest zawsze bezpieczne?**

> Nie. Operacja zdalna mogła się zakończyć, mimo że nie otrzymałem odpowiedzi.
> Przed ślepym ponowieniem sprawdzę jej skutki oraz sposób identyfikacji lub
> uzgodnienia wcześniejszej próby.

**Poziom bazowy całego bloku Python:** wyjaśnia przedwczesny return, wspólną
mutowalną wartość domyślną, jej skutek między wywołaniami i poprawki dające niezależne
wyniki w zadaniu 1. Wyjaśnia i poprawia warunek logiczny w zadaniu 2. Opisuje
konkretną własną automatyzację i jej sprawdzenie. Oba zadania muszą zostać omówione;
zapisz potrzebne podpowiedzi, zamiast traktować wspólną wartość domyślną lub drugie
zadanie jako bonus.
Implementacja i pisanie testów podczas tego bloku nie są wymagane.

**Mocniejsza odpowiedź:** na własnym przykładzie wyjaśnia częściowe błędy,
bezpieczne ponowienia lub sensowne testy jednostkowe i integracyjne.
Nie wymagaj budowania tych mechanizmów podczas rozmowy.

**Dopytaj:** jeśli rozpoznaje błąd wcięcia bez wyjaśnienia przepływu, zapytaj
o wynik przy pierwszym udanym rekordzie. Jeśli pomija współdzieloną listę domyślną,
zapytaj, kiedy powstaje lista i czy następne wywołanie używa tego samego obiektu.
Samo nazwanie reguły bez wyjaśnienia wyników kolejnych wywołań jest niepełne.
Jeśli odpowiedź o projekcie jest listą
bibliotek, poproś o jedną rzeczywistą operację i obsłużony błąd.

**Niepokojące po potwierdzeniu:** po wyjaśnieniu nadal nie rozumie pętli i return
lub wielokrotnie traktuje ukryte błędy jako udaną automatyzację. Pojedyncza drobna
pomyłka nie wystarcza do uznania umiejętności programowania za słabe.

Te krótkie zadania sprawdzają czytanie kodu i podstawowe rozumowanie. Samodzielnie
nie dowodzą zdolności wdrażania automatyzacji produkcyjnej. Oddzielnie zanotuj
obserwacje z każdego fragmentu kodu i z opisu projektu.

## Q6. Utrzymanie, sieć i komunikacja podczas incydentu

### Pierwsze trzy kontrole

> CI jest zielone i pliki trafiają do S3, ale raport od 40 minut nie ma nowych
> danych. Jakie są Twoje pierwsze trzy kroki?

**Przykładowa odpowiedź regular/mid:**

> Najpierw potwierdzę dotknięty zbiór, ostatnią udaną aktualizację i związek
> czasowy z wdrożeniem. Następnie prześledzę znane nowe wejście przez dostarczenie
> zdarzenia i kolejkę, aby znaleźć zatrzymany etap. Na końcu sprawdzę wywołania,
> logi, uprawnienia i wyjście przetwarzania oraz to, czy raport czyta ten wynik.
> Każda hipoteza musi mieć konkretną obserwację. Zielone CI lub brak błędów Lambdy
> nie dowodzą, że nowe dane dotarły do odbiorcy.

**Wystarczające na tym poziomie:** uporządkowana diagnostyka oparta na dowodach
i świadomość wyniku dla odbiorcy. Nie wymagaj dokładnej nawigacji w konsoli
ani składni poleceń z pamięci.

**Mocniejsza odpowiedź:** koreluje identyfikatory obiektów i uruchomień, porównuje
zachowanie przed wdrożeniem i po nim, ogranicza dalszy wpływ oraz potwierdza
odtworzenie przez świeżość i uzgodnienie danych, a nie sam stan usługi.

### Wielokrotne przetworzenie tego samego zdarzenia

> Ta sama wiadomość dociera do Lambdy dwa razy. Jak zapobiegniesz podwójnemu efektowi?

**Przykładowa odpowiedź regular/mid:**

> Założę możliwość ponowień i użyję stabilnego identyfikatora operacji,
> powiązanego z wejściem lub zdarzeniem biznesowym. Zapis wyniku powinien
> umożliwiać bezpieczne powtórzenie albo zakończenie musi być śledzone trwale.
> Nie oprę rozwiązania na globalnym zbiorze Python, bo kolejne wykonanie Lambdy
> może działać w innym procesie lub po restarcie.

**Mocniejsza odpowiedź:** uwzględnia równoczesne próby i okno błędu między efektem
biznesowym a oznaczeniem zakończenia. Zbyt wczesny zapis „przetworzono” może zgubić
pracę, a zbyt późny dopuścić duplikat. Nie wymagaj pełnego protokołu rozproszonego
na poziomie bazowym.
[Lambda z SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

### Jedna błędna wiadomość w paczce

**Przykładowa odpowiedź:**

> Odróżnię błędy przejściowe od nieprawidłowych danych i ograniczę ponawianie
> udanej pracy. Przy odpowiedniej konfiguracji źródła zdarzeń częściowe
> odpowiedzi dla paczki pozwalają wskazać rekordy do ponowienia. Stale błędne
> wejścia potrzebują zapisanej ścieżki diagnostyki i kontrolowanego odtworzenia,
> na przykład skonfigurowanej kolejki DLQ. Sprawdzę visibility timeout,
> ponowienia i współbieżność względem czasu przetwarzania.

**Mocniejsza odpowiedź:** nieobsłużony wyjątek może spowodować błąd całej paczki;
jeśli istotna jest kolejność FIFO, obsługa musi ją zachować. Dokładny JSON odpowiedzi
nie jest wymagany.
[Obsługa błędów źródła SQS](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html).

### Odtworzenie zaległości i wykrywanie niekompletnych danych

**Przykładowa odpowiedź:**

> Naprawię i zweryfikuję przyczynę przed odtworzeniem ograniczonej zaległości.
> Ustalę zakres dotkniętych wejść, ograniczę tempo ponownego przetwarzania
> i uniknę powielania udanych wyników. Następnie porównam wejścia oczekiwane
> z przetworzonymi i sprawdzę zbiór widoczny dla odbiorcy. Będę monitorować
> świeżość i kompletność względem celu, z określonym właścicielem i instrukcją
> obsługi. Udane zadanie bez użytecznego wyniku nie powinno automatycznie oznaczać
> spełnienia wymagania dostarczenia danych.

**Mocniejsza odpowiedź:** odróżnia brak nowych danych u źródła od zatrzymanego
przepływu, wiąże świeżość z oczekiwanym harmonogramem dostaw i oddziela techniczne
zakończenie zadania od kompletności biznesowej danych.

### Timeout Lambdy w prywatnych podsieciach

**Przykładowa odpowiedź regular/mid:**

> Potwierdzę usługę docelową i błąd, potem sprawdzę trasy, DNS, security groups
> oraz istotne ACL i endpointy. Dla celu internetowego potrzebuję odpowiedniej
> drogi wyjścia; dla wspieranych usług AWS mogę użyć właściwego VPC endpointu.
> Sam timeout nie uzasadnia dodawania uprawnień IAM. Sprawdzę łączność,
> a rzeczywistą odpowiedź AccessDenied zbadam oddzielnie.

**Mocniejsza odpowiedź:** odróżnia gateway endpoint S3 i jego powiązanie z tablicą
tras od interface endpointu Secrets Manager, uwzględniając security groups,
prywatny DNS i polityki endpointu. Rozumie, że podpięcie Lambdy do publicznej
podsieci nie daje automatycznie internetu. To dodatkowa głębia, a nie dwuminutowy
egzamin z konfiguracji.
[Łączność VPC Lambdy](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-internet.html),
[Endpointy Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html),
[Gateway endpointy S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

### Informacja dla interesariuszy

**Przykładowa odpowiedź — hipotetyczny komunikat o incydencie:**

> Zbiór raportowy od 40 minut nie otrzymuje nowych danych, więc użytkownicy
> powinni traktować raport jako nieaktualny. Nowe pliki nadal trafiają do S3.
> Ustalamy, gdzie zatrzymuje się przetwarzanie, i sprawdzamy ostatnią zmianę.
> Przyczyna oraz możliwość automatycznego odtworzenia wszystkich opóźnionych
> wejść nie są jeszcze potwierdzone. Zweryfikujemy wadliwy etap, wdrożymy
> kontrolowaną poprawkę i sprawdzimy zaległości. Kolejną informację przekażę
> za 15 minut, również jeśli diagnostyka nadal będzie trwała.

Odstęp między komunikatami to przykładowe zobowiązanie, a nie obietnica czasu
naprawy. Nie oczekuj wymyślania pewnej przyczyny lub terminu przywrócenia.

### Pilna zmiana w środowisku regulowanym

**Przykładowa odpowiedź:**

> Wyjaśnię wpływ i zastosuję uzgodnioną procedurę zmiany awaryjnej. Włączę
> odpowiednią osobę zatwierdzającą, zapiszę zmianę i uzasadnienie, przeprowadzę
> wymaganą walidację oraz potwierdzę wynik. Później uzupełnię uzgodniony przegląd
> i zachowam dowody. Szczegółowe kroki zależą od zatwierdzonej procedury organizacji;
> nie będę zakładać uniwersalnej reguły GxP.

**Bazowa komunikacja:** zrozumiała, uporządkowana, uczciwa wobec niepewności
i jasna w zakresie następnych działań oraz odpowiedzialności. Idealna gramatyka nie jest wymagana.

## Pytania rezerwowe

Wykorzystuj je zamiennie lub do pogłębienia, a nie jako dodatkowy obowiązkowy zakres.

### R1. Przeniesienie zasobu z CloudFormation do Terraform

**Przykładowa odpowiedź regular/mid:**

> Zinwentaryzuję zasób i zależności, przygotuję zgodną konfigurację Terraform
> oraz zaplanuję kontrolowane przekazanie zarządzania. Upewnię się, że usunięcie
> z CloudFormation nie usuwa fizycznego zasobu, następnie zaimportuję go do
> docelowego stanu Terraform i sprawdzę plan. Sam import nie wystarczy:
> konfiguracja musi odpowiadać istniejącemu zasobowi. Celem jest jeden uzgodniony
> właściciel zarządzania, bez niezamierzonego zastąpienia zasobu.

**Mocniejsza odpowiedź:** sprawdza retencję i zależności na przypadku testowym,
unika aktywnego zmieniania zasobu przez oba narzędzia i uzyskuje plan bez
niezamierzonych zmian przed wznowieniem wdrożeń. Kolejność zależy od zasobu;
nie jest uniwersalną receptą poleceń.
[Import Terraform](https://developer.hashicorp.com/terraform/language/import),
[CloudFormation DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html).

### R2. Testy infrastruktury poświadczeniami administratora

**Przykładowa odpowiedź:**

> Udany test administratora dowodzi jedynie, że ta tożsamość mogła wykonać
> operację. Sprawdzę docelową rolę odbiorcy na dozwolonym zbiorze oraz odmowę
> dostępu do niepowiązanej lokalizacji lub zabronionej operacji. Potwierdzę,
> że błąd oznacza oczekiwaną odmowę autoryzacji, a nie złą nazwę zasobu
> lub brak danych testowych.

Poziom bazowy: rozpoznaje zależność od tożsamości. Dodatkowy atut: reprezentatywne
testy szyfrowania i dostępu między kontami bez ujawniania rzeczywistych danych.

### R3. Porównanie architektur logowania S3

**Przykładowa odpowiedź — hipotetyczny szablon:**

> Porównałem [rzeczywiste opcje] z pytaniami użytkowników, oczekiwanym wolumenem,
> retencją, wymaganiami audytowymi i akceptowalnym opóźnieniem zapytań.
> Uwzględniłem koszty odbioru, przechowywania, zapytań i obsługi. Zweryfikowałem
> [rzeczywiste założenia lub próbkę]. Wynikiem była [rekomendacja lub wdrożona
> zmiana], a decyzję wdrożeniową podjął [właściciel].

Nie oczekuj konkretnych usług, oszczędności liczbowych lub wdrożenia bez dowodów
od kandydata. Jasne odróżnienie analizy od implementacji jest pozytywnym sygnałem.

### R4. Uzgodnienie danych SQL po migracji

**Przykładowa odpowiedź regular/mid:**

> Najpierw uzgodnię zakres porównania: to samo okno czasowe, filtry, klucze
> biznesowe i świeżość danych po obu stronach. Porównam liczby rekordów,
> a następnie brakujące klucze i wielokrotności duplikatów. Dla zgodnych kluczy
> porównam istotne wartości z uzgodnioną obsługą nulli i typów. Same równe liczby
> wierszy nie dowodzą zgodności, bo różne braki i duplikaty mogą się równoważyć.

**Mocniejsza odpowiedź:** używa liczności grupowanych po kluczu lub partycji
i odpowiednich złączeń, uwzględniając spóźnione dane i semantykę porównania.
Nie ukrywa nieoczekiwanych duplikatów przez DISTINCT.

### R5. Diagnostyka Dockera

**Przykładowa odpowiedź regular/mid:**

> Opiszę problem, który kontener rozwiązywał w moim projekcie. Przy jego awarii
> sprawdzę status zakończenia i logi, wersję obrazu, polecenie, konfigurację,
> wymagane sekrety, limity zasobów i dostęp do zależności. Odtworzę problem
> z reprezentatywną konfiguracją i sprawdzę poprawkę.

**Mocniejsza odpowiedź:** łączy objaw z konkretną przyczyną wykonania, omawia
powtarzalne budowanie i minimalne uprawnienia. Brak głębokiej znajomości Kubernetes
nie jest automatycznym powodem negatywnej oceny, jeśli rola jej nie wymaga.

### R6. Kompletność migracji S3 i przełączenie odbiorców

**Przykładowa odpowiedź regular/mid:**

> Określę oczekiwany zakres źródła i migrowaną wersję lub punkt odcięcia.
> Obiekty historyczne wymagają jawnego transferu lub uzupełnienia, a bieżące
> zmiany osobnej obsługi. Porównam obiekty oczekiwane i przesłane, rozliczę błędy
> i sprawdzę odczyt jako odbiorca docelowy przed przełączeniem. Jeśli zapisy
> trwają dalej, potrzebuję uzgodnionego nadrobienia zmian lub spójnego punktu przekazania.

**Odpowiedzi uzupełniające:**

- **Obiekty sprzed włączenia replikacji:** „Nie zakładam, że replikacja bieżąca
  automatycznie je przeniesie. Wybiorę transfer historyczny, np. Batch Replication,
  jeśli pasuje do sytuacji, i zweryfikuję wynik.”
- **Nadpisania i wersje:** „Uzgodnię, czy potrzebujemy tylko aktualnej wersji,
  czy także historii, i względem tego zakresu wykonam uzgodnienie.”
- **Liczba a zawartość:** „Równe liczby mogą ukrywać różne brakujące obiekty lub
  błędną zawartość. Potrzebne są zgodne identyfikatory i właściwa kontrola
  integralności; ETag nie zawsze jest skrótem MD5 pliku.”
- **Błędne kopie:** „Zapiszę trwały raport błędów, usunę przyczynę, bezpiecznie
  ponowię nieudany zakres i ponownie sprawdzę miejsce docelowe.”

[Zakres replikacji AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-what-is-isnot-replicated.html),
[Obiekt S3 i ETag](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Object.html).

Przy pytaniu o AccessDenied zaszyfrowanego obiektu wykorzystaj rozumowanie
tożsamość/S3/KMS z Q2. Nie wymagaj pełnej polityki roli replikacji z pamięci.

### R7. Rotacja kluczy dostępu IAM

**Przykładowa odpowiedź regular/mid:**

> Najpierw uzasadnię, dlaczego odbiorca nie może używać poświadczeń tymczasowych.
> Utworzę nowy klucz, gdy stary jeszcze działa, bezpiecznie go zapiszę,
> zaktualizuję odbiorców i sprawdzę ich rzeczywiste operacje. Potem dezaktywuję
> stary klucz, zaobserwuję wynik i usunę go po uzgodnionych kontrolach.
> Zapiszę postęp, żeby ponowienie nie tworzyło bezwarunkowo kolejnego klucza.
> Wartości sekretów nigdy nie trafią do logów.

**Błąd po utworzeniu klucza, ale przed zapisem sekretu:**

> IAM nie zwróci tego sekretu ponownie. Porównam istniejące klucze z zapisanym
> stanem rotacji i zidentyfikuję osierocony klucz z tej próby. Przed usunięciem
> lub ponowieniem ustalę, czy nie używa go inna próba albo odbiorca.
> Proces wymaga świadomej ścieżki odzyskania; tworzenie kolejnych kluczy może
> wyczerpać limit lub zakłócić prawidłową rotację.

**Co udowodniła walidacja STS?**

> GetCallerIdentity wskazuje tożsamość reprezentowaną przez poświadczenia.
> Nadal muszę sprawdzić zamierzoną operację, np. odczyt zatwierdzonego,
> zaszyfrowanego obiektu. Uwierzytelnienie i autoryzacja to odrębne kontrole.

**Co jeśli odbiorca buforuje stary sekret?**

> Sprawdzę sposób odświeżania i potwierdzę przełączenie przed wycofaniem starego
> klucza. Okres przejściowy musi wynikać z zachowania odbiorcy i monitoringu,
> a nie arbitralnego sleep. Dezaktywacja daje kontrolowany punkt weryfikacji
> przed trwałym usunięciem.

**Mocniejsza odpowiedź:** wspomina limit dwóch kluczy, również nieaktywnych,
współbieżne wywołania, trwały identyfikator rotacji i odpowiedzialność za odzyskanie.
Pełny protokół automatycznej rotacji wykracza poza poziom bazowy.
[Rotacja kluczy AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html),
[Limity i odczyt sekretu klucza](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
[GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html).

### R8. Ujawnione hasło do bazy w GitHub - rezerwa na 2-4 minuty

**Pytanie do zadania po angielsku:**

> You discover that a database password was committed to a GitHub repository
> used by an AWS data pipeline. A teammate removes it in a new commit and says
> the problem is solved. Do you agree? What would you do next, and how would
> you check that the pipeline still works?

**Wystarczająca odpowiedź regular/mid - tłumaczenie:**

> Nie. Hasło może nadal być w historii Git lub innych kopiach. Traktuję je
> jako ujawnione i angażuję właściciela incydentu oraz bazy, aby szybko je
> unieważnić lub zmienić. Odzyskanie wymaga uzgodnienia poświadczenia w bazie,
> wartości przechowywanego sekretu oraz jego odbiorców. Sprawdzam, że stare
> poświadczenie już nie działa, a właściwe zadanie wykonuje dozwoloną operację
> z nowym, bez logowania wartości. Osobno koordynujemy usunięcie innych kopii
> i ewentualne czyszczenie historii. Wyjaśniam też, jak sekret trafił do repozytorium.

Kolejność ograniczenia ryzyka i rotacji zależy od zagrożenia, bazy i procedury
organizacji. Nie wymagaj bezprzerwowej rotacji ani dwóch jednocześnie ważnych
haseł dla dowolnej bazy. Sama zmiana wartości w magazynie sekretów nie dowodzi,
że baza przyjmuje nowe hasło.
[AWS: rotacja sekretu](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

**Wybierz jedno dopytanie:**

| Pytanie | Oczekiwane rozumowanie |
| --- | --- |
| What if the repository is private? | Węższy dostęp nie oznacza braku ujawnienia. Ustalenie odbiorców i unieważnienie ujawnionego poświadczenia. |
| Secrets Manager was updated, but the job fails. What next? | Hasło faktycznie przyjmowane przez bazę, referencja/wersja sekretu, cache, konfiguracja odbiorcy i dokładny błąd. Rozróżnienie logowania, uprawnień i łączności. |
| How would you reduce recurrence? | Sekrety poza kodem, ograniczony dostęp w czasie wykonania, brak wartości w logach, odpowiednie skanowanie i review. |

**Dopytaj:** „usunę plik” lub „zrobię force-push” bez unieważnienia hasła;
„zrestartuję zadanie” bez ustalenia, skąd bierze poświadczenie.

**Mocniejsza odpowiedź:** identyfikuje odbiorców, okres ujawnienia, koordynuje
reakcję, sprawdza dostępne dowody audytowe i przywrócenie dostarczania danych.
Brak podejrzanego wpisu nie jest dowodem, że na pewno nie było użycia.

**Niepokojące po potwierdzeniu:** przekonanie, że nowy commit lub prywatne
repozytorium zabezpiecza stare hasło; propozycja wklejania go do rozmowy lub logów.

Bez komend czyszczenia Git, implementacji i prawdziwych poświadczeń. Dwie minuty
na podstawę, do czterech z jednym dopytaniem. Zachowaj końcowe pięć minut dla
kandydata i osobno zapisz lukę w pominiętej umiejętności.
Zobacz [przewodnik R8](r8_sekret_w_git_przewodnik_scenariusze_pl.md).
[GitHub: usuwanie danych wrażliwych](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## Końcowa kalibracja dla prowadzącego

Odpowiedni kandydat regular/mid powinien samodzielnie wyjaśniać typową pracę,
rozpoznawać częste błędy i sprawdzać wyniki. Może korzystać z dokumentacji przy
szczegółach usług i przyznawać się do luk. Nie musi odtwarzać wszystkich elementów
opisanych jako mocniejsze odpowiedzi.

| Obserwacja | Interpretacja |
| --- | --- |
| Poprawna odpowiedź bazowa z rzeczywistym przykładem | Dowód przemawiający za poziomem 3 w tym obszarze |
| Poprawny kierunek, ale potrzebne liczne podpowiedzi | Zapisz zakres pomocy; często odpowiada poziomowi 2 |
| Szczegółowe kompromisy i obsługa częściowych błędów | Dodatkowe dowody na poziom 4, a nie obowiązkowa podstawa |
| Nieznana nazwa API, ale poprawne rozumowanie | Pozwól użyć dokumentacji; oceń właściwą umiejętność |
| Błędne twierdzenie poprawione po wyjaśnieniu | Zapisz zakres podpowiedzi i sprawdź zrozumienie poprawionej odpowiedzi |
| Utrzymujące się podstawowe nieporozumienie | Zapisz konkretne błędne rozumienie i jego skutek operacyjny |
| Tematu nie omówiono | Oznacz N/O; nie wnioskuj o braku umiejętności |

Oceniaj zaobserwowane dowody, a nie podobieństwo do tych zdań. Umiejętności
techniczne, komunikację i formalny wymóg doświadczenia zapisuj jako osobne obserwacje.
