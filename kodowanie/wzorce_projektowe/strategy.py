from abc import ABC, abstractmethod


# Strategia
class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start, end):
        pass


# Konkretne Strategie
class FastestRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        return f"Najszybsza trasa z {start} do {end}"


class ScenicRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        return f"Najbardziej malownicza trasa z {start} do {end}"


class WalkingRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        return f"Trasa piesza z {start} do {end}"


# Kontekst
class NavigationApp:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def build_route(self, start, end):
        return self._strategy.build_route(start, end)


# Klient
nav_app = NavigationApp(FastestRouteStrategy())
print(nav_app.build_route("Dom", "Praca"))

nav_app.set_strategy(ScenicRouteStrategy())
print(nav_app.build_route("Dom", "Praca"))
