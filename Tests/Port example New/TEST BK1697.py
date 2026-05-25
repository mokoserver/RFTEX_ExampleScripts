import RFSE
from devices.bk1697 import BK1697

# 1. Создаем экземпляр прибора, указывая его логическое имя из RF-SE.
#    Вся логика подключения (init, interface) уже встроена в конструктор.
bk_device = BK1697(name="BK")

# 2. Вызываем метод для получения данных.
#    Внутри метода уже есть проверка статуса и обработка ошибок.
power = bk_device.get_max_power()

# 3. Работаем с результатом.
if power:
    RFSE.Stage(f"Измеренная мощность: {power}")
else:
    RFSE.Stage("Не удалось получить данные о мощности.", type='error')

RFSE.EndScript()
