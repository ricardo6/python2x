Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from audio_polimorfico import *
>>> ogg = ArchivoOgg("miarchivo.ogg")
>>> ogg.play()
ejecutándose miarchivo.ogg como ogg
>>> 
>>> mp3 = ArchivoMP3("miarchivo.mp3")
>>> mp3.play()
ejecutándose miarchivo.mp3 como mp3
>>> mp3 = ArchivoMP3("miarchivo.wav")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Python33\proyectos\audio_polimorfico.py", line 4, in __init__
    raise Exception("formato archivo inválido")
Exception: formato archivo inválido
>>> 