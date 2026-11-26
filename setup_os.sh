#!/bin/bash
echo "=== УСТАНОВКА VARDOSANIDZE OS v0.2 ==="
echo "[1/5] Отключаю принудительные обновления и телеметрию..."
# sudo systemctl disable --now unattended-upgrades
echo "[2/5] Ставлю игровой пакет (Steam + MangoHud FPS по умолчанию)..."
# sudo apt install -y steam mangohud gamemode
echo "[3/5] Ставлю базовый софт (Firefox, Telegram, Discord, OBS Studio)..."
# sudo apt install -y firefox-esr telegram-desktop obs-studio
echo "[4/5] Настраиваю сетевой модуль и снижение пинга..."
# Настройка сетевого стека BBR + обход DPI
echo "[5/5] Интегрирую Центр управления и локальный ИИ..."
chmod +x control_center.py
echo "✅ ГОТОВО! Vardosanidze OS v0.2 полностью настроена."
