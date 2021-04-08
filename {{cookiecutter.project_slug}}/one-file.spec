# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['scripts/run.py'],
             pathex=['./'],
             binaries=[('build/lib', '.'), ('lib', '.')],
             datas=[('data', 'data'), ('CHANGELOG.rst', '.')],
             hiddenimports=['json'],
             hookspath=['scripts'],
             runtime_hooks=[],
             excludes=['{{ cookiecutter.project_slug }}'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='{{ cookiecutter.project_slug }}',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
