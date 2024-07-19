Jak działa docker? Czemu środowisko jest hermetyczne?


Kontenery Dockera zapewniają izolację i lekkość wirtualizacji, jednak robią to inaczej niż tradycyjne maszyny wirtualne. Izolacja kontenerów Dockera opiera się na kilku kluczowych funkcjach jądra systemu Linux, takich jak przestrzenie nazw (namespaces), grupy kontrolne (cgroups) oraz opcjonalnie systemy plików tylko do odczytu i inne mechanizmy bezpieczeństwa, takie jak SELinux i AppArmor. Oto jak te mechanizmy działają razem, aby izolować kontenery:

1. Przestrzenie nazw (Namespaces)
Przestrzenie nazw to funkcja jądra Linuxa, która ogranicza widoczność i dostęp do zasobów systemowych pomiędzy grupami procesów. Każdy kontener działa w swojej własnej, izolowanej przestrzeni nazw, co zapewnia, że procesy w jednym kontenerze nie mogą widzieć procesów w innych kontenerach ani interweniować w ich działanie. Istnieje kilka typów przestrzeni nazw, izolujących różne aspekty systemu operacyjnego, w tym:

* PID (Process ID): Izoluje przestrzeń identyfikatorów procesów, dzięki czemu procesy w każdym kontenerze mogą mieć własne, niepowtarzalne PIDy.
* NET (Network): Zapewnia kontenerom własne stosy sieciowe, adresy IP, tablice routingu itp.
* MNT (Mount): Izoluje punkty montowania, dzięki czemu kontenery mogą mieć własne systemy plików.
* IPC (Inter-Process Communication): Izoluje mechanizmy komunikacji międzyprocesowej.
* UTS (Unix Timesharing System): Pozwala kontenerom mieć własne nazwy hosta i domeny.
* USER: Izoluje przestrzenie identyfikatorów użytkowników i grup, umożliwiając procesom działanie z różnymi uprawnieniami w ramach kontenera.

2. Grupy kontrolne (cgroups)
Grupy kontrolne pozwalają Dockerowi ograniczać i monitorować zasoby systemowe, które mogą być używane przez kontenery, takie jak CPU, pamięć RAM, I/O dysku i sieci. Dzięki temu można zapobiec sytuacjom, w których jeden kontener zużywa nieproporcjonalną ilość zasobów, wpływając negatywnie na działanie innych kontenerów lub samego hosta.

3. Systemy plików tylko do odczytu i warstwowe systemy plików
Docker używa unii systemów plików, takich jak OverlayFS, które pozwalają kontenerom mieć wspólne, tylko do odczytu warstwy systemu plików, przy jednoczesnym umożliwieniu zapisu w warstwach specyficznych dla danego kontenera. To zapewnia, że zmiany dokonane w jednym kontenerze nie wpływają na inne kontenery ani na obraz bazowy.

4. Mechanizmy bezpieczeństwa
Dodatkowo, Docker i system operacyjny mogą używać różnych mechanizmów bezpieczeństwa, takich jak SELinux, AppArmor, i seccomp, aby jeszcze bardziej zwiększyć izolację i ograniczyć możliwości działania kontenerów. Te narzędzia mogą nakładać dodatkowe polityki bezpieczeństwa, które ograniczają działania, jakie kontenery mogą wykonywać, i zasoby, do których mogą mieć dostęp.

Dzięki tym mechanizmom kontenery Dockera oferują silną izolację przy jednoczesnym zachowaniu wydajności i elastyczności, co czyni je popularnym rozwiązaniem w wielu scenariuszach deweloperskich i produkcyjnych.