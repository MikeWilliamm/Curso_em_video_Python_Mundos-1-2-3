import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/MikeWilliamm/Curso_em_video_Python_Mundos-1-2-3/tree/master/Modulo03')
except:
    print('deu erro')
else: 
    print('tudo ok')
    print(site.read()) #Lé estrutura do site completa