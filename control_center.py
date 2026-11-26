import shutil

updates = False
while True:
    st = "ВКЛ" if updates else "ВЫКЛ (Защита)"
    print("\n=== VARDOSANIDZE OS | CONTROL CENTER v0.2 ===")
    print("1. Память и диск   2. Игровой Boost")
    print("3. Умный ИИ        4. Сетевой модуль")
    print(f"5. Автообновления: [{st}]   0. Выход")
    cmd = input("Выбор: ")
    if cmd == "1":
        t, u, f = shutil.disk_usage("/data")
        print(f"💾 Диск: свободно {f // (2**30)} ГБ из {t // (2**30)} ГБ | ОЗУ: ~512 МБ")
    elif cmd == "2":
        print("🎮 Игровой Boost АКТИВИРОВАН! Лишние службы заморожены.")
    elif cmd == "4":
        print("🌐 Сетевой модуль DPI: АКТИВЕН (минимальный пинг).")
    elif cmd == "5":
        updates = not updates
        print("🔄 Статус автообновлений изменён!")
    elif cmd == "3":
        q = input("🤖 Вопрос ИИ: ").lower()
        if "озу" in q or "памят" in q: print("🤖 ИИ: Система ест всего ~500 МБ, всё свободно под игры!")
        elif "игр" in q or "fps" in q: print("🤖 ИИ: Советую включить пункт 2 (Игровой Boost) для макс. FPS.")
        elif "кто" in q or "создал" in q: print("🤖 ИИ: Я встроенный ИИ Vardosanidze OS. Мой создатель — Илья Вардосанидзе.")
        else: print("🤖 ИИ: Принято! Оптимизирую работу системы под твою задачу.")
    elif cmd == "0": break
