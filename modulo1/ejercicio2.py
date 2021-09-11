def sustitucion(plaintext):
    nuevoabc = 'JTREKYAVOGDXPSNCUIZLFBMWHQ'
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    for i in plaintext :
        ciphertext += nuevoabc[abc.find(i.upper())]
    print(f'ciphertext: {ciphertext}.')
    return ciphertext

texto = sustitucion(input('plaintext: '))