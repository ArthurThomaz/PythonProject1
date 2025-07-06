import os
from utils import formata_tamanho
path_finder = '/users/Arthu/Videos/TWICE 07.02'
search_term = 'GONE'
conta = 0
for raiz, diretorios, arquivos in os.walk(path_finder):
    for arquivo in arquivos:
        if search_term in arquivo:
            try:
                conta += 1
                full_path = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(full_path)
                print()
                print(f'Encontrei o arquivo {arquivo}')
                print('Caminho:', full_path)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', formata_tamanho(tamanho))
            except PermissionError as e:
                print('You dont have permission to access this file.')
            except FileNotFoundError as e:
                print('File not found.')
            except Exception as e:
                print('Something went wrong.')
print()
if conta == 1:
    print(f'{conta} file found.')
elif conta > 1:
    print(f'{conta} files found.')