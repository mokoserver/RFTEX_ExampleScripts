
import time
from RFSE import Stage, Report, Program, SelectCheckHash, SetHash
try:
    from MWEB import MWeb
except Exception as e:
    Stage(f"MWEB import error: {e}", "error")
    try:
        import sys, subprocess
        subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([sys.executable, "-m", "pip", "install", "-U", "selenium", "--user"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        from MWEB import MWeb
        Stage("Selenium auto-install completed, retrying MWEB import", "info")
    except Exception as e2:
        Stage(f"Failed to auto-install selenium: {e2}", "error")
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
    Stage(f"Opening page: {url}")
    browser.open(url)
    time.sleep(1)
    return browser

def close_browser(browser):
    if browser:
        Stage("Closing browser.")
        browser.close()
    else:
        try:
            from MWEB import close_global
            Stage("Closing browser.")
            close_global()
        except Exception as e:
            Stage(f"Failed to close browser: {e}", "error")
# endregion

# region --- Generic Actions ---

def hide_browser(browser):
    if not browser:
        try:
            from MWEB import get_global
            browser = get_global()
        except Exception:
            browser = None
    if browser:
        Stage("Hiding browser.")
        try:
            browser.hide()
        except Exception as e:
            Stage(f"Failed to hide browser: {e}", "error")
    else:
        Stage("Browser is not initialized.", "error")

def minimize_browser(browser):
    if not browser:
        try:
            from MWEB import get_global
            browser = get_global()
        except Exception:
            browser = None
    if browser:
        Stage("Minimizing browser.")
        try:
            browser.minimize()
        except Exception as e:
            Stage(f"Failed to minimize browser: {e}", "error")
    else:
        Stage("Browser is not initialized.", "error")

def login_to_router(browser, username, password):
    Stage("Logging in...")
    browser.send_keys("id", "username", username)
    browser.send_keys("id", "password", password)
    browser.click("id", "login-btn")
    time.sleep(1)
# endregion

# region --- High-Level Test Function ---

def _run_test_with_report(report_name, browser, hash, point_id, power_level, channel):
    if browser is None:
        try:
            from MWEB import get_global
            browser = get_global()
        except Exception:
            browser = None
    if browser is None:
        Stage("Browser is not initialized.", "error")
        return
    if SelectCheckHash(hash):
        try:
            Stage(f"--- Executing measurement point #{point_id} ---")
            _set_power_level(browser, power_level)
            _set_channel(browser, channel)
            time.sleep(0.5)

            transmit_power = _read_transmit_power(browser)
            effective_rate = _read_effective_rate(browser)

            Program('tree', 'set', f'info = Point {point_id}; Power {power_level}; Channel {channel}; Tx {transmit_power}; Rate {effective_rate}')
            report_data = f"{point_id};{power_level};{channel};{transmit_power};{effective_rate}"
            Report(report_name, 'set', 'table', report_data)
            Stage("Data written to report.")

            SetHash('passed')
            Stage("Step status: PASSED.", "info")

        except Exception as e:
            SetHash('failed')
            Stage(f"Error during step #{point_id}: {e}", "error")
        finally:
             Stage("---")

def run_test_point(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("WiFi Performance", browser, hash, point_id, power_level, channel)

def run_test_point_batch1(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("WiFi Performance - Batch 1", browser, hash, point_id, power_level, channel)

def run_test_point_additional(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("WiFi Performance - Additional", browser, hash, point_id, power_level, channel)

def run_test_point_batch2(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("WiFi Performance - Batch 2", browser, hash, point_id, power_level, channel)

def run_test_point_batch3(browser, hash, point_id, power_level, channel):
    return _run_test_with_report("WiFi Performance - Batch 3", browser, hash, point_id, power_level, channel)
# endregion

# region --- Low-Level WiFi Actions (now also high-level) ---

def _set_power_level(browser, power_level):
    # Use the new universal method from MWEB
    browser.select_dropdown_by_value("id", "power-level", power_level)

def _set_channel(browser, channel):
    # Use the new universal method from MWEB
    browser.select_dropdown_by_value("id", "channel", channel)

def _read_transmit_power(browser):
    return browser.read_text("id", "transmit-power")

def _read_effective_rate(browser):
    return browser.read_text("id", "effective-rate")

# endregion
