
import time
from RFSE import Stage
try:
    from MWEB import MWeb
except Exception as e:
    Stage(f"Ошибка импорта MWEB: {e}", "error")
    try:
        import sys, subprocess
        subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([sys.executable, "-m", "pip", "install", "-U", "selenium", "--user"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        from MWEB import MWeb

        Stage("Автоустановка selenium выполнена, повторяю импорт MWEB", "info")
    except Exception as e2:
        Stage(f"Не удалось установить selenium автоматически: {e2}", "error")
        raise

# region --- Browser Setup ---

def get_router_url():
    import os
    html_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'RFSE_RouterExample', 'index.html'))
    return f"file:///{html_file_path.replace('\\', '/')}"

def initialize_browser(url=None):
    if url is None:
        url = get_router_url()
    browser = MWeb()
    Stage(f"Открываю страницу: {url}")
    browser.open(url)
    time.sleep(1)
    return browser

def close_browser(browser):
    if browser:
        Stage("Закрываю браузер.")
        browser.close()
    else:
        try:
            from MWEB import close_global
            Stage("Закрываю браузер.")
            close_global()
        except Exception as e:
            Stage(f"Не удалось закрыть браузер: {e}", "error")
# endregion

# region --- Generic Actions ---
def ensure_browser(browser):
    """Получает глобальный браузер, если передан None. Возвращает browser или None."""
    if browser is None:
        try:
            from MWEB import get_global
            browser = get_global()
        except Exception:
            browser = None
    if browser is None:
        Stage("Браузер не инициализирован.", "error")
    return browser

def hide_browser(browser):
    browser = ensure_browser(browser)
    if browser:
        Stage("Скрываю браузер.")
        try:
            browser.hide()
        except Exception as e:
            Stage(f"Не удалось скрыть браузер: {e}", "error")
    else:
        Stage("Браузер не инициализирован.", "error")

def minimize_browser(browser):
    browser = ensure_browser(browser)
    if browser:
        Stage("Сворачиваю браузер.")
        try:
            browser.minimize()
        except Exception as e:
            Stage(f"Не удалось свернуть браузер: {e}", "error")
    else:
        Stage("Браузер не инициализирован.", "error")

def login_to_router(browser, username, password):
    Stage("Вхожу в систему...")
    browser.send_keys("id", "username", username)
    browser.send_keys("id", "password", password)
    browser.click("id", "login-btn")
    time.sleep(1)
# endregion

# region --- Low-Level WiFi Actions (теперь они тоже высокоуровневые) ---

def _set_power_level(browser, power_level):
    # Используем новый универсальный метод из MWEB
    browser.select_dropdown_by_value("id", "power-level", power_level)

def _set_channel(browser, channel):
    # Используем новый универсальный метод из MWEB
    browser.select_dropdown_by_value("id", "channel", channel)

def _read_transmit_power(browser):
    return browser.read_text("id", "transmit-power")

def _read_effective_rate(browser):
    return browser.read_text("id", "effective-rate")

# endregion
