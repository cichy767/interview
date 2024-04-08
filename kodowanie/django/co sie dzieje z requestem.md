django tworzy obiekt HTTPRequest który reprezentuje przychodzący request i zawiera wszystkie dane o nim.
potem request trafia do middleware
middleware może być kilka, a ich kolejność jest istotna, ponieważ niektóre middleware są od siebie zależne,a request przechodzi od pierwszego zdefiniowanego do ostatniego 
później do widoku, jeśli jest to także do serializera i modelu.
gdy request został obsłużony i zaczyna wracać, także przechodzi przez te miejsca i może znów zahaczyć o middleware 
