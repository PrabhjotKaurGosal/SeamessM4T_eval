import os


def Delete_m4a_files(rootdir):

  count = 0
  for file in os.listdir(rootdir):
    filename  = os.fsencode(file)
    filename = filename.decode()

    if filename.endswith(".m4a"):
      audio_path = os.path.join(rootdir, filename)
      #print(audio_path)
      os.remove(audio_path)
      count = count+1
      #print(count)
     

if __name__ == "__main__":
  rootdir = "/home/prabhjot/Desktop/seamless/punjabi/valid/audio"
  Delete_m4a_files(rootdir)