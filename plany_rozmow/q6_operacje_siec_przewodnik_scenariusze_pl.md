# Q6: incydenty, sieć i komunikacja

Jak rozumieć pytanie, rozpoznawać scenariusze i oceniać odpowiedzi

**Data Platform Engineer / AWS DevOps · przewodnik po polsku · 17 października 2026**

Materiał dla prowadzącego bez praktyki DevOps. Pokazuje, jak odróżnić brak
wywołania od błędu przetwarzania, jak bezpiecznie wznowić zaległe dane i jak
rozmawiać o problemach sieciowych oraz wpływie na biznes.
Pytania do kandydata są po angielsku.

Q6 ma 11 minut: 4 na diagnozę, 3 na odzyskanie danych i monitoring,
2 na sieć oraz 2 na komunikację. Poniższe scenariusze to przygotowanie
prowadzącego, nie obowiązek omówienia wszystkich gałęzi podczas rozmowy.
Przykłady są dydaktyczne, nie opisują potwierdzonej platformy firmy.

**Najważniejsze:** diagnoza powinna prowadzić od obserwacji do sprawdzonej
hipotezy, a przywrócenie usługi także do poprawnych i kompletnych danych.

## 1. Pytanie główne i czego ma dowieść

> “Return to your design from Q2, or assume S3 to SQS to Lambda to a reporting
> dataset. After a deployment, CI is green and new files arrive in S3, but the
> report has had no new data for 40 minutes. What are your first three checks?
> What evidence would confirm or reject your leading hypothesis?”

Po polsku: pliki przychodzą, wdrożenie jest zielone, ale użytkownik nie widzi
nowych danych. Kandydat ma znaleźć miejsce, w którym przepływ się zatrzymał,
i potwierdzić przyczynę dowodami.

Nie ma jednej wymaganej kolejności nazw usług. Oceniasz uporządkowanie,
świadomość wpływu i zdolność odrzucenia własnego pierwszego pomysłu.
„Sprawdzę logi” jest początkiem, nie pełną odpowiedzią: które logi i czego szuka?

Jeśli kandydat zaprojektował inną poprawną platformę w Q2, pozwól diagnozować
ją. SQS i Lambda są wariantem pomocniczym, a nie powodem zmiany reguł w połowie rozmowy.

## 2. Podstawy: co robi każdy element przepływu

| Element | Rola | Co może pójść źle |
| --- | --- | --- |
| S3 | Przechowuje pliki wejściowe i ewentualnie wynikowe | Inny prefix, niewłaściwa wersja, brak zdarzenia |
| SQS | Buforuje wiadomości o pracy do wykonania | Rośnie zaległość albo wiadomości stale wracają |
| Lambda | Przetwarza wiadomości i uruchamia logikę | Błąd kodu, dostępu, timeout lub brak wywołań |
| Dataset | Przygotowany zbiór dla odbiorcy | Zły schemat, brak partycji, niepełny lub błędny wynik |
| Raport | Odczytuje przygotowane dane | Czyta stary zakres, stary wynik lub pamięć podręczną |

