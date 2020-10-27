'''
ffmpeg é uma ferramenta poderosa para conversão de vídeos
Em linux o comando utilizado pe ffmpeg

'''
import os
import fnmatch
import sys

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = ''

caminho = os.path.join(os.getcwd(), 'Exercicios/videos')

for raiz, pastas, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'ffmpeg -i "{caminho_completo}" ' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            f'{debug} "{arquivo_saida}"'

        os.system(comando)



