from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

_GLOBAL_MWEB = None


class MWeb:
    def __init__(self, block_input_method=None):
        self.driver = None
        self.block_method = block_input_method
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        if self.block_method == 'headless':
            chrome_options.add_argument("--headless")
        self.options = chrome_options

    def open(self, url):
        if self.driver:
            print("Браузер уже открыт.")
            return
        try:
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(url)
            if self.block_method == 'overlay':
                self.block_user_input()
            global _GLOBAL_MWEB
            _GLOBAL_MWEB = self
        except Exception as e:
            print(f"Не удалось запустить Chrome. Убедитесь, что ChromeDriver установлен. Ошибка: {e}")
            raise

    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def _get_by_strategy(self, strategy):
        strategy = strategy.lower()
        if strategy == 'id':
            return By.ID
        elif strategy == 'name':
            return By.NAME
        elif strategy == 'css selector':
            return By.CSS_SELECTOR
        elif strategy == 'xpath':
            return By.XPATH
        elif strategy == 'class name':
            return By.CLASS_NAME
        elif strategy == 'link text':
            return By.LINK_TEXT
        else:
            raise ValueError(f"Неподдерживаемая стратегия поиска: {strategy}")

    def _find_element(self, strategy, selector, timeout=10):
        if not self.driver: raise Exception("Браузер не открыт.")
        by = self._get_by_strategy(strategy)
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, selector)))

    def click(self, strategy, selector):
        element = self._find_element(strategy, selector)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
            print(f"Выполнен JS-клик по элементу: {selector}")
        except Exception as e:
            print(f"JS-клик не удался, пробую стандартный метод. Ошибка: {e}")
            element.click()

    def send_keys(self, strategy, selector, text):
        element = self._find_element(strategy, selector)
        element.clear()
        element.send_keys(text)

    def read_attribute(self, strategy, selector, attribute):
        element = self._find_element(strategy, selector)
        return element.get_attribute(attribute)

    def read_text(self, strategy, selector):
        element = self._find_element(strategy, selector)
        return element.text

    # --- НОВЫЕ УНИВЕРСАЛЬНЫЕ МЕТОДЫ ---

    def select_dropdown_by_value(self, strategy, selector, value):
        select_element = self._find_element(strategy, selector)
        select_object = Select(select_element)
        select_object.select_by_value(str(value))

    def accept_alert(self, wait_time=1):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            return None

    def hide(self):
        if not self.driver:
            raise Exception("Браузер не открыт.")
        try:
            self.driver.minimize_window()
            self.driver.set_window_position(-32000, -32000)
        except Exception:
            self.driver.minimize_window()

    def minimize(self):
        if not self.driver:
            raise Exception("Браузер не открыт.")
        self.driver.minimize_window()

    def block_user_input(self):
        """Блокирует ввод пользователя, создавая прозрачный оверлей."""
        if not self.driver:
            raise Exception("Браузер не открыт.")

        overlay_id = "mweb-input-blocker"
        script = f"""
            if (document.getElementById('{overlay_id}')) return;
            var overlay = document.createElement('div');
            overlay.id = '{overlay_id}';
            overlay.style.position = 'fixed';
            overlay.style.top = '0';
            overlay.style.left = '0';
            overlay.style.width = '100vw';
            overlay.style.height = '100vh';
            overlay.style.backgroundColor = 'rgba(0,0,0,0.0)';
            overlay.style.zIndex = '10000';
            document.body.appendChild(overlay);
        """
        self.driver.execute_script(script)
        print("Ввод пользователя заблокирован.")

    def unblock_user_input(self):
        """Разблокирует ввод, удаляя оверлей."""
        if not self.driver:
            raise Exception("Браузер не открыт.")

        overlay_id = "mweb-input-blocker"
        script = f"""
            var overlay = document.getElementById('{overlay_id}');
            if (overlay) {{
                overlay.parentNode.removeChild(overlay);
            }}
        """
        self.driver.execute_script(script)
        print("Ввод пользователя разблокирован.")


def close_global():
    global _GLOBAL_MWEB
    if _GLOBAL_MWEB:
        try:
            _GLOBAL_MWEB.close()
        finally:
            _GLOBAL_MWEB = None


def get_global():
    return _GLOBAL_MWEB