Wiadomość SQS jest zleceniem lub opisem zdarzenia; zwykle nie całym dużym
plikiem. Lambda z integracją SQS jest wywoływana przez mechanizm odczytujący
kolejkę. Warto wiedzieć, czy w ogóle dostaje wiadomości.
[AWS: Lambda z SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

Zielone CI potwierdza wynik określonych kroków wdrożenia. Nie dowodzi, że
dzisiejsze pliki dotarły do raportu. Brak błędów Lambdy może oznaczać brak
wywołań, a nie poprawne działanie.

> “If Lambda shows no errors, what else would you check before calling it healthy?”

Oczekuj sprawdzenia wywołań, danych wejściowych i wyniku widzianego przez odbiorcę.

## 3. Dobre pierwsze trzy sprawdzenia

Możliwa dobra odpowiedź, bez wymagania identycznej numeracji:

1. **Wpływ i oś czasu:** które raporty lub zbiory są nieaktualne, od kiedy,
   kiedy był ostatni potwierdzony sukces i co dokładnie wdrożono. Czy 40 minut
   przekracza uzgodniony cel? Czy dane rzeczywiście miały już nadejść?
2. **Konkretny plik przez kolejne etapy:** wybieram znany nowy obiekt, ustalam
   zdarzenie/wiadomość, sprawdzam kolejkę, wywołanie i log przetwarzania.
3. **Wynik i porównanie hipotez:** sprawdzam zapis wyjścia oraz odczyt raportu.
   Łączę znaleziony brak z konkretną zmianą i sprawdzam dowód, który mógłby
   obalić ten związek.

Przykład: po wdrożeniu zmieniono prefix z `incoming/` na `input/`, a reguła
zdarzeń nadal filtruje poprzedni. Nowy plik istnieje w S3, ale nie trafia
do kolejki. To lepiej wyjaśnia brak wywołań niż zwiększanie pamięci Lambdy.

> “Which specific object or message would you trace, and where should you see it next?”

Silny kandydat rozróżnia „po wdrożeniu” od „z powodu wdrożenia”. Korelacja
czasowa pomaga zawęzić poszukiwania, ale sama nie potwierdza przyczyny.

## 4. Scenariusze: do kolejki nie dociera lub w niej zalega

### Kandydat mówi: „Sprawdzę eventy i kolejkę”

> “What would you conclude if new objects exist but the queue receives no messages?”

Może sprawdzić właściwy bucket, prefix i typ zdarzenia, konfigurację
powiadomień oraz możliwość dostarczenia do docelowej kolejki. Zero widocznych
wiadomości w jednym momencie nie jest jeszcze dowodem braku dostarczeń:
wiadomości mogły zostać szybko odebrane. Potrzebna jest oś czasu i kilka źródeł dowodu.

### Kandydat mówi: „Kolejka rośnie”

> “What distinguishes a disabled consumer from a consumer that is too slow or repeatedly failing?”

Sprawdza, czy integracja jest włączona, czy są wywołania, throttling lub błędy,
jak zmieniają się zaległość i wiek wiadomości. Przybliżone metryki kolejki
pomagają diagnozować, ale nie zastępują uzgodnienia wszystkich plików z wynikami.

Samo zwiększenie concurrency może pomóc przy potwierdzonym braku przepustowości.
Nie naprawi błędnego formatu danych, brakującego uprawnienia ani przeciążonego
systemu docelowego, któremu dodatkowy ruch może zaszkodzić.

## 5. Scenariusze: Lambda pracuje, ale wynik jest zły

| Obserwacja | Możliwa hipoteza | Potrzebny dowód |
| --- | --- | --- |
| Są wywołania i AccessDenied | Zmiana roli lub polityki | Faktyczna tożsamość, operacja, zasób i warstwa odmowy |
| Są timeouty po zmianie VPC | Brak łączności z usługą | Cel połączenia, DNS, routing, reguły i endpoint/NAT |
| Funkcja kończy się sukcesem, brak wyniku | Zła ścieżka zapisu albo połknięty wyjątek | Log konkretnego pliku i rzeczywista lokalizacja wyjścia |
| Pliki wynikowe są, raport nadal stary | Problem publikacji lub odczytu | Partycja, katalog, zapytanie, cache i tożsamość odbiorcy |
| Część plików pominięta | Błąd zakresu lub niejawna częściowa porażka | Lista oczekiwanych wejść i status każdego z nich |

> “What observation would make you stop investigating Lambda and look at the reporting layer?”

Dobra odpowiedź: potwierdzony poprawny, aktualny wynik dostępny w oczekiwanym
miejscu, który raport powinien czytać. Sam status SUCCEEDED tego nie dowodzi.

Jeśli kandydat od razu wybiera IAM, poproś o powód. Odmowa dostępu ma inne
objawy niż brak dostarczenia zdarzenia. Poszerzenie uprawnień do administratora
bez ustalenia operacji i zasobu nie jest dobrą diagnostyką.

## 6. Logi, metryki i identyfikator przetwarzania

**Log** opisuje konkretne zdarzenie, np. nieudany zapis danego pliku.
**Metryka** pokazuje zmianę wartości w czasie, np. liczbę błędów lub wiek
zaległych wiadomości. **Alarm** reaguje na uzgodniony warunek.
CloudWatch zbiera i udostępnia takie sygnały, ale wybór sensownych wskaźników
nadal należy do zespołu. [AWS: CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

Przydatne pola logu: czas, środowisko, wersja wdrożenia, identyfikator
wykonania, identyfikator wejścia i etap. Pozwala to połączyć odbiór pliku
z wynikiem. Nie oznacza logowania haseł ani całej wrażliwej zawartości.

> “How would you link a failed output write back to the original input?”

Nie wymagaj jednej platformy observability. Oceniaj możliwość odnalezienia
ścieżki i odróżnienia „nie dotarło”, „zaczęło się” i „zakończyło poprawnym wynikiem”.

Pusty dashboard lub brak wpisu jest dowodem dopiero przy znajomości zakresu:
właściwe konto, region, czas, log group i filtr. Kandydat może sensownie
zacząć od sprawdzenia, czy patrzy na właściwe środowisko.

## 7. Duplikaty: idempotencja i skutek biznesowy

> “The same message reaches Lambda twice. How would you avoid a duplicate business effect?”

Integracja SQS/Lambda wymaga uwzględnienia ponowień i możliwych duplikatów.
Idempotencja oznacza, że ponowne wykonanie tej samej operacji nie powiela
jej skutku. [AWS: przetwarzanie wiadomości SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html).

Przykład skutku: podwójne doliczenie tej samej sprzedaży. Dwa uruchomienia
funkcji same w sobie nie są problemem, jeśli wynik nadal zawiera sprzedaż raz.

Oczekuj stabilnego klucza operacji i trwałego mechanizmu, np. zapisu pod
jednoznacznym kluczem albo warunkowej operacji w bazie. Klucz powinien
odróżniać nowe dane od powtórzenia: sama nazwa pliku może nie wystarczyć,
gdy plik jest nadpisywany nową wersją. Nowa wiadomość podczas replay może
mieć inny identyfikator niż pierwotna operacja biznesowa.

**Dlaczego Pythonowy set w pamięci nie wystarczy:** inne wywołanie może działać
w innym procesie, a restart usuwa pamięć. Nie jest to trwały wspólny rejestr.

**Dopytanie dodatkowe:**

> “What if the process writes the result and crashes before recording completion?”

Rejestr „przetworzone” musi być spójny ze skutkiem lub sam zapis musi być
bezpieczny do powtórzenia. Sam fakt użycia DynamoDB nie likwiduje okna awarii
między dwoma niezależnymi operacjami. Pełny projekt transakcyjny jest ponad
minimum; rozpoznanie tej granicy świadczy o większej głębi.

## 8. Batch i DLQ: jedna zła wiadomość w paczce

> “What if one message in a batch fails?”

Batch to paczka wiadomości przekazana jednemu wywołaniu. Jeśli całość zostaje
uznana za błąd, wiadomości mogą wrócić do przetwarzania, również te, których
skutek już powstał. Dlatego idempotencja jest istotna także przy błędach częściowych.

Lambda wspiera odpowiedzi o częściowych błędach paczki. Wymaga to właściwego
zachowania kodu **i** włączenia `ReportBatchItemFailures` w integracji.
Nieobsłużony wyjątek powoduje uznanie całej paczki za nieudaną. Przy kolejce
FIFO trzeba dodatkowo respektować kolejność; po pierwszej porażce nie przetwarza
się kolejnych elementów tak, jakby nic się nie stało.
[AWS: błędy integracji SQS](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html).

**DLQ, dead-letter queue**, przechowuje wiadomości odłożone zgodnie z regułą
po kolejnych nieudanych odbiorach. W tym scenariuszu mówimy o mechanizmie
redrive SQS, nie o bezrefleksyjnym przeniesieniu ustawień asynchronicznej Lambdy.

> “What would you inspect before sending messages from the DLQ back to processing?”

Oczekuj ustalenia przyczyny, zgodności aktualnego kodu, skutków wcześniejszych
prób i bezpiecznego zakresu wznowienia. DLQ nie naprawia danych. Usunięcie
wiadomości tylko po to, by zniknął alarm, ukrywa problem.

## 9. Visibility timeout, ponowienia i limity czasu

Visibility timeout to okres, przez który odebrana wiadomość jest ukryta
przed kolejnymi odbiorcami. Nie oznacza jej usunięcia. Jeśli nie zostanie
skutecznie obsłużona i usunięta, może ponownie stać się dostępna.
[AWS: visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html).

Nie myl tego z limitem czasu wykonania funkcji. Ustawienia trzeba dobrać
do czasu przetwarzania i zachowania integracji, z odpowiednim zapasem.
Zbyt krótka widoczność może dopuszczać kolejne próby, zanim pierwsza
zakończy pracę. Nie wymagaj pamięciowej znajomości konkretnego mnożnika AWS.

> “Could another attempt start while the first one is still producing a result?”

Dobra odpowiedź łączy czas przetwarzania, widoczność, retry i bezpieczny skutek.
Backoff, czyli zwiększanie odstępów ponowień, ogranicza obciążenie. Nie zmienia
jednak niebezpiecznego zapisu w idempotentny.

Samo użycie FIFO nie jest dowodem dokładnie jednego skutku w zewnętrznym
systemie. Kandydat powinien nadal uwzględnić awarię pomiędzy wykonaniem
operacji a potwierdzeniem jej zakończenia.

## 10. Jak wznowić zaległe dane i dowieść kompletności

> “After fixing the issue, how would you recover the backlog and prove the data is complete?”

Rozsądna sekwencja:

1. Ograniczyć dalszy wpływ i potwierdzić naprawę na małej, kontrolowanej próbie.
2. Ustalić zakres: jakie pliki/wersje i okres zostały dotknięte, co już
   zapisano, co jest w kolejce lub DLQ, a czego tam brakuje.
3. Zaplanować replay, czyli ponowne przetworzenie wybranego zakresu,
   z kontrolą tempa i bezpiecznym traktowaniem powtórzeń.
4. Obserwować obciążenie i błędy, żeby odzyskiwanie nie spowodowało kolejnej awarii.
5. Porównać oczekiwane wejścia z prawidłowymi wynikami. Wyjątki jawnie
   sklasyfikować, zamiast oznaczyć całość jako gotową.
6. Sprawdzić wynik u odbiorcy i dopiero wtedy zamknąć wpływ biznesowy incydentu.

Przykład: z 12 oczekiwanych plików 9 ma poprawny wynik, 2 czekają, a 1 jest
błędny i odłożony do wyjaśnienia. Pusta kolejka po skasowaniu trzech wiadomości
nie oznacza kompletnego zbioru. Równa liczba plików także nie dowodzi zgodności
rekordów, wersji i wartości.

> “What would you compare besides the queue becoming empty?”

Dobre odpowiedzi wymieniają identyfikatory wejść, statusy, wynikowe partycje,
reguły jakości oraz odczyt raportu. Dobór kontroli zależy od kontraktu danych.

## 11. Alarm: proces zielony, dane stare lub niepełne

> “What alarm would detect stale or incomplete data even when every job is green,
> and who would own the response?”

**Freshness** to świeżość danych, a **completeness** to kompletność oczekiwanego
zakresu. Można mieć świeży, lecz niepełny wynik: ostatni mały plik dotarł,
ale połowa wcześniejszych została pominięta.

W Q2 cel ćwiczenia wynosił 15 minut od nadejścia danych. Monitoring powinien
odnosić się do tak ustalonego początku i końca, np. czasu od odebrania pliku
do potwierdzonej dostępności prawidłowego wyniku, a nie samego czasu Lambdy.

Przydatne sygnały: zaległe oczekiwane wejścia, wiek najstarszego
niezakończonego przetwarzania, opóźnienie publikacji i kontrola brakujących
rekordów lub partycji. Trzeba uwzględnić harmonogram dostawcy: brak nowego
pliku w uzgodnionej przerwie nie musi być awarią.

Alert powinien mieć właściciela, priorytet i runbook, czyli krótką instrukcję
sprawdzeń oraz eskalacji. Monitoring bez reakcji nie przywraca danych.
[AWS: operational excellence dla analityki](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/operational-excellence.html).

## 12. Sieć od podstaw: timeout a AccessDenied

> “After moving a Lambda function into private subnets, its API calls time out.
> How would you distinguish networking from IAM issues and check access to S3 and Secrets Manager?”

VPC to wydzielona sieć, subnet jej fragment, a route table wskazuje drogę
ruchu. DNS tłumaczy nazwę usługi na adres. Security group kontroluje ruch
dla powiązanego interfejsu; NACL działa na poziomie podsieci.

Timeout może sugerować brak drogi, problem DNS lub reguł sieciowych.
Może też wynikać z innych przyczyn, więc nie jest automatycznym dowodem.
AccessDenied zwykle oznacza, że żądanie dotarło do usługi, ale dostęp został
odrzucony; trzeba zbadać tożsamość i właściwe polityki.

> “Which exact hostname and API operation time out?”

Bez celu połączenia „sprawdzę VPC” jest zbyt ogólne. Kandydat powinien ustalić
usługę, region, DNS, trasę, reguły ruchu oraz to, czy dostęp ma iść przez
internetowy adres usługi, NAT czy odpowiedni endpoint.

Nie wymagaj rysowania wszystkich tablic routingu. W dwie minuty potrzebujesz
spójnej ścieżki rozumowania, nie kursu konfiguracji sieci.

## 13. NAT i endpointy: S3 oraz Secrets Manager

Lambda podłączona do VPC nie uzyskuje automatycznie dostępu do internetu
przez samo umieszczenie w publicznej podsieci. Dla typowego dostępu IPv4 do
publicznych adresów z prywatnej podsieci potrzebna jest odpowiednia ścieżka,
np. NAT, albo właściwy prywatny dostęp do usługi.
[AWS: dostęp internetowy Lambdy w VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-internet.html).

**VPC endpoint** pozwala dotrzeć do obsługiwanej usługi AWS prywatną ścieżką.
Nie daje samodzielnie uprawnienia do czytania danych.

| Usługa i przykładowy wariant | Co sprawdzić |
| --- | --- |
| S3 przez gateway endpoint | Powiązanie z właściwymi route tables oraz politykę endpointu |
| Secrets Manager przez interface endpoint | Osiągalność interfejsu, security group, DNS/prywatny DNS oraz polityki |
| Zewnętrzne API internetowe | Odrębną ścieżkę wyjścia, np. NAT; endpoint S3 go nie obsłuży |

S3 gateway endpoint nie wymaga tej samej konfiguracji co interface endpoint
Secrets Manager. Możliwe są też inne poprawne warianty, np. interface endpoint
dla S3, jeśli kandydat ma powód jego użycia.
[AWS: endpoint S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html),
[AWS: endpoint Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

> “If S3 works but Secrets Manager times out, what could be different in their network paths?”

Szukaj zrozumienia różnic, nie automatycznej odpowiedzi „wszędzie NAT”.
Gdy wystarczają poprawnie działające endpointy, NAT nie jest obowiązkowy.
Z kolei odmowa endpoint policy jest problemem uprawnień na tej ścieżce,
a nie brakiem samego połączenia.

## 14. Komunikat do biznesu i zmiana awaryjna

> “Please give a brief status update to a business stakeholder about the incident.
> Explain the impact, what you know, what remains uncertain, what you are doing
> next, and when they can expect another update.”

Przykładowa odpowiedź, wyłącznie dla założonego scenariusza:

> “The orders report has not received new data for 40 minutes, so please treat
> it as outdated. Source files are still arriving, but we have not yet confirmed
> where processing stops. We are tracing a recent file and checking the latest
> deployment. We have not confirmed data loss or a recovery time. I will provide
> another update in 15 minutes, including the confirmed impact and next steps.”

Jeśli kandydat ma inne potwierdzone ustalenia ze swojej diagnozy, powinien
ich użyć. Nie oczekuj tej samej liczby minut ani tekstu. Oceniaj fakty,
niepewności, działanie i termin kolejnego komunikatu. Obietnica następnej
aktualizacji jest inna niż nieuzasadniona obietnica naprawy.

Dodatkowy scenariusz może zastąpić inne dopytanie:

> “A stakeholder asks you to bypass the normal deployment process to restore
> service faster. How would you respond in a regulated environment?”

Szukaj znajomości rzeczywistego, zatwierdzonego procesu emergency change,
odpowiedzialności, testów i śladu decyzji. Nie wymagaj pamięciowego cytowania
regulacji GxP. Nie zakładaj też, że każda organizacja ma identyczną procedurę.
Istotna jest umiejętność szybkiego działania w uzgodnionych ramach oraz
odróżnienia koniecznej eskalacji od samowolnego obchodzenia kontroli.

## 15. Możliwe odpowiedzi, ocena i 11 minut rozmowy

| Kandydat mówi | Dopytanie po angielsku | Co ustalasz |
| --- | --- | --- |
| “I would restart it.” | “What state or data could already have changed?” | Czy rozumie skutki powtórzenia |
| “I would roll back.” | “What confirms the deployment caused this, and what data would remain?” | Hipoteza i granice cofnięcia |
| “I would increase concurrency.” | “What evidence identifies throughput as the bottleneck?” | Czy skaluje właściwy element |
| “There are no errors.” | “Are there invocations and confirmed fresh outputs?” | Czy myli ciszę ze zdrowiem |
| “I would replay the DLQ.” | “What cause is fixed, and how do you prevent duplicate effects?” | Bezpieczne wznowienie |
| “I would add a NAT.” | “Which destination needs it, and could an endpoint meet the requirement?” | Zrozumienie drogi ruchu |
| “A set prevents duplicates.” | “What happens in a second worker or after a restart?” | Trwałość deduplikacji |

**Plan czasu:** diagnoza 0-4 min; powtórzenia, backlog i alarm 4-7 min;
sieć 7-9 min; komunikat 9-11 min. Nie poświęcaj całego Q6 na zaawansowaną
idempotencję kosztem sieci i komunikacji.

**3:** diagnozuje od wejścia do odbiorcy, wskazuje dowód dla hipotezy,
rozumie trwały bezpieczny skutek ponowień, kontrolowane odzyskanie i podstawy
łączności. Przekazuje jasny status. **2:** dochodzi do tego z podpowiedziami.
**4:** podaje własny incydent, rozpoznaje okna częściowego sukcesu i weryfikuje
kompletność wyniku. **1:** mimo wyjaśnienia proponuje wyłącznie ślepe restart,
poszerzenie dostępu lub usunięcie zaległości. **N/O:** brak wystarczającego dowodu.

Zapisz osobno diagnozę, odzyskanie danych, sieć i komunikację. Nie maskuj
braku wiedzy w jednym obszarze ogólnym stwierdzeniem „dobrze zna AWS”.

## 16. Ściąga przed zadaniem pytania

**Po co pytasz:** czy kandydat potrafi przywrócić wiarygodne dane, ustalić
przyczynę i jasno zakomunikować wpływ.

**Pierwsze sprawdzenia:** wpływ i ostatni sukces; konkretny plik przez przepływ;
potwierdzony wynik oraz rzeczywisty odczyt odbiorcy. Brak błędów nie oznacza wywołań.

**Słownik:** backlog = zaległa praca; batch = paczka wiadomości; DLQ = kolejka
odłożonych niepowodzeń; replay = ponowne przetwarzanie; idempotencja =
powtórzenie bez podwójnego skutku; freshness = świeżość; completeness = kompletność;
runbook = instrukcja reakcji; NAT = element umożliwiający określoną ścieżkę wyjścia;
endpoint = dostęp do obsługiwanej usługi przez VPC.

**Minimum dobrej odpowiedzi:**

- Dowód potwierdzający lub obalający konkretną hipotezę.
- Powtórzenia bez podwójnego skutku; trwałe rozwiązanie, nie tylko pamięć procesu.
- Naprawa przyczyny przed replay, uzgodnienie wejść z wynikami i odczyt odbiorcy.
- Alarm dla danych, z właścicielem i instrukcją działania.
- Rozróżnienie timeoutu i odmowy dostępu; cel, DNS, trasa, reguły, endpoint/NAT.
- Komunikat: wpływ, fakty, niepewności, działania i kolejna aktualizacja.

**Dwa najlepsze dopytania:**

> “What evidence would make you reject your leading hypothesis?”

> “How do you prove recovery beyond an empty queue and green jobs?”

**Nie wymagaj:** kompletnego systemu transakcyjnego, dokładnego JSON-a
odpowiedzi paczki ani pamięciowej konfiguracji AWS. Oceniaj rozumowanie,
bezpieczną decyzję i sposób sprawdzenia wyniku.

Materiał powiązany: [plan rozmowy](data_platform_engineer_devops_60min_pl.md).
