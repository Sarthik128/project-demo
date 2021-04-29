from scipy.io.wavfile import write
import sounddevice

fs = 16000
second = 3

filename = input("Enter the audio name : ")
print("recording...")

while True:
	print("..........")
	record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=1)
	sounddevice.wait()
	write("Recorded/"+filename+".wav",fs,record_voice)
	break

print("recording done...")