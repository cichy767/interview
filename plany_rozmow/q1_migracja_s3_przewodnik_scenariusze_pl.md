# Q1: migracja S3 między kontami

Jak prowadzić pytanie o projekt, rozumieć odpowiedzi i wybierać dopytania

**Data Platform Engineer / AWS DevOps · materiał po polsku · 17 października 2026**

Przewodnik dla prowadzącego bez doświadczenia DevOps. Rozwija pierwsze pytanie
z planu interview i opisuje możliwe ścieżki odpowiedzi, ze szczególnym naciskiem
na „włączyłem replikację S3”. Pytania do kandydata podano po angielsku.

**Najważniejsza zasada:** wybór zarządzanej usługi może być bardzo dobrą decyzją.
Oceniaj rozumienie, rzeczywisty wkład i dowody działania. Ilość własnego kodu
nie jest miarą jakości rozwiązania.

Wszystkie wypowiedzi kandydata i scenariusze są przykładami hipotetycznymi,
a nie zweryfikowanym opisem jego pracy. Bank dopytań jest szerszy niż cztery
minuty przeznaczone na Q1. W rozmowie wybierz najważniejsze i przejdź dalej.

## 1. Pytanie główne i jego cel

> “Your CV mentions an end-to-end cross-account S3 migration. Could you sketch
> the data flow, explain who consumed the data, and identify the components
> you personally designed, implemented, or operated?”

Po polsku: pokaż drogę danych, wyjaśnij, kto ich potrzebował, i określ własny
udział w zaprojektowaniu, wdrożeniu lub utrzymaniu migracji między kontami AWS.

Pytanie ma sprawdzić trzy rzeczy: **co osobiście zrobiłeś, dlaczego tak
postąpiłeś i skąd wiesz, że wynik był poprawny**. Daje też punkt odniesienia
do późniejszych pytań o IAM, Terraform, CI/CD i diagnozowanie problemów.

End-to-end może obejmować uzgodnienie zakresu, przygotowanie, wykonanie,
weryfikację i przekazanie. Nie oznacza automatycznie, że jedna osoba zbudowała
każdy komponent. Poprawna odpowiedź może wyraźnie wskazywać udział innych zespołów.

**Przykład konkretu:** „Konta były gotowe. Ja zmieniłem moduł dostępu,
przygotowałem weryfikację i przeprowadziłem przełączenie odbiorcy”.
**Odpowiedź wymagająca dopytania:** „Robiliśmy migrację w AWS przy użyciu Lambdy”.

> “What problem was the migration intended to solve?”

Cel biznesowy może dotyczyć nowej platformy, dostępu innego zespołu lub zmiany
odpowiedzialności za dane. Kandydat nie musi znać całej strategii organizacji,
ale powinien rozumieć cel własnego zadania.

## 2. Siedem warstw, które możesz sprawdzić

| Warstwa | Pytanie po angielsku | Jakiego konkretu szukasz |
| --- | --- | --- |
| Cel i odbiorca | “Who needed the data, and what did they need to do with it?” | Potrzeba użytkownika i oczekiwany rezultat |
| Własny zakres | “What was already in place, and what did you personally change?” | Wkład własny oddzielony od pracy innych |
| Przepływ | “What actually moved the data?” | Źródło, mechanizm, miejsce docelowe i odbiorca |
| Skala i ograniczenia | “What was the approximate scale and the main constraint?” | Wolumen, liczba obiektów, czas, dostęp lub bieżące zapisy |
| Decyzja | “What alternative did you consider, and why did you choose this approach?” | Wymaganie, wybór i zaakceptowany kompromis |
| Wynik i dowód | “How did you prove that it was complete and usable?” | Weryfikacja danych i odczytu odbiorcy |
| Problemy i przekazanie | “What failed, how did you recover, and who operated it afterwards?” | Diagnoza, bezpieczne dokończenie i odpowiedzialność |

Nie musisz przejść przez wszystkie warstwy osobnym pytaniem. Dobra krótka
opowieść może pokryć kilka naraz. Jeśli odpowiedź jest długa, poproś o jeden przykład.

Przybliżona skala wystarczy. Miliony małych plików stawiają inne wymagania niż
niewiele dużych. Większa liczba nie oznacza automatycznie większej samodzielności.
Nie wymagaj nazw kont, klientów, repozytoriów ani dostępu do poufnych dokumentów.

