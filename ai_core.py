import os, json

mem_file = "ai_memory.json"
mem = json.load(open(mem_file)) if os.path.exists(mem_file) else {"user": "Илья", "mode": "Обычный"}

def save():
    json.dump(mem, open(mem_file, "w"), ensure_ascii=False)

def ask_ai(q):
    t = q.lower()
    if "провер" in t or "статус" in t or "status" in t:
        mods = ["Ядро Linux", "FPS-оверлей", "Сетевой DPI", "ИИ-модуль"]
        return " | ".join([f"{m}: OK" for m in mods])
    elif "игр" in t or "катк" in t or "game" in t:
        mem["mode"] = "Игровой (Макс. FPS)"
        save()
        return f"{mem['user']}, режим '{mem['mode']}' сохранён в память!"
    elif "режим" in t or "mode" in t:
        return f"Текущий профиль системы: {mem['mode']}"
    return f"{mem['user']}, команда '{q}' обработана."

while True:
    cmd = input(f"\n[{mem['user']} | {mem['mode']}] Запрос: ")
    if cmd.lower() in ["выход", "exit"]:
        break
    print("🤖 ->", ask_ai(cmd))
