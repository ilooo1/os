import shutil

updates = False
fps_overlay = True  # Встроенный FPS включён по умолчанию!

while True:
    st_upd = "ВКЛ" if updates else "ВЫКЛ (Защита)"
    st_fps = "ВКЛ (Активен)" if fps_overlay else "ВЫКЛ"
    print("\n=== VARDOSANIDZE OS | CONTROL CENTER v0.3 ===")
    print("1. Память и диск   2. Игровой Boost")
    print("3. Умный ИИ        4. Сетевой модуль")
    print(f"5. Автообновления: [{st_upd}]")
    print(f"6. Встроенный FPS-оверлей: [{st_fps}]")
    print("0. Выход")
    cmd = input("Выбор: ")

    if cmd == "1":
        t, u, f = shutil.disk_usage("/data")
        print(f"💾 Диск: свободно {f // (2**30)} ГБ из {t // (2**30)} ГБ | ОЗУ: ~512 МБ")
    elif cmd == "2":
        print("🎮 Игровой Boost АКТИВИРОВАН! Приоритет CPU/GPU на максимум.")
    elif cmd == "4":
        print("🌐 Сетевой модуль DPI: АКТИВЕН (минимальный пинг).")
    elif cmd == "5":
        updates = not updates
        print("🔄 Статус автообновлений изменён!")
    elif cmd == "6":
        fps_overlay = not fps_overlay
        print(f"📊 Встроенный FPS-оверлей теперь: {'ВКЛЮЧЁН' if fps_overlay else 'ВЫКЛЮЧЕН'}")
    elif cmd == "3":
        q = input("🤖 Вопрос ИИ: ").lower()
        if "озу" in q or "памят" in q:
            print("🤖 ИИ: Система ест всего ~500 МБ, остальное свободно под игры!")
        elif "игр" in q or "fps" in q or "фпс" in q:
            print("🤖 ИИ: Встроенный счётчик FPS уже активен по умолчанию. Включи пункт 2 для буста!")
        elif "кто" in q or "создал" in q:
            print("🤖 ИИ: Я встроенный ИИ Vardosanidze OS. Мой создатель — Илья Вардосанидзе.")
        else:
            print("🤖 ИИ: Принято! Оптимизирую систему под твою задачу.")
    elif cmd == "0":
        break


