from pytube import YouTube

#função que baixa o vídeo cujo link foi dado pelo usuário:
def baixar(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    titulo = video.title
    if input("\nVocê deseja mesmo fazer o download do vídeo '{}'? (s/n)\n ".format(titulo.upper())) == "s":
        try:
            video.download()
            print("\033[0;49;32mSUCESSO!\033[m")
        except:
            print("\033[0;49;91mDesculpe, mas um erro ocorreu :/\033[m")

link = input("Insira o link do vídeo que quer baixar: ")
baixar(link)