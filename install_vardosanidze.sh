#!/bin/bash
echo "=== УСТАНОВКА VARDOSANIDZE OS v1.0 (UNIVERSAL PC) ==="
echo "[1/3] Скачиваю модули системы с GitHub..."
mkdir -p ~/VardosanidzeOS && cd ~/VardosanidzeOS
git clone https://github.com/ilooo1/os.git .
echo "[2/3] Применяю настройки софта, сети и FPS-оверлея..."
bash setup_os.sh && bash optimize_pc.sh
echo "[3/3] Добавляю ярлык Vardosanidze Control Center в меню ПК..."
mkdir -p ~/.local/share/applications
printf "[Desktop Entry]\nName=Vardosanidze Control Center\nExec=python3 ~/VardosanidzeOS/gui_center.py\nType=Application\nTerminal=false\n" > ~/.local/share/applications/vardosanidze.desktop
echo "✅ СБОРКА ЗАВЕРШЕНА! Система готова к работе на любом ПК."
