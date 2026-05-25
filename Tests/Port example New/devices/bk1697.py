import RFSE
from Mport import Device

class BK1697(Device):
    """
    Класс для работы с прибором BK1697.
    """
    def get_max_power(self) -> str | None:
        """
        Отправляет команду GMAX00 и возвращает результат.

        Returns:
            str | None: Результат выполнения команды или None в случае ошибки.
        """
        ok_result = '402502'

        if not self.is_initialized:
            RFSE.Stage(f"[{self.name}] Устройство не инициализировано. Попытка переподключения...", type='warning')
            self.connect()
            if not self.is_initialized:
                return None

        if self._write('GMAX00'):
            result_command = self._read()
            result_status = self._read()
            if result_status == 'OK' and result_command == ok_result:
                RFSE.Stage(f"[{self.name}] Статус: успешно. Команда вернула: {result_command}", type='info')
                return result_command
            else:
                RFSE.Stage(type='warning', stage_string=f"[{self.name}] Статус: ошибка. Статус ответа: {result_status}, Результат команды: {result_command}")
                self.is_initialized = False
                return None
        return None
