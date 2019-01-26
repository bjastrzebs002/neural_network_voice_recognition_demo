
# coding: utf-8

# In[10]:


import pyaudio
import wave
from array import array
import sys

# In[11]:


def record_start(name):
    FORMAT=pyaudio.paInt16
    CHANNELS=2 
    RATE=44100
    CHUNK=1024
    RECORD_SECONDS=1.5
    FILE_NAME=name
    audio=pyaudio.PyAudio() #instantiate the pyaudio

    #recording prerequisites
    stream=audio.open(format=FORMAT,channels=CHANNELS, 
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

    #starting recording
    frames=[]
    print("start of recording")
    for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data=stream.read(CHUNK)
        data_chunk=array('h',data)
        vol=max(data_chunk)
        if(vol>=500):
            frames.append(data)


    print("end of recording")
    #end of recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    #writing to file
    wavfile=wave.open(FILE_NAME,'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(audio.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))#append frames recorded to file
    wavfile.close()


# In[ ]:


if __name__ == "__main__":
    name = sys.argv[1]
    record_start(name)

