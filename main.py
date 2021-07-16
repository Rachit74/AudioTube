import youtube_dl
from colorama import init
from colorama import Fore, Style
import time

init()

def run():
    print(Fore.RED + "Welcome to youtube to mp3")
    print(Style.RESET_ALL)
    video_url = input("Enter url:")
    time.sleep(2)
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
        
    print("---------------------------------------------")
    print(Fore.GREEN + f"Download complete... {filename}")

if __name__=='__main__':
    run()
