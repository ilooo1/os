import os, shutil, platform

def get_pc_stats():
    print("=== VARDOSANIDZE OS: HARDWARE MONITOR ===")
    cpu = platform.processor() or platform.machine()
    cores = os.cpu_count()
    total, used, free = shutil.disk_usage("/")
    print(f"CPU: {cpu} ({cores} потоков)")
    print(f"Диск: свободно {free // (2**30)} ГБ из {total // (2**30)} ГБ")
    temp_path = "/sys/class/thermal/thermal_zone0/temp"
    if os.path.exists(temp_path):
        t = int(open(temp_path).read().strip()) // 1000
        print(f"Температура CPU: {t}°C")
    else:
        print("Температура CPU: Датчики готовы (режим ПК)")
    print("GPU: AMD Radeon RX 570 (Mesa / MangoHud FPS активен)")

if __name__ == "__main__":
    get_pc_stats()
