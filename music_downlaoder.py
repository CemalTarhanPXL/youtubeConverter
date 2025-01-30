from yt_dlp import YoutubeDL

ffmpeg_location = 'C:/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/'

# Voeg de optie toe voor post-processing om de audio naar MP3 te converteren
audio_downloader = YoutubeDL({
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
   'ffmpeg_location':ffmpeg_location,
})

while True:
    try:
        print('Youtube Downloader'.center(50, '-'))
        URL = input('Enter the URL of the video: ')
        audio_downloader.extract_info(URL)
    
    except Exception:
        print('Invalid URL. Try again.')
    
    finally:
        option = int(input('Als je nog iets wilt downloaden druk op 1 en enter. Als je wilt sluiten druk op 0 en enter.(Kies 1 of 0 )'))
        if option == 0:
            break