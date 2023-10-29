from pydub import AudioSegment
import os

#m4a_file = '/home/prabhjot/Desktop/seamless/punjabi/valid/audio/844424930560952-973-f.m4a' # I have downloaded sample audio from this link https://getsamplefiles.com/sample-audio-files/m4a
#wav_filename = '/home/prabhjot/Desktop/seamless/844424930560952-973-f.m4a.wav'

#sound = AudioSegment.from_file(m4a_file, format='m4a')
#file_handle = sound.export(wav_filename, format='wav')

def Convert_2_wav(rootdir):
 
 count = 0
 for file in os.listdir(rootdir): #Read contents in this directory
    filename  = os.fsencode(file)
    filename = filename.decode()
   # print(filename)
    

    if filename.endswith(".m4a"):
      audio_path = os.path.join(rootdir, filename)
      #print(audio_path)     

      wav_file = os.path.splitext(filename)[0] + '.wav' #name the file with .mp3 extension
      path_to_save = (os.path.join(rootdir,wav_file))
      ##print(path_to_save)

      sound = AudioSegment.from_file(audio_path, format='m4a')
      sound.export(path_to_save, format="wav")

      count = count+1
      #print(count)

if __name__ == "__main__":
  rootdir = "/home/prabhjot/Desktop/seamless/Punjabi/audio"
  Convert_2_wav(rootdir)