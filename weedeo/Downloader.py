from moviepy.editor import *


class Cutter():

  '''
  inheriting this allows to accept []
  '''
  # value = 0
  boundaries = []

  def __getitem__(self, i):
    if type(i) is slice:
      print(i)
        # if i != 0:
            # raise IndexError("this container can only hold one object")
    return self.boundaries[i]


# a = Cutter()

# make timeline - where clips gonna ge stored and order can be operated
class Timeline():

  pass

  # def 

class WeeLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

class WeeClip(VideoFileClip, Cutter):

  def __init__(self, filename):
    super(WeeClip, self).__init__(filename)
    # VideoFileClip()

  # def 

class Downloader():

  def __setitem__():
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
 
        self.marks[key] = value
    

  def __init__(self, link):
    Downloader_YoutubeDl(link)
    
  # def __get__():
    # sd
    
class Downloader_YoutubeDl(Downloader):

  bounds = []

  def _check_meta():
    

  def _check_duration():
    self.ydl_opts = ydl_opts("7:56", "8:05")

  def __getitem__(self, i):
    returnself.bounds[i]
    # if i != 0:
      # raise IndexError("this container can only hold one object")
      # return self.value

  def __init__(self, links):

    self.ydl_opts = ydl_opts("7:56", "8:05")
    # download_video(links)
    with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
      dictMetas = {}
      for link in links:
        dictMetas[link] = ydl.extract_info(link,
          download=True)
        # if
        print("debug") 
        print(dictMetas[link])
      video = ydl.download(links)


def process_video_hook(d):
    if d['status'] == 'finished':
      print(d)
      filename = d['filename']
      # print(filename)
      clip = WeeClip(filename)
      # [1:2]
      # WeedeoFile("")
      clip.subclip(1,2).write_videofile("test.mp4")
      # clip = random_sequence(filename)
      # video = WeedeoClip(filename)


``
def ydl_opts(t_from, t_to):
  return {
    'verbose': True,
    'format': 'best',  #format,vebrose,ottmpl
    'outtmpl': f'%(title)s-%(id)s-{t_from}-{t_to}-.%(ext)s', # add timestamps
    'logger': WeeLogger(),                  #options
    'progress_hooks': [process_video_hook],             # how can i find
    'external_downloader':"ffmpeg",
    "external_downloader_args": ["-ss", t_from, "-to", t_to]
    # ,
    # "download_archive": "downloaded.txt"
}



# video_adresses=['https://www.youtube.com/watch?v=Os-E0g96cxE', 'https://www.youtube.com/watch?v=bgsD23wCTQM'] #+ ['https://www.youtube.com/watch?v=iJK2QiH6Mf4'] # чувак, это рэпчик
video_adresses=['https://www.youtube.com/watch?v=57vv4meBMB8'] #+ ['https://www.youtube.com/watch?v=iJK2QiH6Mf4'] # чувак, это рэпчик
# for address in video_adresses:
  # print(address)
Downloader(video_adresses)
a = Cutter()
a
# [11:14:0]
# a
# [0]
