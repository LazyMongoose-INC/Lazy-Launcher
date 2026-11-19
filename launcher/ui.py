import logging,os
from pathlib import Path
from PySide6.QtCore import QThread,Signal,Slot
from PySide6.QtWidgets import QApplication,QFileDialog,QFormLayout,QHBoxLayout,QLabel,QLineEdit,QMainWindow,QMessageBox,QPushButton,QSpinBox,QTextEdit,QVBoxLayout,QWidget
from . import __version__
from .discovery import find_installation
from .profiles import load_profile,save_profile,validate_nickname
from .runtime import build_command,find_java,run_process
LOG=Path.home()/"AppData"/"Roaming"/"LazyLauncher"/"logs"
if not LOG.parent.exists(): LOG=Path.home()/".config"/"LazyLauncher"/"logs"
LOG.mkdir(parents=True,exist_ok=True)
logging.basicConfig(filename=LOG/"launcher.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s",encoding="utf-8")
class Worker(QThread):
    output=Signal(str); done=Signal(int); error=Signal(str)
    def __init__(self,path,nick,java,ram): super().__init__(); self.path=path; self.nick=nick; self.java=java; self.ram=ram
    def run(self):
        try:
            inst=find_installation(self.path); java=find_java(self.java)
            self.output.emit("Forge: "+inst.version_id); self.output.emit("Java: "+str(java))
            cmd,cwd=build_command(inst,self.nick,java,self.ram); self.output.emit("Запуск настоящего процесса Minecraft…")
            self.done.emit(run_process(cmd,cwd,self.output.emit))
        except Exception as e: logging.exception("Launch failed"); self.error.emit(str(e))
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Lazy Launcher "+__version__); self.resize(760,580); self.worker=None
        p=load_profile(); root=QWidget(); v=QVBoxLayout(root); title=QLabel("LAZY LAUNCHER"); title.setStyleSheet("font-size:28px;font-weight:800")
        v.addWidget(title); v.addWidget(QLabel("LazyMongoose Modpack • Minecraft Java 1.12.2")); form=QFormLayout()
        self.folder=QLineEdit(p.get("game_dir","")); self.folder.setPlaceholderText("Папка .minecraft или экземпляра")
        b=QPushButton("Выбрать папку…"); b.clicked.connect(self.pick_folder); row=QHBoxLayout(); row.addWidget(self.folder,1); row.addWidget(b); w=QWidget(); w.setLayout(row); form.addRow("Папка игры:",w)
        self.nick=QLineEdit(p.get("nickname","LazyPlayer")); self.nick.setMaxLength(16); form.addRow("Игровой ник:",self.nick)
        self.java=QLineEdit(p.get("java","")); self.java.setPlaceholderText("Автоопределение или путь к javaw.exe")
        jb=QPushButton("Обзор…"); jb.clicked.connect(self.pick_java); jr=QHBoxLayout(); jr.addWidget(self.java,1); jr.addWidget(jb); jw=QWidget(); jw.setLayout(jr); form.addRow("Java:",jw)
        self.ram=QSpinBox(); self.ram.setRange(1024,32768); self.ram.setSingleStep(512); self.ram.setValue(int(p.get("memory_mb",4096))); self.ram.setSuffix(" МБ"); form.addRow("RAM:",self.ram)
        v.addLayout(form); buttons=QHBoxLayout(); self.play=QPushButton("ИГРАТЬ"); self.play.setMinimumHeight(42); self.play.clicked.connect(self.start)
        f=QPushButton("Папка игры"); f.clicked.connect(self.open_folder); l=QPushButton("Открыть лог"); l.clicked.connect(self.open_log)
        buttons.addWidget(self.play,2); buttons.addWidget(f); buttons.addWidget(l); v.addLayout(buttons)
        self.status=QLabel("Выберите папку существующей Minecraft 1.12.2 Forge."); v.addWidget(self.status)
        self.console=QTextEdit(); self.console.setReadOnly(True); v.addWidget(self.console,1); self.setCentralWidget(root)
        self.setStyleSheet("QMainWindow,QWidget{background:#15191f;color:#e8edf3;font-size:13px} QLineEdit,QSpinBox,QTextEdit{background:#202731;border:1px solid #394554;border-radius:6px;padding:8px} QPushButton{background:#26323e;border:1px solid #435263;border-radius:7px;padding:9px} QPushButton#play{background:#176b48}")
        self.play.setObjectName("play"); self.log("Прототип 0.1.0: использует установленную сборку; установку и загрузку пока не выполняет.")
    def log(self,s): self.console.append(s); logging.info(s)
    def pick_folder(self):
        p=QFileDialog.getExistingDirectory(self,"Выберите папку Minecraft/экземпляра")
        if p: self.folder.setText(p)
    def pick_java(self):
        p,_=QFileDialog.getOpenFileName(self,"Выберите Java","","javaw.exe/java.exe (*)")
        if p: self.java.setText(p)
    def start(self):
        try:
            nick=validate_nickname(self.nick.text())
            if not self.folder.text().strip(): raise ValueError("Сначала выберите папку сборки.")
            save_profile({"nickname":nick,"game_dir":self.folder.text().strip(),"java":self.java.text().strip(),"memory_mb":self.ram.value()})
            inst=find_installation(self.folder.text().strip()); self.log("Найден Forge: "+inst.version_id); self.status.setText("Игра запускается…"); self.play.setEnabled(False)
            self.worker=Worker(self.folder.text().strip(),nick,self.java.text().strip(),self.ram.value())
            self.worker.output.connect(self.log); self.worker.error.connect(self.failed); self.worker.done.connect(self.finished); self.worker.start()
        except Exception as e: QMessageBox.critical(self,"Ошибка запуска",str(e))
    @Slot(str)
    def failed(self,msg):
        self.play.setEnabled(True); self.status.setText("Ошибка запуска"); self.log("ОШИБКА: "+msg); QMessageBox.critical(self,"Ошибка запуска",msg)
    @Slot(int)
    def finished(self,code):
        self.play.setEnabled(True); self.status.setText("Minecraft завершился. Код: "+str(code)); self.log("Minecraft exit code: "+str(code))
    def open_folder(self):
        p=self.folder.text().strip()
        if not p or not Path(p).is_dir(): QMessageBox.information(self,"Папка","Сначала выберите папку."); return
        self.open_path(p)
    def open_log(self):
        p=LOG/"launcher.log"; p.touch(exist_ok=True); self.open_path(str(p))
    @staticmethod
    def open_path(p):
        try: os.startfile(p)
        except Exception as e: QMessageBox.warning(None,"Ошибка",str(e))
    def closeEvent(self,event):
        if self.worker and self.worker.isRunning():
            if QMessageBox.question(self,"Выход","Minecraft ещё работает. Закрыть лаунчер?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes: event.ignore(); return
        event.accept()
def run_app():
    import sys
    app=QApplication(sys.argv); win=MainWindow(); win.show(); return app.exec()
