"""

utils/oracle.py
Назначение: Проверка внешних условий (например, смерти).
Что делает:

MockDeathOracle: Возвращает мок-данные (для тестов).

В реальности запрашивает API госреестров.
Для чего нужен:

Автоматизация триггеров (смерть/неактивность).

Интеграция с оффчейн-источниками данных.

"""


class DeathOracle:
    def __init__(self, is_dead=False):
        self.is_dead = is_dead
    
    def check_death(self, address):
        return self.is_dead