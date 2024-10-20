# CREAR MÚLTIPLES CARPETAS

import calendar
from pathlib import Path

mesAño = list(calendar.month_name[1:])
diaSemana = ["Día 1", "Día 10", "Día 20"]

for i, mes in enumerate(mesAño):
    for dia in diaSemana:
        Path( f"2024/{i+1}.{mes}/{dia}" ).mkdir(parents=True, exist_ok=True)
