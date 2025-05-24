# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],  # Usar el directorio actual
    binaries=[],
    datas=[
        ('backup.csv', '.'),
        ('error.txt', '.'),
        ('infos.txt', '.'),
        ('sensor_data.csv', '.'),
        ('gui.py', '.'),
        ('sensor_utils.py', '.'),
        ('serial_utils.py', '.'),
        ('telegram_bot.py', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='mi_proyecto',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Cambia a False si tu aplicación es GUI
    cipher=block_cipher,
    code_signature=None
)
