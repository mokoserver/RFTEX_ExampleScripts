
import os
import time
import sys

# Добавляем путь к папке Libs, чтобы можно было импортировать MWEB
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Libs.MWEB import MWeb

def run_automation():
    # Получаем абсолютный путь к index.html
    # Это делает скрипт независимым от того, где он запускается
    html_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.html'))
    
    # Конвертируем путь в формат URL
    local_url = f"file:///{html_file_path.replace('\\', '/')}"

    browser = MWeb()

    try:
        print(f"Открываю страницу: {local_url}")
        browser.open(local_url)
        time.sleep(1)

        print("Вхожу в систему...")
        browser.send_keys("id", "username", "admin")
        browser.send_keys("id", "password", "password123")
        browser.click("id", "login-btn")
        time.sleep(1)

        print("Меняю имя сети (SSID)...")
        new_ssid = "RFSE_Test_WiFi"
        browser.send_keys("id", "ssid", new_ssid)
        browser.click("id", "save-ssid-btn")
        time.sleep(1) # Даем время на появление alert
        
        # Selenium не может напрямую взаимодействовать с нативными alert'ами
        # Но мы можем их принять (нажать "ОК")
        try:
            alert = browser.driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
        except Exception as e:
            print(f"Не удалось обработать alert: {e}")

        print("Инициирую перезагрузку роутера...")
        browser.click("id", "reboot-btn")
        time.sleep(1)
        
        try:
            alert = browser.driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
        except Exception as e:
            print(f"Не удалось обработать alert: {e}")

        print("Скрипт успешно выполнен. Ожидание перед закрытием...")
        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка во время выполнения: {e}")

    finally:
        print("Закрываю браузер.")
        browser.close()

if __name__ == "__main__":
    run_automation()
