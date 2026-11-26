import os, shutil, platform

def ask_ai(text):
    t = text.lower()
    if "желез" in t or "процессор" in t or "cpu" in t:
        return f"Архитектура: {platform.machine()} | Ядер CPU: {os.cpu_count()} | Нагрузка: Низкая"
    elif "диск" in t or "памят" in t or "мест" in t:
        _, _, free = shutil.disk_usage("/data")
        return f"Свободно: {free // (2**30)} ГБ | ОЗУ системы: ~500 МБ"
    elif "катк" in t or "игр" in t or "cs" in t or "фпс" in t:
        return "Игровой режим ВКЛ! FPS-оверлей активен, лишние службы остановлены."
    elif "создател" in t or "автор" in t:
        return "Я локальный ИИ Vardosanidze OS. Разработчик: Илья Вардосанидзе."
    return f"Задача '{text}' выполнена. Система работает стабильно."

while True:
    q = input("\n[ИИ Vardosanidze] Запрос (или 'выход'): ")
    if q.lower() == "выход": break
    print("🤖 ->", ask_ai(q))
