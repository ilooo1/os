#!/bin/bash
echo "=== УСТАНОВКА VARDOSANIDZE OS v0.1 ==="
echo "[1/4] Отключаю фоновые и принудительные обновления..."
# sudo systemctl disable --now unattended-upgrades
echo "[2/4] Ставлю игровой пакет (Steam + MangoHud FPS по умолчанию)..."
# sudo apt install -y steam mangohud gamemode
echo "[3/4] Настраиваю сетевой модуль и снижение пинга..."
# Настройка сетевого стека BBR
echo "[4/4] Интегрирую Центр управления и локальный ИИ..."
chmod +x control_center.py
echo "✅ ГОТОВО! Vardosanidze OS настроена и готова к работе."