Szukaj związku przyczynowego: „mieliśmy ograniczenie X, więc wybraliśmy Y,
a test Z potwierdził wynik”. Płynność wypowiedzi, akcent i używanie „my” same
nie rozstrzygają o kompetencjach.

## 3. Minimum techniczne potrzebne prowadzącemu

| Pojęcie | Znaczenie w tej rozmowie |
| --- | --- |
| S3 object | Obiekt przechowujący dane, często plik, wraz z metadanymi |
| Bucket | Pojemnik na obiekty S3 |
| Object key / prefix | Nazwa obiektu / początek nazwy określający zakres, np. orders/ |
| Konto AWS | Oddzielna przestrzeń zarządzania zasobami i dostępem |
| Region | Lokalizacja usług; inne konto nie musi oznaczać innego regionu |
| Versioning | Przechowywanie i rozróżnianie wersji obiektów |
| Replikacja | Automatyczne kopiowanie według reguł określonej usługi |
| Backfill | Uzupełnienie historycznego zakresu danych |
| Cutover | Przełączenie odbiorców na docelowe rozwiązanie |
| IAM / role / policy | Uprawnienia / tożsamość sesji / reguły dostępu |
| KMS | Usługa zarządzania kluczami kryptograficznymi i ich użyciem |
| IaC / Terraform | Opis infrastruktury w kodzie / narzędzie realizujące taki opis |

Podstawowy rysunek może być bardzo prosty:

```text
Bucket źródłowy / konto A -> mechanizm transferu
                         -> bucket docelowy / konto B
                         -> aplikacja, analityk albo zadanie danych
```

Do każdego komponentu kandydat może dopisać: kto go przygotował, kto miał
uprawnienia i jak sprawdzono działanie. To wystarczy; nie wymagaj diagramu
korporacyjnej architektury.

Ważne rozróżnienie: **mechanizm transferu** przenosi dane, natomiast skrypt
pomocniczy może tylko uruchamiać proces, monitorować go albo porównywać wyniki.
W CV tego kandydata Lambda i Python mogą oznaczać właśnie takie wsparcie.

## 4. Co oznacza „skorzystałem z replikacji S3”

### To pełnoprawny wariant rozwiązania

Natywna replikacja S3 wykonuje asynchroniczne kopiowanie między bucketami.
Może działać między kontami, w tym samym regionie lub między regionami.
SRR oznacza ten sam region, CRR różne regiony. Cross-account opisuje konta,
a cross-region regiony; to dwie osobne cechy.
[AWS: rodzaje replikacji](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html).

Kandydat nie musi pisać własnego programu kopiującego, aby wykonać wartościową
pracę inżynierską. Wykorzystanie usługi zarządzanej może zmniejszać koszt
implementacji i utrzymania. Musi jednak umieć wyjaśnić swój zakres i wynik.

### Co nadal pozostaje do ustalenia przez zespół

| Element | Sens pytania |
| --- | --- |
| Wybór obiektów | Czy reguła obejmowała cały bucket, czy np. określony prefix? |
| Warunki techniczne | Czy przygotowano wersjonowanie i odpowiedni dostęp? |
| Historia | Jak potraktowano obiekty istniejące wcześniej? |
| Szyfrowanie | Czy potrzebna była konfiguracja SSE-KMS i właściwe klucze? |
| Wdrożenie | Co kandydat zrobił w konsoli, IaC lub procesie akceptacji? |
| Monitoring | Jak zauważano opóźnienie albo błąd? |
| Odbiór | Jak sprawdzono wymagane dane i dostęp odbiorcy? |

Replikacja wymaga włączonego wersjonowania bucketa źródłowego i docelowego oraz
odpowiednich uprawnień. Nie wymagaj pełnej polityki JSON z pamięci.
[AWS: wymagania replikacji](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-requirements.html).

Bieżąca replikacja nie obejmuje automatycznie obiektów, które istniały przed
jej skonfigurowaniem. Interfejs może zaproponować dodatkowe zadanie dla historii;
to osobny mechanizm, który kandydat powinien umieć rozróżnić.
[AWS: live i Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html).

### Trzy rzeczy, których nie należy zakładać

