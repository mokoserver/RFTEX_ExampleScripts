import RFSE
import MCLK


MCLK.ClickerInit()

#Region Status (статус)
#description: Decribe;command;;(описание;команды);
#hash The first command: to get a screenshot;of the screen;;(получить;скриншот;экрана)
screenshot = MCLK.GetScreenshot()
RFSE.Report("ClickerScr", 'set', 'picture', screenshot)

RFSE.Program('tree', 'set', 'select = ' + 'The first command')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status (статус)

#Region Status (Статус)
#description: Decribe;command;;(описание;команды);
#hash The second command: to specify the;image path;;(указать путь;картинки)

MCLK.PngPath("C:/RF-SE/Images/Desktop RFSE Long.png")

RFSE.Program('tree', 'set', 'select = ' + 'The second command')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

#Region Status (статус)
#description: Decribe;command;;(описание;команды);
#hash The third command: to get the image;from the specified;path;(получить;картинку;по указанному;пути)
png_file = MCLK.GetPngFile()
RFSE.Report("ClickerFile", 'set', 'picture', png_file)

RFSE.Program('tree', 'set', 'select = ' + 'The third command')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

RFSE.EndScript()