# O co pytam na rozmowie?

Przewodnik dla prowadzącego bez doświadczenia DevOps

**Data Platform Engineer / AWS DevOps · wersja polska · 17 października 2026**

Ten materiał wyjaśnia zagadnienia z przygotowanej rozmowy: od podstaw platformy
danych przez Terraform, CI/CD i bezpieczeństwo po oba zadania Python oraz awarie.
Każdy temat łączy znaczenie pojęć z celem pytania i sposobem oceny odpowiedzi.

Czytaj przed rozmową. Podczas interview korzystaj z krótkiego planu i klucza
odpowiedzi. Rozmowa z kandydatem pozostaje prowadzona po angielsku.

Przykłady architektury, zdarzeń i wartości liczbowych są dydaktyczne.
Nie opisują potwierdzonej infrastruktury Capgemini ani osiągnięć kandydata.

## 1. Jak korzystać z przewodnika

### Co musisz umieć przed zadaniem pytania

Powinieneś rozumieć problem, skutek błędu i rodzaj dowodu potwierdzającego sukces.
Nie musisz znać składni konfiguracji AWS ani wszystkich możliwych architektur.
Gdy kandydat wybiera inne narzędzie, poproś o uzasadnienie względem wymagań.

W każdym bloku wracaj do czterech rzeczy: **co ma działać, co może się zepsuć,
jak to zauważymy i jak sprawdzimy naprawę**. Same nazwy usług nie odpowiadają
na te pytania.

| Pytania z planu | Co musisz rozumieć | Rozdział |
| --- | --- | --- |
| Q1: projekt, skala, własna decyzja | Przepływ danych, wkład własny, wynik i dowód | 2–3 |
| Q2: pliki, przetwarzanie, 15 minut, schemat, backfill, koszt | Elementy platformy i wymagania dotyczące danych | 2 i 4 |
| Q2: analityk z innego konta, KMS, AccessDenied | Tożsamość, uprawnienia, szyfrowanie i granice kont | 5 |
| Q3: PR, state, locking, drift, częściowy apply, sensitive | Bezpieczne zmienianie infrastruktury | 6 |
| Q4: pipeline, OIDC, artefakty, testy i promocja | Droga zmiany od kodu do sprawdzonej produkcji | 7 |
| Q5: dwa fragmenty kodu i własna automatyzacja | Czytanie kodu, stan między wywołaniami, logika i testy | 8–10 |
| Q6: brak nowych danych, duplikaty, paczki, sieć, komunikacja | Diagnostyka, bezpieczne odtworzenie i wpływ biznesowy | 11–14 |
| Pytania rezerwowe z CV i R8 | CloudFormation, Docker, SQL, hasło w Git, migracja S3, rotacja kluczy | 15–16 |
| Ocena i niezrozumiałe skróty | Kalibracja dowodów i słownik | 17–18 |

### Prosty sposób dopytywania po angielsku

> “Could you explain that using one concrete example?”

> “What would you check to prove that it worked?”

> “What happens if the operation stops halfway through?”

Jeżeli nie rozumiesz odpowiedzi, poproś o prostsze wyjaśnienie i zaznacz miejsce
do sprawdzenia. Nie zamieniaj własnej niepewności w negatywną ocenę kandydata.
Złożony wariant zapisz do weryfikacji z osobą techniczną.

## 2. Podstawy: co właściwie buduje ta osoba

### Platforma danych i DevOps

Platforma danych to zestaw usług i zasad, dzięki którym dane docierają od dostawcy
do użytkownika. Przykład: firma otrzymuje pliki zamówień, przelicza je i udostępnia
analitykowi tabelę do raportu. Potrzebne są miejsce na pliki, przetwarzanie, dostęp,
wdrażanie zmian i wykrywanie awarii.

Data engineer zwykle tworzy logikę przekształceń. Data Platform Engineer w tym
interview ma zapewniać środowisko, w którym takie zadania da się powtarzalnie
uruchamiać, zabezpieczać i utrzymywać. Granice obowiązków zależą od zespołu.
DevOps oznacza współpracę przy dostarczaniu i utrzymaniu oprogramowania, wspieraną
automatyzacją; nie sprowadza się do jednego produktu.

### Słowa, które padną od początku

| Pojęcie | Proste znaczenie | Przykład w rozmowie |
| --- | --- | --- |
| AWS | Chmura oferująca usługi informatyczne | Korzystamy z gotowych usług zamiast budować wszystko samodzielnie |
| Konto AWS / account | Oddzielna przestrzeń zarządzania zasobami, dostępem i rozliczeniami | Konto produkcyjne i konto testowe |
| Region | Obszar geograficzny działania usług | Wybór wpływa m.in. na dostępność, odległość i wymagania danych |
| Zasób / resource | Konkretny element infrastruktury | Bucket, kolejka, rola lub funkcja |
| API | Interfejs pozwalający programowi wywołać operację innej usługi | Skrypt prosi S3 o odczyt obiektu |
| SDK / boto3 | Biblioteka ułatwiająca korzystanie z API | boto3 jest SDK AWS dla Pythona |
| Dev, test, prod | Środowiska rozwoju, sprawdzania i rzeczywistej pracy | Błąd w dev nie powinien zmieniać danych produkcyjnych |
| Konsola / console | Panel WWW do obsługi chmury | Ręczna zmiana uprawnień w panelu |
| Serverless | Dostawca zarządza podstawową infrastrukturą wykonawczą | Nadal konfigurujemy kod, dostęp, limity, koszt i monitoring |

### Jeden przepływ, który warto umieć narysować

```text
Dostawca -> S3 raw -> informacja o nowym pliku -> kolejka
                       -> przetwarzanie -> S3 curated
                       -> katalog + zapytania -> raport
```

Raw to zachowane wejście, curated to przygotowane dane. Zdarzenie zwykle przenosi
informację o pliku, a procesor odczytuje sam plik z magazynu. Istnienie pliku
wejściowego nie dowodzi, że raport został zaktualizowany.

**Sens rozmowy:** kandydat powinien łączyć komponenty z potrzebą użytkownika.
Zdanie „wdrożyłem Lambdę” potrzebuje dalszego wyjaśnienia: co uruchamiało funkcję,
co robiła, gdzie zapisywała wynik i jak potwierdzano jego poprawność.

## 3. Q1: własny wkład, skala i odpowiedzialność

**O co pytasz:** czy kandydat rzeczywiście wykonywał opisane działania i rozumie
ich rezultat. End-to-end oznacza odpowiedzialność za uzgodniony przebieg od początku
do końca, np. plan, wdrożenie, testy i przekazanie. Nie musi oznaczać samodzielnego
zbudowania każdego komponentu.

W migracji źródło to miejsce, z którego dane wychodzą, a miejsce docelowe to ich
nowa lokalizacja. Odbiorca to osoba lub program korzystający z wyniku.
Interesariusz / stakeholder to osoba zainteresowana wynikiem albo wpływem zmiany.

### Jak czytać odpowiedź

| Gdy pytasz o… | Po co | Przykład konkretu |
| --- | --- | --- |
| Skalę | Poznać ograniczenia i kontekst rozwiązania | Wielkość danych, liczba plików, kont, czas na migrację |
| Co już istniało | Oddzielić pracę własną od odziedziczonej platformy | Istniała sieć; kandydat dodał role i automatyzację kopiowania |
| Własną decyzję | Sprawdzić rozumienie kompromisów / trade-offs | Szybsza metoda wymagała dodatkowego kosztu lub kontroli |
| Trudny problem | Zobaczyć sposób diagnozowania | Błąd, hipoteza, sprawdzenie, przyczyna, udane powtórzenie |
| Wynik | Odróżnić aktywność od efektu | Lista braków była pusta, a odbiorca odczytał wymagane dane |

