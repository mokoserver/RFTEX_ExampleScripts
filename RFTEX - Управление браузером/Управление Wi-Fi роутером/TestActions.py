
import time
import WebActions as wa
from RFSE import Stage, Report, Program, HashSelectCheck, HashSet

# region --- High-Level Test Function ---
def _run_test_with_report(report_name, browser, hash, point_id, power_level, channel):
    if (browser := wa.ensure_browser(browser)) is None: return
    if HashSelectCheck(hash):
        try:
            Stage(f"--- Выполнение точки измерения #{point_id} ---")
            wa._set_power_level(browser, power_level)
            wa._set_channel(browser, channel)
            time.sleep(0.5)

            transmit_power = wa._read_transmit_power(browser)
            effective_rate = wa._read_effective_rate(browser)

            Program('tree', 'set',
                    f'info = Точка {point_id}; Уровень {power_level}; Канал {channel}; Мощность {transmit_power}; Скорость {effective_rate}')
            report_data = f"{point_id};{power_level};{channel};{transmit_power};{effective_rate}"
            Report(report_name, 'set', 'table', report_data)
            Stage("Данные записаны в отчет.")

            HashSet('passed')
            Stage("Статус шага: ПРОЙДЕНО.", "info")

        except Exception as e:
            HashSet('failed')
            Stage(f"Ошибка при выполнении шага #{point_id}: {e}", "error")
        finally:
            Stage("---")

def run_test_point(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("Производительность Wi-Fi", browser, hash, point_id, power_level, channel)

def run_test_point_batch1(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("Производительность Wi-Fi Пакет 1", browser, hash, point_id, power_level, channel)

def run_test_point_additional(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("Производительность Wi-Fi Дополнительно", browser, hash, point_id, power_level, channel)

def run_test_point_batch2(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("Производительность Wi-Fi Пакет 2", browser, hash, point_id, power_level, channel)

def run_test_point_batch3(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("Производительность Wi-Fi Пакет 3", browser, hash, point_id, power_level, channel)
# endregion


