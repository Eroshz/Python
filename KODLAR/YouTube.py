from pytube import YouTube
import time
import youtube_dl

print("                  ---> Video İndirme Programına Hoşgeldiniz <---")
print("                                  made by Eroshz")
time.sleep(2)

islem_sec = int(input("Yapmak İstediğiniz İşlemi Seçin: \n1-) Video İndirici \n2-) MP3 İndirici \n (İşleminizi 1 veya 2 Olarak Girin) \n---> " ))
islem = islem_sec

def mp3():
    video_url = input("İndirmek İstediğiniz Videonun Linkini Girin: \n---> ")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Başarıyla İndirildi {}".format(filename))


def mp4():
    link = input("İndirmek İstediğiniz Videonun Linkini Girin: \n---> ")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("---> İndiriliyor...")
    ys.download()
    print("---> Video Başarıyla İndirildi")

if islem_sec == 1:
    mp4()
else:
    mp3()

