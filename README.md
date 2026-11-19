# Lazy Launcher

Первая запускаемая версия Lazy Launcher для запуска уже установленной локальной сборки Minecraft Java 1.12.2 + Forge.

## Запуск на Windows

Требуется Python 3.10+ для запуска из исходников.

~~~powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python main.py
~~~

В окне выберите папку .minecraft (или корень экземпляра, внутри которого лежит .minecraft), введите ник и нажмите «Играть». Можно выбрать Java вручную и настроить RAM. Настройки профиля сохраняются локально.

## Что реализовано в 0.1.0

- PySide6 GUI с выбором игровой папки.
- Поиск Forge-профиля 1.12.2 по version JSON.
- Локальный ник и корректный offline UUID.
- Поиск Java и проверка Java 8 x64.
- Чтение Forge и родительского Minecraft JSON.
- Построение classpath, распаковка Windows natives и legacy minecraftArguments.
- Запуск настоящего Java-процесса без shell.
- Вывод игрового процесса в окно и файл лога.
- Настройка RAM.

## Ограничения

Это не установщик сборки. Лаунчер использует файлы, которые уже установлены в выбранной папке: versions, libraries, assets, mods, config и ресурсы. Он пока не скачивает недостающие компоненты, не устанавливает Java и не обновляет модпак.

Поддерживается legacy Forge JSON с minecraftArguments, характерный для Minecraft 1.12.2. Если JSON/библиотеки/ресурсы отсутствуют, лаунчер сообщает об ошибке, а не подменяет их случайными файлами.

Offline-профиль предназначен для одиночной игры и LAN. Он не проходит авторизацию на серверах с online-mode=true.

## Тесты и сборка portable приложения

~~~powershell
python -m pytest
python -m pip install pyinstaller
pyinstaller --noconfirm --windowed --name "Lazy Launcher" main.py
~~~

Windows EXE следует собирать на Windows. Portable build с PyInstaller будет собираться в Windows CI.

## CI
Windows CI на ветке разработки запускает pytest и собирает portable ZIP как GitHub Actions artifact.