Uruchomienie reguły nie oznacza zakończenia transferu. Obiekt w miejscu docelowym
nie dowodzi jeszcze, że właściwy odbiorca może go odczytać. Przeniesienie danych
nie oznacza przeniesienia całej konfiguracji bucketa, np. reguł lifecycle
i powiadomień.
[AWS: zakres replikacji](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-what-is-isnot-replicated.html).

Właściwa reakcja na „użyłem replikacji” to spokojne pogłębienie odpowiedzi,
bez sugerowania, że użycie gotowej usługi było zbyt proste.

## 5. Scenariusz A: kandydat mówi tylko „włączyłem replikację”

### Dwa dopytania pierwszego wyboru

> “What did you personally configure, and what was already provided by the team?”

> “Did this cover only new objects, or historical objects as well? How did you verify the required scope?”

Pierwsze ustala wkład własny. Drugie sprawdza rozumienie zakresu, a następnie
weryfikacji. Jeśli nie było historii, odpowiedź „tylko nowe obiekty” może być
całkowicie poprawna. Nie wymagaj backfillu, którego projekt nie potrzebował.

### Możliwe odpowiedzi i kolejny ruch

| Co usłyszysz | Jak to rozumieć | Następne pytanie |
| --- | --- | --- |
| „Wybrałem bucket docelowy w konsoli” | Wiemy o wykonaniu kroku; nie znamy jeszcze szerszej odpowiedzialności | “Who prepared permissions, and what did you test afterwards?” |
| „Dodałem regułę i dostęp w Terraform” | Możliwy konkretny wkład IaC | “Which parts did you change, and what did the plan and test confirm?” |
| „Konta i moduł były gotowe” | Normalna praca w istniejącej platformie | “What did you need to understand or adapt for this migration?” |
| „Migrowaliśmy wyłącznie przyszłe dostawy” | Brak historii może być zgodny z wymaganiem | “How was that scope agreed, and how did you test new arrivals?” |
| „Po włączeniu stare pliki też się przeniosły” | Być może użyto dodatkowej operacji albo skrótu myślowego | “Was there a separate batch job or transfer for the existing objects?” |
| „AWS zrobił wszystko automatycznie” | Brakuje informacji o jego pracy i odbiorze | “What did you check before declaring the work complete?” |

### Krótka symulacja rozmowy

**Kandydat:** “I used S3 replication.”

**Ty:** “What did you personally configure, and what was already in place?”

**Kandydat:** “The buckets existed. I added the rule and the required policies.”

**Ty:** “Did you also need to migrate existing objects?”

**Kandydat:** “Yes. We handled those with a separate batch job.”

**Ty:** “How did you verify the result before the consumer switched over?”

Ta ścieżka daje informacje o wkładzie, historii i odbiorze. Szczegóły polityk
zostawiasz na Q2, a szczegóły IaC na Q3.

### Co może oznaczać odpowiedź „zrobiłem to w konsoli”

Nie jest automatycznie dyskwalifikująca. Ustal, czy był to eksperyment, zatwierdzona
operacja jednorazowa, ręczny etap procedury czy nieudokumentowana zmiana produkcji.
W roli DevOps potrzebujesz też dowodów powtarzalnego zarządzania infrastrukturą,
ale możesz je zebrać w Q3 na innym przykładzie.

Jeśli po dopytaniu kandydat opisuje wyłącznie wykonanie instrukcji i nie rozumie
zakresu lub testu, masz dowód wąskiej samodzielności w tym zadaniu. Nie dopisuj
mu odpowiedzialności za całą migrację ani nie wnioskuj od razu o całym profilu.

## 6. Scenariusz B: live replication i osobny transfer historii

**Możliwa odpowiedź:** “We used live replication for new writes and S3 Batch
Replication for existing objects.”

To logiczny wariant, gdy nowe pliki nadal przychodzą, a trzeba przenieść historię.
Same nazwy dwóch mechanizmów nie dowodzą jednak poprawnego wykonania.

Batch Replication działa na istniejących obiektach na żądanie i może obejmować
także określone przypadki wcześniejszych błędów replikacji. Wymaga istniejącej
konfiguracji replikacji. Manifest to opis obiektów objętych zadaniem; może być
przygotowany lub wygenerowany zgodnie z możliwościami usługi. Raport wykonania,
jeśli skonfigurowany, pomaga rozliczyć operacje.
[AWS: S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html).

> “How did you define the historical scope, and what did you do with failed items?”

