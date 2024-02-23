from thinkdsp import SquareSignal

signal = SquareSignal(1100)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=40000)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=1, framerate=40000)
wave.apodize()
wave.make_audio()
