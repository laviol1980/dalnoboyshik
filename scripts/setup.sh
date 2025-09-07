#!/usr/bin/env bash
set -e
echo '[setup] Подготовка окружения…'
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo '[setup] Готово.'