> “While the backfill was running, how did you account for new writes and overwrites?”

**Szukaj:** uzgodnionego zakresu, wersji, rozliczenia braków, obsługi błędów i testu
odbiorcy. Kandydat nie musi pamiętać formatu manifestu ani wszystkich opcji.

**Przykład sensownej odpowiedzi:** „Ustaliliśmy, które dane mają zostać przeniesione,
sprawdziliśmy wynik zadania i błędne obiekty, a nowe dostawy kontrolowaliśmy
oddzielnie. Odbiorca odczytał wskazany zbiór przed przełączeniem”. Poproś
o rzeczywisty przykład, aby uzyskać dowód zamiast hipotetycznego opisu.

**Ważne rozróżnienie:** S3 Batch Operations Copy i S3 Batch Replication to różne
operacje. Pierwsza wykonuje kopiowanie obiektów według manifestu; druga korzysta
z mechanizmu replikacji. Zapytaj o konkretną operację, jeśli kandydat mówi
jedynie „użyliśmy batcha”.
[AWS: Batch Operations Copy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-copy-object.html).

Nie zakładaj, że wszystkie historyczne wersje zachowają się zgodnie z oczekiwaniem
bez ustalenia wymagań. Zapytaj, czy celem były bieżące wersje, czy historia.
Nie wymagaj migracji historii wersji, jeśli nie należała do zakresu.

## 7. Scenariusz C: polecenie CLI, np. aws s3 sync

**Możliwa odpowiedź:** “It was a one-off transfer. I used aws s3 sync.”

CLI to program wywoływany poleceniem. Może być rozsądnym narzędziem dla danego
zakresu i skali. Krótkie polecenie może stać za dobrze przygotowaną operacją;
nie trzeba zastępować go długim własnym skryptem.

`sync` synchronizuje wskazany zakres według zasad i opcji polecenia. Nie należy
zakładać, że jest migracją całej konfiguracji, wszystkich wersji albo pełną
weryfikacją zgodności bajt po bajcie. Opcja `--delete` może usuwać obiekty
w miejscu docelowym, których nie ma w źródle; znaczenie mają też filtry.
To temat do wyjaśnienia, a nie polecenie do wykonania podczas rozmowy.
[AWS CLI: sync](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html).

> “Why was this approach suitable for the scope and scale?”

> “What happened if the command stopped halfway through?”

> “How did you decide what needed copying, and how did you verify the result?”

**Szukaj:** kontrolowanej tożsamości, właściwego zakresu, logów/wyniku, bezpiecznego
powtórzenia i sprawdzenia odbiorcy. Jeśli źródło zmieniało się w trakcie, dopytaj
o nadrobienie zmian i moment porównania.

**Odpowiedź wymagająca pogłębienia:** „Polecenie zakończyło się sukcesem, więc
migracja była kompletna”. Zapytaj, jak ten sukces wiązał się z uzgodnionym zakresem.
Sukces polecenia i odbiór biznesowy to odrębne dowody.

Nie obniżaj oceny za brak skomplikowanej architektury, jeżeli prosty mechanizm
spełniał wymagania i był bezpiecznie przeprowadzony.

## 8. Scenariusz D: Python, boto3 albo Lambda

**Możliwa odpowiedź:** “I wrote Python automation with boto3 and ran part of it in Lambda.”

Najpierw ustal, czy kod kopiował dane, koordynował inne zadanie czy wyłącznie
sprawdzał wynik. To trzy różne rodzaje pracy.

> “What exactly did your code do, and what was handled by AWS or another component?”

