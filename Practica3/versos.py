def countPoem(file):
    versos, nWords = 0,0
    poem = open(file,'r', encoding='utf-8')
    for linea in poem:
        if not(linea.startswith('\n')): 
            versos += 1
            for word in linea:
                nWords += 1
    return versos, nWords