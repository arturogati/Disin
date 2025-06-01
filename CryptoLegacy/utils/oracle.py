class DeathOracle:
    def __init__(self, is_dead: bool = False):
        self.is_dead = is_dead
    
    def check_death(self, address: str) -> bool:
        # В реальности: запрос к API госреестров
        return self.is_dead
    


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