Następnie poproś o jedną operację, wejście i wynik. Przy kopiowaniu dużej liczby
obiektów ważne jest objęcie całego zakresu listowania. API może zwracać wyniki
stronami; paginacja obsługuje kolejne strony. Nie wymagaj pamiętania ich limitu.
[AWS boto3: paginatory](https://docs.aws.amazon.com/boto3/latest/guide/paginators.html).

> “How did you make sure you processed all objects, not just the first page?”

> “How could an operator identify and retry only the failed scope?”

**Szukaj:** świadomego zakresu, raportowania częściowych błędów, bezpiecznych
ponowień, testów i kontroli czasu działania. Checkpoint to trwały zapis postępu,
pomagający kontynuować dłuższą pracę. Nie zawsze jest potrzebny, ale kandydat
powinien umieć wyjaśnić sposób wznowienia przy własnej skali.

Jeśli wszystko wykonywała jedna Lambda, zapytaj, jak czas zadania mieścił się
w ograniczeniach wykonania i co działo się po przerwaniu. Lambda ma limit czasu
pojedynczego wywołania; nie jest dowolnie długo działającym serwerem.
[AWS: ograniczenia Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).

**Dodatkowa głębia:** kandydat uzasadnia, dlaczego własny kod był potrzebny
i które obowiązki przejmował względem usługi zarządzanej. Więcej kodu oznacza
również więcej zachowań do przetestowania i utrzymywania.

Jeśli kod był tylko narzędziem wspierającym replikację, nie wymagaj, żeby sam
implementował transfer, który poprawnie realizowała usługa S3.

## 9. Scenariusz E: DataSync lub inne zarządzane zadanie transferu

**Możliwa odpowiedź:** “We configured an AWS DataSync task between the S3 locations.”

DataSync jest zarządzaną usługą transferu danych. AWS dokumentuje również transfer
między bucketami S3 na różnych kontach. Korzystanie z niej wymaga odpowiedniego
dostępu i konfiguracji lokalizacji oraz zadania.
[AWS: DataSync między kontami S3](https://docs.aws.amazon.com/datasync/latest/userguide/tutorial_s3-s3-cross-account-transfer.html).

> “What did you configure yourself, and how did you check the task results?”

> “How did this handle changes arriving after the first transfer?”

**Szukaj:** uzasadnienia wyboru, prawidłowych lokalizacji i tożsamości, zakresu
przesyłania, interpretacji wyniku i testu konsumenta. Zadanie zarządzane nadal
wymaga świadomego planu migracji.

Nie przenoś automatycznie wymagań live replication na inne narzędzia. Przykładowo
pytanie o wersjonowanie jako warunek replikacji nie oznacza tego samego obowiązku
dla każdego rodzaju transferu. Zapytaj o wymagania rzeczywiście użytej metody.

Jeżeli kandydat wskazuje inne narzędzie, wróć do pytań uniwersalnych: zakres,
własna konfiguracja, wynik, błędy, odbiór. Nie wymagaj nazwy rozwiązania z tego
przewodnika. Wariantów i kombinacji jest więcej niż w tej liście.

## 10. Scenariusz F: gotowy moduł, wąski wkład lub brak kopiowania

### „Skorzystałem z istniejącego modułu Terraform”

To normalne w zespole platformowym. Wspólne moduły mają umożliwiać powtarzalne
wdrożenia. Zapytaj o parametry, zmianę, plan i test, a nie o napisanie wszystkiego
od zera.

> “What did the module provide, what did you adapt, and what did you verify?”

**Dobry sygnał:** kandydat rozumie efekt konfiguracji, zakres swoich uprawnień
i zachowanie po wdrożeniu. **Dopytaj przy:** „wpisałem wartości z instrukcji”,
jeśli nie umie wyjaśnić ich znaczenia ani sprawdzenia wyniku.

### „Odpowiadałem tylko za uprawnienia lub testy”

To konkretny, możliwie wartościowy zakres. Ustal, które decyzje podejmował i co
potrafił wykonać samodzielnie. Nie przypisuj mu autorstwa całej migracji.
Zbierz pozostałe dowody w kolejnych blokach rozmowy.

> “Which operations were you responsible for enabling or testing?”

### „Udostępniliśmy istniejące dane innemu kontu”

Możliwe, że żadne dane nie były kopiowane. Mogło chodzić o zmianę dostępu,
przejęcie roli albo przepięcie odbiorcy. Poproś o doprecyzowanie terminu migracja.

> “Were objects physically copied, or did the consumer start accessing the existing location?”

Nie nazywaj tego od razu błędem lub nadużyciem. Ustal rzeczywisty przebieg i oceniaj
ujawniony zakres. Zmiana dostępu może być technicznie istotna, choć daje inne
dowody niż przeprowadzenie transferu danych.

### „Koordynowałem projekt, techniczną część wykonywał inny zespół”

Komunikacja i koordynacja mają wartość, szczególnie przy tym CV. Pytanie ma jednak
również zebrać dowody inżynierskie. Poproś o własną zmianę techniczną albo
przykład z innego projektu. Jasne przyznanie granic jest lepsze niż dopisywanie
sobie cudzego wkładu.

## 11. Gdy replikacja nie działa: możliwe ścieżki diagnozy

### Brakuje starego pliku, ale nowe się kopiują

Najpierw sprawdź, czy stary obiekt należał do zakresu historycznego i czy uruchomiono
dla niego odpowiedni transfer. Potem pytaj o filtr, wersję i wynik operacji.
Nie trzeba zaczynać od rozszerzania uprawnień.

> “Was this object eligible for live replication, or did it require the historical transfer?”

### Obiekt oczekuje albo ma błąd

W podstawowym scenariuszu źródło może pokazywać `PENDING`, `COMPLETED` lub `FAILED`,
a docelowa replika `REPLICA`. Są także bardziej złożone konfiguracje. Status
jest dowodem dla danego obiektu i kontekstu, nie automatycznym odbiorem całej migracji.

`PENDING` oznacza brak zakończenia; przy przejściowej niedostępności usługa może
kontynuować po odzyskaniu zasobu. `FAILED` wymaga ustalenia przyczyny i sposobu
ponownego objęcia obiektu transferem. Nie zakładaj, że po naprawieniu polityki
wszystkie wcześniej nieudane obiekty automatycznie ruszą ponownie. Można rozważyć
odpowiednie Batch Replication albo ponowny zapis, uwzględniając jego skutki.
[AWS: statusy i ponawianie replikacji](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-status.html).

> “After fixing the cause, how did you recover the objects that had already failed?”

### Część obiektów szyfrowanych nie dociera

Możliwe obszary sprawdzenia to ustawienia reguły dla SSE-KMS, dostęp do klucza
źródłowego i klucza docelowego oraz polityki zasobów. Ustal, jaka rola wykonuje
operację. Sam dostęp do S3 może nie wystarczać.
[AWS: replikacja obiektów szyfrowanych](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html).

Nie wymagaj szczegółowych akcji KMS z pamięci. Dobra odpowiedź ustala tożsamość,
operację i klucz, zamiast nadawać stały dostęp administratora.

### Plik jest na miejscu, ale odbiorca nie czyta

Oddziel rolę wykonującą transfer od roli odbiorcy. Sprawdź jego uprawnienia S3,
KMS, właściwą lokalizację oraz ustawienia własności obiektów. Własność i dostęp
zależą od konfiguracji; samo istnienie kopii nie rozstrzyga obu kwestii.
[AWS: właściciel repliki](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-change-owner.html),
[AWS: KMS między kontami](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html).

### Kandydat mówi „sprawdziliśmy CloudWatch”

> “Which metric or event did you inspect, and what did it show?”

Po włączeniu odpowiednich metryk replikacji można śledzić np. oczekujące dane,
operacje i opóźnienie. Dostępne są także zdarzenia błędów. Nie wymagaj nazw metryk
z pamięci; oczekuj wyjaśnienia, co mierzono i jak na to reagowano.
[AWS: monitoring replikacji](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-metrics.html).

## 12. Co ma znaczyć „migracja się udała”

### Uzgodniony zakres jest podstawą porównania

Trzeba określić buckety, prefixy, wersje i punkt w czasie. Gdy źródło nadal
przyjmuje zapisy, chwilowe porównanie może pokazywać różnice wynikające z ruchu.
Kandydat powinien wyjaśnić sposób nadrobienia zmian lub uzgodnienia punktu odcięcia.

Równe liczby obiektów nie dowodzą zgodności: źródło może zawierać A, B, C,
a cel A, B, D. Suma rozmiarów także nie identyfikuje wszystkich braków.
Próbka sprawdza wybrany zakres; nie należy przedstawiać jej jako dowodu
kompletności każdego obiektu.

### Tożsamość, zawartość i możliwość użycia

Szukaj porównania właściwych obiektów/wersji, uzgodnionej kontroli integralności,
rozliczenia niepowodzeń i odczytu jako docelowy odbiorca. ETag nie zawsze jest
MD5 zawartości; metoda porównania musi odpowiadać sposobowi zapisu i szyfrowania.
[AWS: ETag obiektu](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Object.html).

> “What evidence did you use beyond a successful job status or matching counts?”

Nie wymagaj jednej uniwersalnej metody walidacji. Jej zakres powinien wynikać
z wymagań i ryzyka. Kandydat może nie pamiętać dokładnego raportu; powinien
rozumieć, co on potwierdzał i jakie miał ograniczenia.

### Przełączenie i dokończenie po awarii

Cutover to rozpoczęcie korzystania z celu. Zapytaj o warunki gotowości, osobę
akceptującą i plan na problem po przełączeniu. Jeśli nowe zapisy trafiają już
do nowego miejsca, powrót do starego może wymagać uzgodnienia danych; nie jest
automatycznie bezpieczny.

Jeśli 80% pracy się udało, kandydat powinien umieć wskazać pozostałe 20%, usunąć
przyczynę, bezpiecznie dokończyć i powtórzyć sprawdzenie. „Uruchomiliśmy wszystko
jeszcze raz” może być poprawne, jeśli potrafi wyjaśnić bezpieczeństwo tej operacji.

> “Why was rerunning that scope safe in your setup?”

### Domknięcie odpowiedzialności

Kto otrzymywał alarmy? Kto obsługiwał błędne obiekty? Jak przekazano instrukcję
operacyjną i dostęp? Te pytania pomagają ustalić znaczenie deklaracji end-to-end.
Nie zakładaj, że po przekazaniu projektu kandydat miał osobiście pełnić stały dyżur.

## 13. Przykładowe odpowiedzi i ich interpretacja

Poniższe przykłady służą kalibracji. Nie są odpowiedziami, których trzeba oczekiwać
słowo w słowo, ani twierdzeniami o pracy tej osoby.

### Odpowiedź ogólna: za mało dowodów

> “I enabled replication, selected the destination bucket and AWS copied the data.”

Wiemy, jaki mechanizm wskazuje. Nadal nie znamy celu, zakresu, wkładu i testu.
Zadaj dwa pytania z rozdziału 5. Nie oceniaj negatywnie samego użycia replikacji.
Jeśli po wyjaśnieniu nadal nie potrafi podać konkretu, zapisz brak dowodów
samodzielności w tym projekcie.

### Wąski, ale uczciwie opisany zakres

> “The platform team provided the design and module. I configured the approved
> scope, ran the deployment and tested a new object. Historical migration and
> consumer cutover were owned by another engineer.”

To konkretne doświadczenie wykonawcze, lecz nie dowód samodzielnego zaprojektowania
całej migracji. Dopytaj o rozumienie konfiguracji i testu. Głębszą samodzielność
sprawdź w kolejnych blokach albo innym projekcie.

### Odpowiedź spójna na regular/mid

> “The accounts existed. I configured replication and the required access for
> our agreed scope. We handled existing objects separately. I checked failed
> items and verified a read as the intended consumer before the handover.
> I can explain one permission issue I investigated and how I confirmed the fix.”

To dobry kierunek: własny zakres, historia, błędy i odbiorca. Poproś o jeden
rzeczywisty przykład, aby sprawdzić, czy opis ma pokrycie. Nie wymagaj użycia
dokładnie tych usług, jeśli jego projekt miał inne wymagania.

### Mocniejsza odpowiedź

Kandydat dodatkowo wyjaśnia wybór względem alternatywy, wersje i nadpisania,
zbieżność porównań przy aktywnym źródle, kontrolę kosztu, odzyskanie błędów
i warunki przełączenia. Każdy szczegół wiąże z konkretną sytuacją.

To dodatkowa głębia, a nie lista wszystkich obowiązkowych elementów dla regular/mid.
Rozbudowana opowieść bez konkretu nie jest lepsza od krótkiego, sprawdzalnego przykładu.

### Sygnały wymagające wyjaśnienia

| Twierdzenie | Jak dopytać przed oceną |
| --- | --- |
| „Stare obiekty przeniosły się po włączeniu live replication” | Czy uruchomiono osobne zadanie dla historii? |
| „Sukces API oznaczał zakończoną migrację” | Które API i co dokładnie potwierdzała odpowiedź? |
| „Administrator odczytał plik, więc odbiorca też może” | Czy przetestowano tożsamość odbiorcy? |
| „Po naprawie polityki nic więcej nie trzeba było robić” | Co stało się z wcześniej nieudanymi obiektami? |
| „ETag zawsze jest MD5” | Czy metoda uwzględniała sposób utworzenia i szyfrowanie? |
| „Wszystko zrobiłem sam” | Co już istniało i kto przeglądał lub odbierał zmianę? |

Skrót myślowy lub niedokładna pamięć nie są od razu nieporozumieniem technicznym.
Znaczenie ma wyjaśnienie po doprecyzowaniu i rzeczywisty skutek dla działania.

## 14. Jak zmieścić to w czterech minutach

### Proponowany przebieg

| Czas | Co robisz |
| --- | --- |
| 0:00–1:00 | Pytanie główne: przepływ, odbiorca i własny zakres |
| 1:00–2:00 | Doprecyzuj osobiście wykonaną zmianę i mechanizm transferu |
| 2:00–3:15 | Zapytaj o kompletność i użyteczność; przy replikacji wybierz historię, jeśli była w zakresie |
| 3:15–4:00 | Jedna własna decyzja lub jeden problem i dowód naprawy; zapisz temat do pogłębienia |

Nie czytaj całego banku pytań. Jeśli kandydat już podał konkret, wykorzystaj
czas na brakujący dowód. Jeśli opis trwa za długo, wróć do jednego przykładu.

> “To keep us on time, could you focus on one change you personally made and how you verified it?”

### Gdzie przenieść szczegóły

| Temat ujawniony w Q1 | Dalszy blok |
| --- | --- |
| Niejasne role, KMS i dostęp między kontami | Q2: bezpieczeństwo platformy |
| Konfiguracja w konsoli, stan, moduły i powtarzalność | Q3: Terraform |
| Testy i promocja bez konkretnego dowodu | Q4: CI/CD |
| Własny skrypt, częściowe błędy, paginacja | Q5: doświadczenie z Pythonem |
| Ponowienia, brak monitoringu lub odzyskania zaległości | Q6: utrzymanie |

### Notatka po Q1

```text
Cel migracji i odbiorca:
Źródło, cel i mechanizm transferu:
Co istniało wcześniej:
Własna zmiana techniczna:
Historia / nowe zapisy / wersje - uzgodniony zakres:
Decyzja i uzasadnienie:
Dowód kompletności i odczytu odbiorcy:
Problem, sprawdzenie i potwierdzenie naprawy:
Potrzebne podpowiedzi:
Temat do pogłębienia / nie oceniono:
```

To materiał pomocniczy, nie odrębny próg zatrudnienia. Używaj rubryki całej rozmowy;
Q1 samo nie wystarcza do oceny pełnych kompetencji Data Platform Engineer.

## 15. Ściąga prowadzącego i dalsza lektura

Jeżeli zapamiętasz tylko cztery pytania, wybierz te:

> “What did you personally implement?”

> “What exactly was in scope?”

> “How did you prove that it worked for the intended consumer?”

> “What happened when part of the work failed?”

Przy odpowiedzi „S3 replication” dopowiedz pytanie o nowe i istniejące obiekty.
Przy CLI lub skrypcie dopowiedz o zakres, przerwanie i bezpieczne wznowienie.
Przy gotowym module dopowiedz o zrozumienie własnej konfiguracji i testu.

**Nie nagradzaj:** liczby nazw usług, długości kodu, pewności siebie ani
niezweryfikowanej deklaracji odpowiedzialności za całość.
**Oceniaj:** konkretny wkład, uzasadnienie, zrozumienie ograniczeń, wynik i dowód.

Skróty: SRR to replikacja w tym samym regionie; CRR między regionami; SSE-KMS
to szyfrowanie po stronie usługi z wykorzystaniem KMS; CLI to narzędzie poleceń;
SDK/boto3 to biblioteka do używania API; manifest to opis obiektów objętych zadaniem;
checkpoint to zapis postępu; cutover to przełączenie odbiorcy; lifecycle to reguły
cyklu życia obiektów, np. przechowywania i usuwania.

Linki przy odpowiednich sekcjach prowadzą do dokumentacji AWS. Szczegóły
zweryfikowano 17 października 2026; opcje i ograniczenia sprawdzaj dla rzeczywistego
narzędzia i środowiska. Nie trzeba pamiętać ich wszystkich podczas interview.

[Plan rozmowy](data_platform_engineer_devops_60min_pl.md) ustala czas i kolejne bloki.
[Ogólny przewodnik po pojęciach](przewodnik_dla_prowadzacego_aws_devops_pl.md)
wyjaśnia podstawy wszystkich pytań. Ten dokument pogłębia wyłącznie Q1.
