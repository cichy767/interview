Serverless, czyli "bezserwerowe" to model obliczeniowy, w którym zarządzanie infrastrukturą serwerową jest w pełni zautomatyzowane i ukryte przed developerem. W tym modelu deweloperzy skupiają się tylko na pisaniu kodu i definiowaniu zdarzeń, które mają go uruchamiać, a dostawca chmury zajmuje się resztą — skalowaniem, utrzymaniem, aktualizacjami i zarządzaniem serwerami.

Kluczowe cechy serverless
1. Automatyczne skalowanie: Aplikacje są automatycznie skalowane w zależności od potrzeb, co oznacza, że system może obsługiwać zarówno bardzo małą, jak i bardzo dużą liczbę żądań bez interwencji użytkownika.
2. Rozliczenie za użycie: Płaci się tylko za faktyczny czas, kiedy kod jest wykonywany. Gdy kod nie jest uruchamiany, nie generuje kosztów.
3. Zarządzanie przez dostawcę: Cała infrastruktura jest zarządzana przez dostawcę usług chmurowych, co redukuje obciążenie związane z zarządzaniem serwerami, sieciami, przechowywaniem danych i bezpieczeństwem.


Jak to działa?
W architekturze serverless, kod jest zwykle uruchamiany w odpowiedzi na zdarzenia. Zdarzenia te mogą pochodzić z wielu źródeł, takich jak żądania HTTP do API, 
zmiany w bazie danych, przesyłanie plików, czy też zdarzenia z planistów zadań. Po odebraniu zdarzenia, 
platforma serverless dynamicznie przydziela zasoby do wykonania kodu, a po zakończeniu go zwalnia te zasoby.


**Zalety i wady serverless**

**Zalety:**

* Koszty: Płacenie tylko za to, co się używa, może znacząco obniżyć koszty operacyjne, szczególnie dla aplikacji z nieregularnym ruchem.
* Produktywność: Developerzy mogą skupić się na pisaniu kodu, nie martwiąc się o infrastrukturę.
* Szybkość wdrażania: Aplikacje można szybko wdrożyć i zaktualizować.

**Wady:**

* Problem zimnego startu: Jeśli funkcja nie była używana przez jakiś czas, jej pierwsze wywołanie może być wolniejsze, ponieważ musi być "zimno" uruchomiona.
* Ograniczenia platformy: Możliwości konfiguracyjne i kontroli są ograniczone, co może nie pasować do niektórych zaawansowanych wymagań.
* Zależność od dostawcy: Migracja między platformami może być trudna ze względu na specyfikę implementacji i używane API.