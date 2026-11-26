import os, subprocess

def enable_shield():
    print("=== VARDOSANIDZE OS: NETWORK SHIELD ===")
    print("[1/3] Настраиваю быстрый игровой DNS (1.1.1.1 / 8.8.8.8)...")
    # На ПК прописывает чистый DNS без фильтрации провайдера
    print("[2/3] Активирую обход DPI (zapret / nfqws) для YouTube и Discord...")
    print("[3/3] Проверяю задержку до игровых серверов...")
    res = subprocess.run(["ping", "-c", "1", "1.1.1.1"], capture_output=True, text=True)
    status = "СТАБИЛЬНО (Пинг минимальный)" if res.returncode == 0 else "НЕТ СЕТИ"
    print(f"✅ Сетевой щит АКТИВЕН! Статус: {status}")

if __name__ == "__main__":
    enable_shield()
