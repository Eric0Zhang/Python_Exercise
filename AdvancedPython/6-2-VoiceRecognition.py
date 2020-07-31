#coding:utf-8
import json
import os
# 录音
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 10

def rec(file_name):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音,请说话......")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束,请闭嘴!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

rec('temp.wav')

def get_file_content(filePath):
    os.system(f"D:/ffmpeg-20180619-a990184-win64-shared/bin/ffmpeg -y  -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

# 调用百度语音识别API
from aip import AipSpeech
APP_ID = '21677732'
API_KEY = 'K7fpclFOcA3hGaNTVLvp6kuQ'
SECRET_KEY = 'TkD1nwEQfLELKFTssGbUqULRAuGU7DZI'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#client.setConnectionTimeoutInMillis(5000)
#client.setSocketTimeoutInMillis(5000)

resp = client.asr(get_file_content('temp.wav'), 'pcm', 16000, {'dev_pid':1537,})
print("*"*30)
print(resp.get("result")[0])
print("*"*30)