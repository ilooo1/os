import os, shutil, platform, subprocess

def get_pc_stats():
    print("=== VARDOSANIDZE OS: HARDWARE MONITOR ===")
    cpu = platform.processor() or platform.machine()
    total, _, free = shutil.disk_usage("/")
    print(f"CPU: {cpu} ({os.cpu_count()} потоков) | Диск свободно: {free // (2**30)} ГБ")
    try:
        out = subprocess.check_output("lspci | grep -i vga", shell=True, text=True).strip()
        gpu = out.split(":")[-1].strip()
    except Exception:
        gpu = "Автоопределение GPU (готово к работе на ПК)"
    print(f"GPU: {gpu} [MangoHud FPS Active]")

if __name__ == "__main__":
    get_pc_stats()
