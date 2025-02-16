# Co to jest Wektoryzacja?

to technika używana w programowaniu, szczególnie w analizie danych i naukach ścisłych, 
polegająca na operowaniu na tablicach lub sekwencjach danych jako całościach, 
zamiast stosowania pętli do iterowania i operowania na pojedynczych elementach danych. 
Wektoryzacja jest szeroko stosowana w bibliotekach Pythona do obliczeń naukowych, 
takich jak NumPy, ponieważ znacznie zwiększa wydajność przez zredukowanie liczby operacji w Pythonie na rzecz operacji 
wykonywanych na poziomie skompilowanego kodu C, który jest znacznie szybszy.

**Wydajność:**

Operacje wektoryzowane mogą być znacznie szybsze niż ich odpowiedniki realizowane przez pętle w Pythonie, 
głównie dzięki wykorzystaniu optymalizacji na poziomie niższym niż interpreter Pythona, takich jak biblioteki napisane w C, 
które mogą wykonywać operacje równolegle lub z większą efektywnością.

**Czystszy kod:**

Kod wykorzystujący wektoryzację jest często krótszy i łatwiejszy do zrozumienia, ponieważ koncentruje się na operacjach wykonywanych na całych zbiorach danych, 
a nie na szczegółach iteracji po tych danych.

**Wykorzystanie bibliotek:**

Biblioteki takie jak NumPy oferują szeroki zakres funkcji wektoryzowanych, które są już zoptymalizowane pod kątem różnych operacji matematycznych i naukowych, 
co pozwala programistom skupić się na problemach wyższego poziomu.