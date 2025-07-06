def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'M'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'G'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'T'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'P'
    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')