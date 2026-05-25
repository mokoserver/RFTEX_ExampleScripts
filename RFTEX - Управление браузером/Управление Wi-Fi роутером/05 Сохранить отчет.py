import RFSE
from RFSE import Stage, StageError, StageInfo,StageSuccess

#region Создание протокола$REPORT
#description: MS Word;
RFSE.HashExecuteStep("Создание протокола$REPORT")

if RFSE.HashSelectCheck('Создание протокола$REPORT'):
    try:
        RFSE.ReportSave("Word")
        RFSE.StageSuccess("Word-отчет сгенерирован")
        RFSE.HashSet('passed')
    except Exception as e:
        RFSE.StageError(f"Ошибка во время генерации отчета: {e}")
        RFSE.HashSet('failed')

RFSE.ReportTimeAdd('add',"RU")
RFSE.EndScript()
