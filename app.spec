# -*- mode: python ; coding: utf-8 -*-

import sys
sys.setrecursionlimit(5000)

block_cipher = None


a = Analysis(['app.py'],
             pathex=['D:\\dash'],
             binaries=[],
             datas=[('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\dash_core_components\\', 'dash_core_components'),
                 ('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\dash_html_components\\', 'dash_html_components'),
                 ('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\dash_renderer\\','dash_renderer'),
				 ('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\dash_table\\','dash_table'),
				 ('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\dash\\','dash'),
				 ('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\flask\\','flask'),
				 ('C:\\Users\\sunwt\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\plotly\\', 'plotly')],
             hiddenimports=['pkg_resources.py2_warn','plotly.express','flask_compress'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')
