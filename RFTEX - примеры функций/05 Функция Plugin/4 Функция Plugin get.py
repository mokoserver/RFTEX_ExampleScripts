import RFSE
import MGPH

#Region Status (статус)
#hash Plugin get

RFSE.Messenger('set', 'Plugin - get.png', 'В текущем скрипте будет продемонстрирована команда \'\'get\'\', '
                                          'которая передает данные в плагин. '
                                          'В данном скрипте будет сделан скриншот экрана')


screen = MGPH.GetScreenshotWindow()
RFSE.Report("Screenshot_1_All", 'set', 'picture', screen)

RFSE.Program('tree', 'set', 'select = ' + 'Plugin get')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()