Przybliżone liczby i zanonimizowane przykłady są wystarczające. Nie nakłaniaj
do ujawniania poufnych nazw. Używanie „my” jest naturalne; dopytaj, za co
odpowiadała ta osoba.

**Odpowiedź zrozumiała i wiarygodna:** „Zmieniłem politykę dostępu, odtworzyłem
nieudany odczyt rolą odbiorcy i potwierdziłem działanie po wdrożeniu”.
**Dopytaj przy:** „Zajmowaliśmy się AWS i automatyzacją”. Brakuje konkretnej operacji.

> “Which part did you personally change, and how did you verify it?”

Wcześniejsze doświadczenie finansowe może dostarczać dowodów analizy, SQL,
automatyzacji i komunikacji. Nie zakładaj automatycznie, że oznacza ten sam zakres
co praca przy infrastrukturze chmurowej. Formalny staż i wykazane umiejętności
zapisuj oddzielnie.

## 4. Q2: platforma danych, jakość i koszt

### Do czego służą poszczególne elementy

S3 przechowuje obiekty, np. pliki. Bucket jest pojemnikiem na obiekty, a key jest
ich nazwą/identyfikatorem, np. `raw/orders/2026-10-17.csv`. Prefix to początek
takiej nazwy; przypomina ścieżkę katalogu, lecz S3 nie jest zwykłym dyskiem.
CSV zapisuje dane tabelaryczne, JSON pozwala opisywać także zagnieżdżone struktury.

| Element | Rola w przykładowym projekcie |
| --- | --- |
| Lambda | Uruchamia kod, np. obsługuje zdarzenie lub niewielką operację |
| Glue job | Wykonuje przetwarzanie i integrację danych, np. większą transformację |
| Glue Data Catalog | Przechowuje metadane: opis tabel, kolumn i lokalizacji danych |
| Athena | Pozwala wykonywać zapytania SQL nad odpowiednio opisanymi danymi |
| SQS | Buforuje wiadomości z pracą do wykonania; oddziela tempo dostaw od przetwarzania |
| EventBridge / harmonogram | Może uruchamiać proces według zdarzenia lub czasu |
| Orkiestracja | Pilnuje kolejności, zależności, zakończeń i błędów kroków |
| SNS | Usługa publikowania powiadomień do subskrybentów |

