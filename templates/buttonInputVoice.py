import sys,threading
import pyaudio,wave

from PyQt5.QtWidgets import QApplication,QVBoxLayout,QPushButton,QWidget

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output_test.wav"
RECORDING = False


def record_thread(fileName, stream, p):
    print('recording')
    waveFile = wave.open(fileName, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    while RECORDING:
        waveFile.writeframes(stream.read(CHUNK))
    waveFile.close()
    print('end')

def record_generator(fileName, recordBtn):
    global RECORDING
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
        channels=CHANNELS, rate=RATE,
        input=True, frames_per_buffer=CHUNK)
    while 1:
        recordBtn.setText(u'开始录制')
        yield
        recordBtn.setText(u'停止录制')
        RECORDING = True
        t = threading.Thread(target=record_thread, args=(fileName, stream, p))
        t.setDaemon(True)
        t.start()
        yield
        RECORDING = False

app = QApplication(sys.argv)
mainWindow = QWidget()
layout = QVBoxLayout()
btn = QPushButton()
g = record_generator('output_test.wav', btn)
g.next()
btn.pressed.connect(g.next())
layout.addWidget(btn)
mainWindow.setLayout(layout)
mainWindow.show()
sys.exit(app.exec_())


