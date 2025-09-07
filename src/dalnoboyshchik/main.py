"""
Входная точка «Дальнобойщика».
Идея: один архив -> репозиторий -> автосборка/раскладка артефактов.
"""

from pathlib import Path
import json
import sys

def deliver(payload_dir: Path = Path("data"), out_dir: Path = Path("delivered")):
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "delivered_files": [],
    }
    if payload_dir.exists():
        for p in payload_dir.rglob("*"):
            if p.is_file():
                target = out_dir / p.name
                target.write_bytes(p.read_bytes())
                manifest["delivered_files"].append(str(target))
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"[OK] Доставлено файлов: {len(manifest['delivered_files'])}. Манифест: {out_dir/'manifest.json'}")

def main():
    # Позже сюда легко добавить разбор аргументов/режимов.
    deliver()

if __name__ == "__main__":
    main()