Glue może dostarczać zarówno przetwarzanie, jak i katalog. Sam katalog nie
przelicza danych. Odpowiedni wybór między Lambdą a Glue wymaga znajomości wielkości
wejścia, złożoności operacji i czasu działania; sama nazwa usługi nie rozstrzyga.
[AWS: możliwości Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

### Dlaczego kandydat powinien najpierw zadać pytania

Plik 100 KB i zestaw plików o łącznym rozmiarze 1 TB stawiają inne wymagania.
Ważna jest też częstotliwość, transformacja, poufność i sposób używania danych.
Wymóg „gotowe w 15 minut” musi określać początek i koniec pomiaru, np. od
otrzymania pliku do dostępności zweryfikowanego wyniku dla analityka.

**Przykład:** proces kończy się po 8 minutach, ale dane są dostępne dla zapytania
SQL dopiero po kolejnych 20, ponieważ katalog lub publikacja nie są gotowe.
Cel 15 minut nie został spełniony. Samo odświeżenie dashboardu BI jest poza
celem Q2. To założenie ćwiczenia, a nie faktyczna umowa klienta.

### Stałe założenia Q2 i gotowe odpowiedzi

Pełna tabela odpowiedzi po angielsku znajduje się bezpośrednio przy Q2
w [planie rozmowy](data_platform_engineer_devops_60min_pl.md) oraz w rozdziale 2
[osobnego przewodnika Q2](q2_platforma_aws_przewodnik_scenariusze_pl.md).
Odczytaj odpowiedni wiersz, gdy kandydat zapyta. Jeśli nie pyta, podaj
przynajmniej rozmiar, tempo i operacje przed oceną wyboru usług.

- Pliki 1-50 MB bez kompresji, średnio 10 MB; CSV z nagłówkiem lub JSON
  z jednym rekordem w wierszu, kodowanie UTF-8.
- Około 10 000 plików/dzień w produkcji, w tym szczyt do 1000 w pięć minut.
  Daje to około 100 GB/dzień przy średniej, nie automatycznie 500 GB.
- Niezależna walidacja schematu, pól i typów, lekkie mapowania i filtracja;
  bez dużych złączeń i zależności od zewnętrznych API.
- Do dziesięciu równoczesnych zapytań analityków. Poprawne nowe dostawy
  dostępne dla uprawnionego SQL do 15 minut od zakończenia zapisu do S3,
  także podczas podanego szczytu; wliczamy kolejkę i publikację.
- Odrzucamy cały błędny plik, zachowujemy raw, powód i status, alarmujemy
  i umożliwiamy kontrolowany replay. Rozpoznanie błędnego pliku do 15 minut
  nie oznacza obietnicy jego naprawienia w tym czasie.
- Dostawca przekazuje stały `delivery_id` w metadanych. Ponowienie pod inną
  nazwą zachowuje ten identyfikator i nie może podwoić wyniku.
- Osobne konta dev, test i prod, wspólny wzorzec IaC; pełny ruch tylko w prod,
  syntetyczne dane w dev/test. KMS w spoczynku, TLS w transmisji i ograniczone role.
- Jeśli zapyta o retencję: raw 30 dni, curated 90 dni; jeden region, bez
  dodatkowego wymagania odtwarzania między regionami.

**Ocena wymagań:** są odpowiednie dla Regular/Mid po doprecyzowaniu szczytu,
końca pomiaru, reguły błędów i tożsamości powtórzeń. Nie wymagają jednej usługi
przetwarzania ani pełnego ruchu produkcyjnego w trzech środowiskach. Oczekuj
uzasadnienia i testu 50 MB oraz szczytu, nie gwarancji wydajności z pamięci.

### Schemat, duplikaty i ponowne przetwarzanie

Schemat opisuje pola i typy, np. `order_id` jako tekst, `amount` jako liczbę.
Zmiana schematu może być zgodna, np. dopuszczone dodatkowe pole, albo niezgodna,
np. brak wymaganego identyfikatora. Walidacja sprawdza dane przed publikacją;
kwarantanna to wydzielenie błędnego wejścia do wyjaśnienia.

Duplikat pliku lub rekordu nie zawsze rozpoznasz po nazwie. Potrzebna jest
uzgodniona tożsamość wejścia i sposób traktowania wersji. Backfill oznacza
uzupełnienie historii, np. ponowne przeliczenie wtorku. Replay oznacza ponowne
odtworzenie wskazanych zdarzeń lub wejść. Oba wymagają ochrony przed podwójnym
doliczeniem wcześniej zapisanych wyników.

**Dlaczego zachowujemy raw:** po wykryciu błędu w kodzie możemy odtworzyć wynik
z pierwotnych danych. Trzeba ustalić dokładną wersję wejścia, wersję kodu,
zakres i regułę zastąpienia albo scalenia wyników.

**Wspólny moduł dla data engineerów:** gotowy wzorzec przyjmujący kod zadania,
wejścia, wyjścia i środowisko; automatycznie tworzy uzgodnione role, logi,
wyzwalanie i alarmy. Dzięki temu nowy proces nie wymaga konfiguracji od zera.

### Koszt: pytaj o pomiar i kompromis

Koszt mogą zwiększać długie obliczenia, zbyt duże zasoby, wielokrotne przetwarzanie,
retencja, skanowanie danych przez zapytania, transfer i intensywne logowanie.
Retencja to okres przechowywania. Partycjonowanie dzieli dane, np. według daty,
żeby odpowiednie zapytanie mogło pominąć niepotrzebny zakres.

**Dobra logika:** zmierzyć koszt i świeżość, wskazać przyczynę, przetestować zmianę
na reprezentatywnych danych, porównać wynik przy dużym obciążeniu. Nie wymagaj
cen z pamięci. Nie każda redukcja zasobów daje najniższy koszt całej operacji.

> “What would prove that the data is ready for the analyst within 15 minutes?”

## 5. Q2: IAM, KMS i dostęp między kontami

### Najpierw ustal: kto, co, do czego

IAM zarządza tożsamościami i uprawnieniami. Principal to tożsamość wykonująca
żądanie, np. rola aplikacji. Rola / role jest zestawem zasad i uprawnień,
który można przyjąć na sesję. ARN to pełny identyfikator zasobu lub tożsamości.

| Pojęcie | Pytanie, na które odpowiada |
| --- | --- |
| Uwierzytelnienie / authentication | Kim jesteś? |
| Autoryzacja / authorization | Czy możesz wykonać tę operację? |
| Trust policy | Kto może przejąć rolę? |
| Permission policy | Co może zrobić sesja tej roli? |
| Identity policy | Jakie uprawnienia przypisano tożsamości? |
| Resource policy, np. bucket policy | Jaki dostęp dopuszcza polityka zasobu? |
| Least privilege | Czy nadano wyłącznie potrzebne operacje i zakres? |

Allow to pozwolenie, Deny to odmowa. Jawna odmowa w mającej zastosowanie polityce
może zablokować operację mimo Allow w innej. SCP, permissions boundary i polityka
sesji mogą dodatkowo ograniczać uprawnienia; nie są samodzielnym nadaniem dostępu.
[AWS: ocena polityk](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

### Konto analityka a konto platformy

Istnieją dwa różne wzorce: rola z konta analityka czyta dane bezpośrednio albo
analityk przejmuje rolę w koncie platformy. W drugim wzorcu odczyt wykonuje
przejęta rola. Dlatego odpowiedź „sprawdzę IAM” jest niepełna bez wskazania
tożsamości, konkretnego obiektu i operacji, np. odczytu zamiast listowania.

### Dlaczego S3 i KMS to dwa osobne sprawdzenia

KMS zarządza kluczami kryptograficznymi i ich użyciem. Dostęp do zaszyfrowanego
obiektu może wymagać zarówno prawa odczytu S3, jak i prawa użycia odpowiedniego
klucza do odszyfrowania. To jak dostęp do szafki oraz możliwość otwarcia
zamkniętego pojemnika w środku.

Przy bezpośrednim użyciu klucza z innego konta muszą współdziałać polityka KMS
oraz polityka IAM wywołującego. Przejęcie roli zmienia tożsamość do oceny.
Nie wymagaj gotowego JSON polityki z pamięci.
[AWS: KMS między kontami](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html).

Lake Formation może dodawać kontrolę dostępu do danych i katalogu, jeżeli projekt
jej używa. Nie wymagaj jej w architekturze, w której nie jest potrzebna.

**AccessDenied** oznacza odmowę dostępu. Sensowna diagnoza ustala dokładne żądanie,
rolę, zasób i kontekst, a następnie weryfikuje polityki i błąd. Test powinien
odtwarzać odczyt jako rzeczywisty odbiorca. Administrator może przejść test,
który nie powiedzie się użytkownikowi docelowemu.

**Dopytaj przy:** propozycji stałego AdministratorAccess bez wyjaśnienia przyczyny.
Chwilowy krok diagnostyczny i końcowa konfiguracja wymagają odróżnienia.

> “Which identity is making the request, and which operation is denied?”

## 6. Q3: Terraform i bezpieczne zmiany infrastruktury

### Kod, stan i rzeczywistość

Infrastructure as Code / IaC oznacza opisywanie infrastruktury w plikach,
które można przeglądać i wersjonować. Terraform jest jednym z narzędzi.
Deklarujemy pożądany rezultat, np. bucket i rolę, zamiast ręcznie klikać każdy zasób.

**Trzy różne rzeczy:** konfiguracja mówi, co chcemy mieć; state przechowuje
powiązania zarządzanych zasobów z ich obiektami; AWS zawiera rzeczywiste zasoby.
State nie jest kopią zapasową danych przechowywanych w bucketach.
[HashiCorp: cel stanu](https://developer.hashicorp.com/terraform/language/state/purpose).

| Termin | Znaczenie dla prowadzącego |
| --- | --- |
| Provider | Integracja pozwalająca Terraform komunikować się np. z AWS |
| Module | Wspólny zestaw definicji zasobów z parametrami |
| Backend | Miejsce i sposób przechowywania stanu |
| Plan | Propozycja zmian: co powstanie, zmieni się lub zostanie usunięte |
| Apply | Wykonanie zaplanowanych zmian |
| Drift | Różnica między konfiguracją deklarowaną a faktycznym stanem zasobów |
| Locking | Blokada chroniąca przed konfliktującym zapisem/pracą na tym samym stanie |
| Blast radius | Zakres skutków błędu, np. jeden proces albo całe środowisko |

### Droga od PR do produkcji

PR / pull request to propozycja zmiany do przeglądu. Commit jest zapisaną wersją
zmian w Git. Review to ocena przez inną osobę. Sensowny przebieg obejmuje
przegląd kodu, walidację, plan dla właściwego środowiska, akceptację, apply
i weryfikację działania. Kod i dane środowisk muszą mieć jednoznaczny cel wdrożenia.

Wspólny zdalny stan ogranicza ryzyko posiadania różnych lokalnych rejestrów.
W S3 blokowanie jest opcjonalne i wymaga konfiguracji, np. `use_lockfile = true`.
Starsza metoda z DynamoDB jest oznaczona jako deprecated. Poprawny opis starszej
instalacji nadal świadczy o doświadczeniu. Blokada stanu i ustawienie kolejki
wdrożeń w CI to dwa uzupełniające mechanizmy.
[HashiCorp: backend S3](https://developer.hashicorp.com/terraform/language/backend/s3).

Osobne nazwy lub workspaces nie zapewniają same izolacji bezpieczeństwa.
Znaczenie mają również konta, uprawnienia, konfiguracja i oddzielne stany.
Wersje modułów i providerów pomagają powtarzać uzgodnioną konfigurację.
Stary plan może już nie odpowiadać sytuacji po innych zmianach.

### Dlaczego częściowo nieudane apply nie jest transakcją

W pytaniu bucket powstał, a polityka nie. Wykonanie mogło zakończyć część operacji
przed błędem. Cofnięcie commitu zmienia pliki w Git, lecz nie cofa automatycznie
już wykonanych operacji w AWS.

**Rozumowanie, którego szukasz:** ustalić, co powstało, co zapisano w stanie,
jaka była przyczyna błędu i co pokazuje nowy plan; następnie naprawić problem,
chroniąc dane. Import lub ręczna ingerencja w stan są działaniami wymagającymi
konkretnego uzasadnienia, a nie rutynową odpowiedzią na każdy błąd.
[HashiCorp: apply](https://developer.hashicorp.com/terraform/cli/commands/apply).

Jeżeli plan usuwa zasób z danymi, kandydat powinien wstrzymać zmianę i wyjaśnić
powód, środowisko, zależności i możliwość odzyskania danych. Przy ręcznej zmianie
w konsoli trzeba zdecydować, czy zapisać ją w kodzie, czy przywrócić deklarację.

### Sekrety w stanie

Sekret to np. hasło lub token. `sensitive` przede wszystkim ogranicza ujawnianie
wartości w zwykłym wyjściu; samo oznaczenie nie usuwa jej ze stanu i planu.
Należy chronić te pliki. Istnieją odrębne mechanizmy ephemeral/write-only,
których dostępność zależy od zasobu i wersji.
[HashiCorp: dane wrażliwe](https://developer.hashicorp.com/terraform/language/manage-sensitive-data).

> “What already changed in AWS, and what would a new plan show?”

## 7. Q4: CI/CD, OIDC i testy wdrożeniowe

### Co robi pipeline

Pipeline to zautomatyzowana sekwencja działań. CI sprawdza integrowane zmiany;
CD automatyzuje dostarczanie lub wdrażanie zgodnie z przyjętym procesem.
Akceptacja człowieka przed produkcją jest zgodna z takim podejściem.
GitHub Actions jest narzędziem uruchamiającym workflow, czyli opisany proces.

```text
PR -> kontrole kodu i testy -> plan -> przegląd / akceptacja
   -> wdrożenie do test -> test przepływu -> zatwierdzona produkcja
```

Artefakt to wdrażalny wynik pracy, np. paczka kodu Lambdy. Wersja lub digest
pozwala rozpoznać dokładnie ten sam artefakt w kolejnych środowiskach.
Promocja oznacza dopuszczenie sprawdzonej wersji do następnego środowiska.
Konfiguracja i uprawnienia mogą różnić się między testem i produkcją, lecz
powinno być wiadomo, jakie wersje razem działają.

### OIDC bez technicznej magii

OIDC pozwala GitHub przedstawić AWS token potwierdzający tożsamość uruchomienia.
Token nie jest trwałym hasłem. AWS sprawdza warunki zaufania i przez STS może
wydać czasowe poświadczenia roli. Dopiero jej uprawnienia określają dozwolone operacje.

`aud` mówi o odbiorcy tokenu, `sub` identyfikuje jego podmiot/kontekst, np.
repozytorium i kontekst wdrożenia. Ich dokładny format zależy od konfiguracji.
`id-token: write` pozwala pobrać token OIDC; nie daje samo prawa zmieniania AWS.
Ochrona środowiska kontroluje dodatkowo, kto może uruchomić wdrożenie produkcyjne.
[GitHub: OIDC w AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws).

**Cel pytania:** kandydat rozumie, dlaczego inny projekt albo niezaufany kod z PR
nie powinien przejmować roli produkcyjnej. Stałe klucze administratora w CI
wymagają uzasadnienia; nie są naturalnym rezultatem poprawnej konfiguracji OIDC.

### Co naprawdę udowadniają testy

| Rodzaj sprawdzenia | Co potwierdza | Czego samo nie dowodzi |
| --- | --- | --- |
| Walidacja / lint | Poprawność określonych reguł kodu lub konfiguracji | Poprawnych uprawnień odbiorcy w AWS |
| Test jednostkowy | Zachowanie fragmentu logiki przy kontrolowanym wejściu | Działania prawdziwej usługi i sieci |
| Mock / fake | Zastępuje usługę kontrolowaną odpowiedzią w teście | Zgodności rzeczywistej konfiguracji AWS |
| Test integracyjny | Współdziałanie rzeczywistych komponentów | Całej ścieżki użytkownika, jeśli test obejmuje tylko część |
| Test end-to-end | Przejście danych od wejścia do oczekiwanego wyniku | Wszystkich możliwych przypadków i obciążeń |
| Test negatywny | Właściwe odrzucenie zabronionej operacji | Niczego, jeśli błąd wynikał np. ze złej nazwy pliku |

pytest to narzędzie do uruchamiania testów Pythona, nie opis ich zakresu.
Fixture to przygotowane dane lub środowisko testowe. Pytaj, jaką tożsamością
wykonano operację, jakie wejście podano i co porównano z oczekiwanym wynikiem.

**Przykład dobrego testu:** rola analityka odczytuje dozwolony zaszyfrowany obiekt,
a próba odczytu niedozwolonego zbioru daje oczekiwaną odmowę uprawnień.

Przy nieudanej integracji zatrzymujemy promocję. Rollback to powrót do poprzedniej
wersji; fix-forward to wdrożenie poprawki. Odwrócenie infrastruktury nie musi
odtworzyć usuniętych danych lub cofnąć już zapisanych błędnych wyników.

> “Which behaviour does the test verify, and under which identity?”

## 8. Q5: jak zrozumieć pierwsze zadanie Python

### Najpierw przeczytaj składnię

`def` definiuje funkcję. `jobs` jest jej wejściem: listą rekordów. Rekord to tutaj
słownik z polami `name` i `status`. `for` przechodzi po rekordach, `if` sprawdza
warunek, `==` porównuje wartości, a `append` dopisuje element do listy.
`return` kończy całe wywołanie funkcji i zwraca wynik. Wcięcia określają,
które instrukcje należą do pętli lub warunku.

**Cel:** każde wywołanie ma zwrócić wyłącznie własne nazwy błędnych zadań.

```python
def failed_jobs(jobs, failed=[]):
    for job in jobs:
        if job["status"] == "FAILED":
            failed.append(job["name"])
        return failed
```

### Błąd 1: zakończenie po pierwszym rekordzie

W arkuszu pierwszy rekord to `load_customers / SUCCEEDED`. Warunek jest fałszywy,
więc nic nie dopisujemy. Następnie wykonuje się `return`, nadal wewnątrz pętli.
Przy świeżej definicji wynik to `[]`; dwa późniejsze błędy nie są sprawdzane.
Puste wejście nie uruchamia pętli, więc funkcja dochodzi do końca i zwraca `None`.

`[]` oznacza pustą listę wyników. `None` jest osobną wartością oznaczającą brak
takiej wartości wyniku. Nie są tym samym dla programu, który oczekuje listy.

### Błąd 2: jedna lista domyślna dla kolejnych wywołań

Wartość `failed=[]` powstaje przy definiowaniu funkcji. Gdy wywołujący pomija
drugi argument, kolejne wywołania używają tej samej listy. `append` ją zmienia.
Mutowalny oznacza „możliwy do zmiany w miejscu”. Samo czytanie listy nie powoduje
tej akumulacji; tutaj powoduje ją dopisywanie.
[Python: wartości domyślne](https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects).

Po przesunięciu wyłącznie return poza pętlę, przy świeżej definicji i natychmiastowym
wypisywaniu kolejnych wyników:

| Wywołanie | Wynik |
| --- | --- |
| Pierwsze dla danych z arkusza | `["load_orders", "load_products"]` |
| Drugie dla tych samych danych | `["load_orders", "load_products", "load_orders", "load_products"]` |
| Następnie dla pustej listy | Nadal te cztery stare nazwy |

Pierwotne złe wcięcie ukrywa ten efekt w przykładzie, bo pierwszy rekord jest
udany. Dlatego pytanie o kolejne wywołania pada po naprawie wcięcia.
Oba wyniki odnoszą się do tej samej listy: zachowany pierwszy wynik też się zmieni
po drugim wywołaniu. To dodatkowy szczegół o współdzieleniu obiektu.

### Najprostsza pełna poprawka

```python
def failed_jobs(jobs):
    failed = []
    for job in jobs:
        if job["status"] == "FAILED":
            failed.append(job["name"])
    return failed
```

Teraz każde wywołanie ma nową listę, a return następuje po całej pętli.
Puste wejście i same sukcesy dają `[]`, także po wcześniejszych błędach.
Akceptuj ustne wyjaśnienie; nie wymagaj przepisywania kodu. Kandydat powinien
wyjaśnić oba błędy, nie tylko nazwać regułę o argumentach domyślnych.

> “When is that list created, and does the next call use the same list?”

## 9. Q5: jak zrozumieć drugie zadanie Python

**Cel:** wybrać tylko statusy `FAILED` i `TIMED_OUT`. Arkusz zawiera też
`SUCCEEDED` i `CANCELLED`, które mają być pominięte.

```python
def retryable_jobs(jobs):
    retryable = []
    for job in jobs:
        if job["status"] == "FAILED" or "TIMED_OUT":
            retryable.append(job["name"])
    return retryable
```

### Dlaczego warunek wpuszcza wszystkie rekordy

Python odczytuje tu dwie części: porównanie `job["status"] == "FAILED"`
oraz sam napis `"TIMED_OUT"`. Nie dopisuje drugiego porównania automatycznie.
Niepusty napis jest traktowany jako prawda przy sprawdzaniu warunku.

Gdy status to FAILED, lewa część wystarcza. Gdy to SUCCEEDED lub CANCELLED,
lewa część jest fałszywa, lecz prawa nadal ma prawdziwość niepustego napisu.
W rezultacie wybieramy każdą nazwę.
[Python: prawdziwość i operator or](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).

| Wariant | Wynik dla czterech rekordów z arkusza |
| --- | --- |
| Oryginalny kod | load_customers, load_orders, load_products, load_prices |
| Poprawna logika | load_orders, load_products |

### Dwie czytelne poprawki warunku

```python
if job["status"] in ("FAILED", "TIMED_OUT"):
```

`in` pyta, czy status należy do podanego zbioru dopuszczonych wartości.
Równoważny wariant to dwa pełne porównania:

```python
if job["status"] == "FAILED" or job["status"] == "TIMED_OUT":
```

Sama zamiana `or` na `and` nie naprawi wymaganej logiki. Do sprawdzenia wystarczą
mieszane statusy, oba statusy dopuszczone, oba pomijane i pusta lista.
Nie wymagaj pisania testów ani mechanizmu rzeczywistych ponowień.

**Co oceniasz:** czy kandydat rozumie działanie kodu, przewiduje skutek i potrafi
zaproponować poprawkę. Dodatkowy atut to wiedza, że `or` oblicza tylko potrzebną
część i zwraca operand; nie trzeba pytać o to w tym krótkim zadaniu.

> “Does the string on the right compare itself to the status?”

## 10. Q5: automatyzacja, błędy i testy w realnym projekcie

### Dlaczego pytamy jeszcze o doświadczenie

Znalezienie błędu w kilku liniach nie dowodzi samodzielnego wdrażania automatyzacji.
Poproś o skrypt lub Lambdę: wejście, operację, wynik, przewidywane błędy
i sposób sprawdzenia. Sama lista bibliotek nie opisuje wykonanej pracy.

Exception / wyjątek sygnalizuje problem w kodzie lub wywołaniu. Obsłużenie wyjątku
powinno prowadzić do świadomej reakcji. Zapisanie błędu i zgłoszenie pełnego sukcesu
może ukryć awarię. Structured logging oznacza zapisywanie informacji w polach,
np. identyfikator uruchomienia, obiekt i rodzaj błędu, aby łatwiej je wyszukiwać.

### Częściowy sukces i timeout

Jeśli z dziesięciu plików osiem się skopiowało, potrzebujemy wiedzieć, które dwa
nie. Inaczej operator nie potrafi bezpiecznie dokończyć pracy. Timeout oznacza,
że nie otrzymaliśmy odpowiedzi w oczekiwanym czasie. Operacja po drugiej stronie
mogła się jednak zakończyć. Bezmyślne ponowienie może stworzyć podwójny efekt.

Retry to ponowienie. Backoff to zwiększanie przerwy między próbami, jitter dodaje
losowe rozproszenie. Te mechanizmy ograniczają przeciążenie, ale same nie
gwarantują bezpieczeństwa skutku biznesowego. Do tego wraca pytanie o idempotencję.

**Przykład sensownej odpowiedzi:** kandydat opisuje konkretny błąd API, wskazuje
go w wyniku/logach, sprawdza reakcję przy kontrolowanym błędzie oraz testuje
rzeczywistą konfigurację integracyjną. Nie każdy test musi kontaktować się z AWS.

> “How could the operator tell which work succeeded and which work failed?”

## 11. Q6: brak nowych danych i obserwowalność

### Co znaczy „CI zielone, a raport nieaktualny”

Zielone CI potwierdza sukces uruchomionych kontroli. Zakres tych kontroli może
nie obejmować całej drogi danych. Plik w S3 potwierdza jedynie dotarcie do
jednego etapu. Brak błędów Lambdy może oznaczać, że funkcja nie była wywołana.

Obserwowalność / observability to możliwość zrozumienia działania systemu
na podstawie jego sygnałów. Log zapisuje zdarzenie, metryka mierzy wartość
w czasie, alarm powiadamia o warunku, a korelacja łączy sygnały z tą samą operacją.
CloudWatch służy m.in. logom, metrykom i alarmom; CloudTrail zapisuje aktywność
API dla obsługiwanych zdarzeń, zależnie od konfiguracji. Nie zakładaj, że zapisuje
automatycznie każdy potrzebny odczyt danych.

### Jak ma wyglądać diagnoza

| Etap sprawdzenia | Jakie pytanie rozstrzyga | Przykładowy dowód |
| --- | --- | --- |
| Wpływ i ostatni sukces | Co jest nieaktualne i od kiedy? | Czas ostatniej poprawnej publikacji i dotknięty zbiór |
| Wejście i zdarzenie | Czy plik uruchomił dalszą pracę? | Konkretny obiekt i wiadomość |
| Kolejka | Czy praca czeka i jak długo? | Rosnąca zaległość, wiek wiadomości, DLQ |
| Przetwarzanie | Czy proces ruszył i jaki był wynik? | Uruchomienie, logi, błąd, zapis wyjścia |
| Odbiorca | Czy raport czyta właściwy, świeży wynik? | Odczyt lub zapytanie jako odbiorca |

Hipoteza to możliwe wyjaśnienie, root cause to ustalona przyczyna.
Kandydat powinien powiedzieć, jaka obserwacja potwierdzi lub odrzuci hipotezę,
np. czy po wdrożeniu zniknęły wywołania mimo przychodzących wiadomości.
Nie musi wymieniać wszystkich usług naraz.

**Dobra kolejność:** określić wpływ, prześledzić znane wejście, znaleźć zatrzymany
etap, sprawdzić ostatnią zmianę, ograniczyć dalsze skutki i potwierdzić naprawę.
Sam restart bez zrozumienia może tylko odsunąć albo powtórzyć problem.

> “Which observation would confirm or reject your hypothesis?”

## 12. Q6: kolejki, duplikaty i bezpieczne ponowienia

### Co robi kolejka

Wiadomość to informacja o pracy, np. „przetwórz plik X”. SQS przechowuje ją,
zanim odbiorca zakończy obsługę. W integracji SQS z Lambdą mechanizm źródła
zdarzeń pobiera wiadomości i wywołuje funkcję, często z paczką / batch.

Wiadomość może być przetwarzana więcej niż raz. Visibility timeout to czas,
przez który pobrana wiadomość jest ukryta przed kolejnymi odbiorami; nie jest
tym samym co limit czasu działania funkcji. Po niepowodzeniu może znów być
dostępna. Zbyt krótki czas względem przetwarzania zwiększa ryzyko ponownej obsługi.
[AWS: Lambda z SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

### Idempotencja: powtórzenie bez podwójnego skutku

Wyobraź sobie zamówienie `123` wysłane dwa razy. Wstawienie go drugi raz jako
nowej sprzedaży zawyży raport. Bezpieczny zapis może rozpoznawać ten sam
identyfikator i zastępować/uzgadniać ten sam wynik, zamiast dopisywać drugi.
Alternatywnie proces trwale śledzi zakończenie danej operacji.

Pamięć pojedynczego procesu, np. globalny zbiór w Pythonie, nie wystarcza przy
restartach i wielu wykonaniach. Trwały magazyn, np. baza, musi również radzić
sobie z równoczesnymi próbami i awarią między zapisem efektu a oznaczeniem sukcesu.
Samo „zapiszę identyfikator w DynamoDB” wymaga wyjaśnienia tego momentu.
Pełny protokół rozproszony jest dodatkową głębią, nie wymogiem podstawowym.

### Jedna zła wiadomość w paczce

Domyślna obsługa błędu paczki może powodować ponowienia także udanych rekordów.
Partial batch response pozwala wskazać nieudane rekordy, ale wymaga odpowiedniej
konfiguracji źródła i zachowania kodu. Nieobsłużony wyjątek nadal może oznaczać
niepowodzenie całej paczki. Przy FIFO trzeba zachować wymagania kolejności.
[AWS: błędy i częściowe odpowiedzi](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html).

DLQ / dead-letter queue to wydzielona kolejka dla wiadomości nieskutecznie
obsługiwanych po ustalonej liczbie prób, jeśli taki mechanizm skonfigurowano.
Nie naprawia danych automatycznie. Potrzebuje alarmu, właściciela, diagnozy
i zasad kontrolowanego ponowienia. Dla SQS sprawdzaj konfigurację kolejki;
nie myl jej z innymi mechanizmami błędów wywołań Lambdy.

> “What if processing succeeded, but recording completion failed?”

## 13. Q6: prywatne podsieci, DNS, NAT i endpointy

### Sieć i uprawnienia to odrębne warstwy

Sieć odpowiada za dotarcie żądania do celu. IAM odpowiada za zgodę na operację.
Timeout zwykle kieruje diagnozę najpierw ku łączności, ale jest objawem, nie
jednoznacznym dowodem przyczyny. AccessDenied wskazuje odmowę, którą trzeba
rozpatrzyć w kontekście usługi, tożsamości i obowiązujących polityk.

| Termin | Proste objaśnienie |
| --- | --- |
| VPC | Własna logiczna sieć w AWS |
| Subnet / podsieć | Wydzielony fragment tej sieci |
| Route table / tablica tras | Reguły mówiące, którędy wysyłać ruch |
| DNS | Tłumaczy nazwę usługi na adres sieciowy |
| Security group | Reguły dopuszczania ruchu przy powiązanych interfejsach/zasobach |
| Network ACL | Dodatkowe reguły filtrowania na poziomie podsieci |
| NAT | Umożliwia odpowiednio skonfigurowany ruch wychodzący do publicznych celów |
| VPC endpoint | Prywatna droga do obsługiwanej usługi, bez wymagania wyjścia przez publiczny internet |

### Dlaczego „przenieśmy do publicznej podsieci” nie wystarcza

Publiczna podsieć ma odpowiednią drogę do internet gateway, lecz samo podłączenie
do niej Lambdy nie daje funkcji automatycznie publicznego adresu i internetu.
Prywatne podsieci mogą mieć wyjście przez właściwie skonfigurowany NAT.
Jeżeli potrzebujemy wyłącznie obsługiwanych usług AWS, odpowiednie endpointy
mogą wystarczyć.
[AWS: internet dla Lambdy w VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-internet.html).

Dla S3 popularnym wariantem jest gateway endpoint powiązany z tablicami tras.
Secrets Manager może używać interface endpointu, którego dostęp zależy m.in.
od security groups i prywatnego DNS. Endpoint policy może ograniczać operacje;
sama prywatna droga nie nadaje automatycznie uprawnień do danych.
[AWS: gateway endpoint S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html),
[AWS: endpoint Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

**Czego słuchasz:** kandydat najpierw ustala cel wywołania i błąd, potem sprawdza
DNS, trasy, reguły i właściwą drogę. Nie dodaje w ciemno uprawnień IAM ani NAT
do każdej sytuacji. Dokładne polecenia diagnostyczne nie są wymagane.

> “Which service are you trying to reach, and what network path should it use?”

## 14. Q6: odzyskanie danych, monitoring i komunikacja

### Co znaczy „naprawione”

Usługa może już działać, a dane z czasu awarii nadal być niepełne.
Backlog to zaległa praca. Odtworzenie wymaga wskazania dotkniętego zakresu,
bezpiecznego ponowienia, kontroli tempa oraz porównania oczekiwanych i uzyskanych
wyników. Należy też sprawdzić, czy bieżąca praca i backfill nie nadpisują się błędnie.

Freshness / świeżość to aktualność danych względem uzgodnionego punktu i harmonogramu.
Completeness / kompletność oznacza obecność oczekiwanego zakresu.
Jeżeli dostawca niczego nie przysłał, brak nowego wyniku może być poprawny;
jeżeli plik jest, a wynik nie powstał, sytuacja jest inna. Sukces zadania
z zerową liczbą użytecznych rekordów nie zawsze oznacza sukces biznesowy.

SLO to mierzalny cel działania, np. świeżość danych. SLA to uzgodnienie dotyczące
poziomu usługi. W naszym pytaniu 15 minut jest celem scenariusza. Runbook to
instrukcja rozpoznania problemu i reakcji. Alarm potrzebuje osoby lub zespołu,
który go odbierze i podejmie działanie.

### Jak rozpoznać dobry komunikat o incydencie

Powinien zawierać wpływ, potwierdzone fakty, niepewności, kolejne działania
i czas następnej aktualizacji. ETA to przewidywany czas przywrócenia;
nie należy go wymyślać, gdy brak podstaw.

> „Raport jest nieaktualny od 40 minut. Pliki nadal trafiają do S3. Sprawdzamy
> etap przetwarzania po ostatniej zmianie. Przyczyna nie jest jeszcze potwierdzona.
> Kolejny status przekażemy za 15 minut.”

To obietnica aktualizacji, nie naprawy w 15 minut. Podczas rozmowy kandydat
przekazuje tę informację po angielsku, prostym językiem dla odbiorcy biznesowego.

GxP to zbiorcze określenie praktyk jakościowych w regulowanych obszarach.
W tym interview liczy się faktyczny change management: przegląd, testy, akceptacja
i dowody. Pilna zmiana powinna korzystać z uzgodnionej ścieżki awaryjnej.
Szczegółowe wymagania wynikają z procedur organizacji i zastosowania;
nie wymagaj od kandydata uniwersalnej reguły GxP.

> “How will you prove the backlog is recovered and the report is complete?”

## 15. Rezerwa: CloudFormation, Docker, SQL, logowanie i hasło w Git

### Przekazanie zasobu z CloudFormation do Terraform

CloudFormation jest innym narzędziem IaC; stack to zarządzany przez niego zestaw
zasobów. Przekazanie zarządzania to zmiana narzędzia odpowiedzialnego za istniejący
zasób. Nie chcemy przypadkowo stworzyć drugiego ani usunąć pierwszego.

Kandydat powinien sprawdzić zależności i zachowanie przy usuwaniu z definicji,
zadbać o zachowanie fizycznego zasobu, przygotować zgodną konfigurację Terraform,
zaimportować zasób i obejrzeć plan. Retain pozwala zachować zasób w odpowiednich
operacjach CloudFormation. Zastąpienia zasobów wymagają osobnego rozważenia,
m.in. UpdateReplacePolicy. Sama deklaracja Retain nie rozwiązuje każdego scenariusza.
[AWS: DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html).

Import wiąże istniejący zasób ze stanem Terraform. Nie gwarantuje automatycznie,
że konfiguracja odpowiada rzeczywistości i kolejny apply niczego nie zmieni.
Sekwencja zależy od zasobu, zależności i możliwości importu. Docelowo powinien
istnieć jeden uzgodniony właściciel zarządzania.
[HashiCorp: import](https://developer.hashicorp.com/terraform/language/import).

### Docker: obraz i uruchomiony kontener

Image / obraz to pakiet aplikacji i zależności. Container / kontener to jego
uruchomiona instancja z konkretną konfiguracją. Kontenery pomagają powtarzać
środowisko wykonania; nadal mogą mieć złe hasło, brak sieci lub za mało pamięci.
[Docker: podstawy](https://docs.docker.com/get-started/docker-overview/).

Przy awarii pytaj o status zakończenia, logi, wersję obrazu, polecenie, konfigurację,
sekrety, zasoby i zależności. Samo ponawianie restartów nie wyjaśnia przyczyny.
Kubernetes zarządza uruchamianiem kontenerów na większą skalę, lecz nie jest
obowiązkowym tematem w tej rozmowie.

### SQL: dlaczego równe liczby wierszy nie wystarczają

Załóżmy, że system A zawiera identyfikatory 1 i 2, a B identyfikatory 1 i 3.
Oba mają dwa wiersze, lecz zawartość się różni. Trzeba uzgodnić to samo okno czasu,
filtry i klucz biznesowy, a następnie sprawdzić braki, duplikaty i wartości.

JOIN łączy rekordy według warunku, GROUP BY grupuje je np. po kluczu do policzenia
wystąpień. NULL oznacza brak/nieznaną wartość i wymaga świadomej obsługi w porównaniu.
DISTINCT usuwa powtórzenia z wyniku; użyty bez wyjaśnienia może ukryć duplikaty.
[PostgreSQL: złączenia i grupowanie](https://www.postgresql.org/docs/current/queries-table-expressions.html).

**Przykład dobrej odpowiedzi:** porównanie grupowanych liczności po kluczu,
brakujących identyfikatorów i istotnych pól, z uwzględnieniem spóźnionych danych
oraz różnic typów. Nie wymagaj jednej konkretnej składni zapytania.

### Porównanie kosztów logowania S3

Logi operacyjne odpowiadają na inne pytania niż ślad audytowy czy metryki.
Kandydat powinien zacząć od potrzeb użytkowników: co chcemy znaleźć, za jaki
okres, jak szybko i jak dokładnie. Następnie porównać odbiór, retencję, zapytania,
obsługę i koszt. Analiza z rekomendacją jest innym wynikiem niż wdrożony system.
Nie zakładaj oszczędności lub wdrożenia tylko na podstawie nazwy usługi w CV.

### R8: hasło do bazy trafiło do GitHub - pytanie rezerwowe

Użyj, gdy kandydat nie zna innego tematu albo odpowiada szybko. Pytanie zajmuje
2-4 minuty i nie wymaga kodowania. Zapisz lukę w pominiętym obszarze osobno:
odpowiedź o sekretach nie potwierdza znajomości Terraform lub Pythona.

> “You discover that a database password was committed to a GitHub repository
> used by an AWS data pipeline. A teammate removes it in a new commit and says
> the problem is solved. Do you agree? What would you do next, and how would
> you check that the pipeline still works?”

**Pojęcia:** sekret to poufna wartość umożliwiająca dostęp, np. hasło. Commit
jest zapisem wersji kodu, więc kolejny commit nie usuwa poprzedniej historii.
Rotacja oznacza zmianę poświadczenia; dla bazy trzeba uzgodnić faktyczne hasło,
jego zapis w magazynie sekretów i użycie przez aplikację.

Samo usunięcie wartości z aktualnego pliku nie wystarcza. Kandydat powinien
traktować poświadczenie jako ujawnione, zaangażować właściwych właścicieli,
unieważnić je lub przeprowadzić rotację oraz sprawdzić działanie odbiorców.
Czyszczenie historii jest osobnym, koordynowanym działaniem; nie zastępuje
unieważnienia hasła i nie daje pewności usunięcia wszystkich kopii.
[GitHub: ujawnione sekrety](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

**Dowód naprawy:** stare poświadczenie nie umożliwia nowego logowania,
właściwy job używa nowego i wykonuje oczekiwaną operację, a wynik danych
dociera do odbiorcy. Ocena aktywnych sesji i dalszych skutków wymaga procedury
danego systemu. Wartości hasła nie powinny trafiać do logów testu.

**Jedno dopytanie:** “The value in Secrets Manager was updated, but the job
still fails. What would you check?”

Słuchaj o zgodności z bazą, poprawnej referencji/wersji sekretu, cache
i rzeczywistym błędzie. Sam zapis nowej wartości nie gwarantuje zmiany hasła
w bazie. [AWS: rotacja](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

Szczegóły, możliwe odpowiedzi i ściąga są w [osobnym przewodniku R8](r8_sekret_w_git_przewodnik_scenariusze_pl.md).

## 16. Rezerwa: migracja S3 i rotacja kluczy IAM

### Migracja: historia, bieżące zapisy i przełączenie

Replikacja kopiuje dane według ustalonych reguł. Bieżąca replikacja S3 nie
przenosi automatycznie wszystkich obiektów istniejących przed jej włączeniem.
Historia może wymagać oddzielnego transferu, np. Batch Replication tam, gdzie
spełnione są wymagania. Wersjonowanie pozwala rozróżniać wersje obiektu;
trzeba uzgodnić, czy migrujemy tylko aktualne, czy też historyczne.
[AWS: zakres replikacji](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-what-is-isnot-replicated.html).

Cutover to przełączenie odbiorców na nowe miejsce. Jeśli źródło nadal przyjmuje
zapisy, potrzebny jest plan nadrobienia zmian lub punkt odcięcia. Walidacja
powinna obejmować tożsamość obiektów, uzgodnioną integralność, raport błędów
oraz odczyt jako właściwy odbiorca, także dla szyfrowania.

ETag jest identyfikatorem w metadanych obiektu, którego znaczenie zależy od sposobu
utworzenia i szyfrowania. Nie wolno zawsze traktować go jak MD5 zawartości.
Równe liczby obiektów również nie dowodzą równości zbiorów.
[AWS: Object i ETag](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Object.html).

### Trzy różne rodzaje „klucza”

| Nazwa | Znaczenie |
| --- | --- |
| S3 object key | Nazwa/identyfikator obiektu w bucketcie |
| KMS key | Klucz kryptograficzny używany przy szyfrowaniu |
| IAM access key | Poświadczenie do programowego uwierzytelnienia żądań |

Rotacja IAM access key nie jest tym samym co rotacja klucza KMS.
Secrets Manager przechowuje sekrety i może wspierać ich rotację; odbiorca musi
rzeczywiście pobrać i zacząć używać nowej wartości.

### Po co pytać o awarię w połowie rotacji

Długoterminowy klucz IAM składa się z identyfikatora i sekretu. Sekret można
otrzymać przy utworzeniu; później nie da się go odczytać ponownie z IAM.
Na użytkownika przypada limit dwóch kluczy, także gdy jeden jest nieaktywny.
Role i poświadczenia tymczasowe powinny być rozważone przed takim wyjątkiem.
[AWS: klucze IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

W normalnym przebiegu tworzymy nowy klucz, bezpiecznie go zapisujemy, aktualizujemy
odbiorców, sprawdzamy ich operacje, dezaktywujemy stary i po uzgodnionej kontroli
usuwamy go. Okres przejściowy zależy od sposobu odświeżania sekretu przez odbiorców.

Jeśli proces zatrzyma się przed zapisem sekretu, trzeba rozpoznać stan rozpoczętej
rotacji i ewentualny osierocony klucz. Ślepe tworzenie kolejnego może wyczerpać
limit. Usuwanie też wymaga sprawdzenia, czy inna próba lub odbiorca już go nie używa.
To pytanie sprawdza myślenie o częściowych awariach i współbieżności.

`GetCallerIdentity` z STS zwraca tożsamość wywołującego. Nie dowodzi, że ta
tożsamość ma dostęp do konkretnego obiektu S3. Potrzebny jest test zamierzonej operacji.
[AWS: GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html).

## 17. Jak oceniać odpowiedzi, gdy sam nie jesteś DevOpsem

### Szukaj związku przyczynowego i dowodu

| Usłyszysz | Co warto doprecyzować |
| --- | --- |
| „Użyłbym Glue” | Jakie wymaganie sprawia, że pasuje? |
| „Sprawdzę IAM” | Jaką tożsamość, operację, zasób i politykę? |
| „Uruchomię ponownie” | Co już się wykonało i czy powtórzenie jest bezpieczne? |
| „Mamy testy” | Jakie zachowanie testują, na jakich danych i jaką rolą? |
| „Problem naprawiony” | Jaki wynik dla odbiorcy to potwierdza? |
| „Nie pamiętam dokładnej opcji” | Czy rozumie mechanizm i potrafi znaleźć szczegół w dokumentacji? |

Poziom regular/mid oznacza samodzielne radzenie sobie z typowym zadaniem,
rozpoznanie częstych błędów i sprawdzenie efektu. Szczegółowa obsługa rzadkich
awarii i złożonych kompromisów jest dodatkowym dowodem większej głębi.

Zapisuj, czy odpowiedź przyszła samodzielnie, po neutralnym doprecyzowaniu,
czy po wskazaniu mechanizmu przez prowadzącego. Nie oceniaj jedynie podobieństwa
do przykładowych zdań. Alternatywna architektura może być poprawna.

N/O oznacza „nie oceniono”, a nie brak umiejętności. Jeśli nie rozumiesz
technicznego wariantu na tyle, by go rozstrzygnąć, zapisz go do konsultacji.
Utrzymujące się nieporozumienie oceniaj przez konkretny skutek, np. duplikację
danych lub nieuprawniony dostęp.

### Kontrola własnego przygotowania

Przed rozmową spróbuj własnymi słowami wyjaśnić sześć zdań:

1. Plik w S3 nie oznacza jeszcze świeżego raportu.
2. Tożsamość i uprawnienia to różne rzeczy; szyfrowanie może dodać warunek KMS.
3. Cofnięcie kodu nie cofa automatycznie zmian infrastruktury.
4. Zielony pipeline potwierdza zakres wykonanych testów.
5. Powtórzenie operacji może wymagać ochrony przed podwójnym efektem.
6. Naprawa obejmuje też zaległe dane i weryfikację wyniku odbiorcy.

Komunikację oceniaj przez całą rozmowę po angielsku: jasność, zrozumienie
dopytań i wyjaśnienie wpływu. Akcent lub pojedynczy błąd gramatyczny nie
powinny przesłaniać poprawnego rozumowania.

## 18. Słownik i materiały do powtórki

### Najczęstsze skróty i wyrażenia

| Termin | Znaczenie w tej rozmowie |
| --- | --- |
| Artifact / artefakt | Wersjonowany pakiet lub plik przygotowany do wdrożenia |
| Audit trail | Ślad pozwalający odtworzyć, kto i kiedy wykonał zmianę |
| Backfill | Uzupełnienie lub przeliczenie historycznego zakresu |
| Backlog | Praca, która czeka na wykonanie |
| Batch | Paczka rekordów przetwarzanych w jednym wywołaniu |
| Boundary / granica | Ograniczenie zakresu dostępu albo odpowiedzialności |
| Concurrency | Równoczesne wykonywanie operacji |
| Credentials | Poświadczenia używane do uwierzytelnienia |
| Curated / raw | Dane przygotowane / zachowane dane źródłowe |
| Cutover | Przełączenie odbiorców na nowe rozwiązanie |
| Data Catalog / metadata | Opis danych i ich lokalizacji |
| Digest | Skrót pozwalający identyfikować konkretną zawartość artefaktu |
| DLQ | Kolejka dla wiadomości nieobsłużonych po ustalonych próbach |
| Drift | Rozbieżność deklarowanej i rzeczywistej konfiguracji |
| ETL / ELT | Odczyt, przekształcenie i zapis / odczyt, zapis i przekształcenie |
| Fixture / mock | Przygotowane dane/środowisko testu / kontrolowany zastępnik usługi |
| Freshness / completeness | Świeżość / kompletność danych |
| Idempotency | Powtórzenie nie powoduje dodatkowego niezamierzonego skutku |
| Integration / end-to-end | Współdziałanie komponentów / sprawdzenie całej ścieżki |
| Least privilege | Najmniejszy potrzebny zakres uprawnień |
| OIDC / STS | Protokół potwierdzenia tożsamości / usługa AWS m.in. dla sesji tymczasowych |
| Orchestration | Koordynacja kroków, zależności i ich wyników |
| Partial failure | Niepowodzenie części operacji przy sukcesie pozostałych |
| PR / review | Propozycja zmiany / jej przegląd |
| Reconciliation | Uzgodnienie oczekiwanych i otrzymanych danych lub stanu |
| Replay / retry | Odtworzenie określonej pracy / ponowienie próby |
| Rollback / fix-forward | Powrót do wcześniejszej wersji / wdrożenie poprawki |
| Runbook | Instrukcja diagnozy i reakcji operacyjnej |
| Schema / validation | Opis struktury / sprawdzenie zgodności i reguł |
| State / locking | Rejestr zarządzanych zasobów / ochrona przed konfliktem pracy na nim |
| Throttling | Ograniczenie tempa wywołań przez usługę |
| Timeout | Przekroczenie oczekiwanego czasu odpowiedzi lub wykonania |
| Trust policy | Zasady określające, kto może przejąć rolę |
| Unit test | Test wydzielonego fragmentu logiki |
| Versioning | Rozróżnianie i zachowanie wersji kodu lub danych |

### Jak czytać ten materiał razem z pozostałymi

[Plan rozmowy](data_platform_engineer_devops_60min_pl.md) określa pytania i czas.
[Arkusz kandydata](zadanie_python_dla_kandydata_pl.md) zawiera oba zadania bez odpowiedzi.
[Klucz odpowiedzi](example_answers_aws_data_platform_devops_pl.md) podaje przykłady
i kalibrację poziomu. Ten przewodnik tłumaczy mechanizmy, żeby pytania były
zrozumiałe dla prowadzącego.

Linki przy rozdziałach prowadzą do oficjalnej dokumentacji. Szczegóły produktów
zweryfikowano 17 października 2026. Limity, wersje i możliwości konfiguracji
należy sprawdzać dla rzeczywiście używanego środowiska.
