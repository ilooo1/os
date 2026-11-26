#!/bin/bash
echo "=== VARDOSANIDZE OS: ОПТИМИЗАЦИЯ ПК ==="
echo "[1/3] Уменьшаю задержки ядра (sysctl) и отключаю лишний своп..."
sudo sysctl -w vm.swappiness=10
sudo sysctl -w fs.inotify.max_user_watches=524288
sudo sysctl -w net.core.default_qdisc=fq
sudo sysctl -w net.ipv4.tcp_congestion_control=bbr
echo "[2/3] Настраиваю драйверы AMD Mesa и MangoHud FPS по умолчанию..."
mkdir -p ~/.config/MangoHud
cat << 'CFG' > ~/.config/MangoHud/MangoHud.conf
fps
gpu_stats
gpu_temp
cpu_stats
cpu_temp
ram
position=top-right
font_size=20
CFG
echo "[3/3] Включаю глобальный оверлей Vulkan (MANGOHUD=1)..."
grep -q "MANGOHUD=1" /etc/environment || echo "MANGOHUD=1" | sudo tee -a /etc/environment
echo "✅ ГОТОВО! Оптимизация ядра, сети BBR и счётчик FPS применены."
