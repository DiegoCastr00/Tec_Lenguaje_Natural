def getrecord(arr, record):
    newLen = len(arr) - len(record)
    return arr[newLen:-1]

def veriConsonant(letter):
    consonants = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
    if letter in consonants:
        return True
    return False

def veriVocals(letter):
    vocals = 'aeiouAEIOU'	
    vocalsTilde = 'áéíóúÁÉÍÓÚ'
    if letter in vocals:
        return 'sin'
    elif letter in vocalsTilde:
        return 'con'
    return False

def defineLetters(word):
    types = ''
    for letter in word:
        if veriConsonant(letter):
            types += 'C'
        else:
            types += 'V'
    return types

def typeVocal(word):
    vocals = ''
    fuertes = 'aeoáéó'
    debiles = 'iuíú'
    for letter in word:
        if letter in fuertes:
            vocals += 'F'
        elif letter in debiles:
            vocals += 'D'
        else:
            #cosonante 
            vocals += 'C'
    return vocals
                
def wordNoAccent(word):
    return word.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u'). replace('ü','u')

def sameV(word):
    noAcc = wordNoAccent(word)
    if noAcc[0] != noAcc[1]:
        return False
    else:
        return True
    
    
def identify(word):
    types = []
    consonants = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
    fuertes = 'aeoAEO'
    debiles = 'iuIU'
    fuertesA = 'ÁÉÓáéó'	
    debilesA = 'íúÍÚ'
    for letter in word:
        if letter in consonants:
            types.append('C')
        elif letter in fuertes:
            types.append('F')
        elif letter in fuertesA:
            types.append('Fa')
        elif letter in debiles:
            types.append('D')
        elif letter in debilesA:
            types.append('Da')
    return types

def regla1(word, syllables):
    pos = 0
    if veriConsonant(word[0]):
        for i, l in enumerate(word):
            if veriVocals(l) == 'sin' or veriVocals(l) == 'con':
                syllables.append(word[0:i+1])
                pos = i+1
                break
    return syllables, pos


def veriDiptongo(v1, v2):
    cadena = v1 + v2
    ty = identify(cadena)
    ty= ty[0]+ ty[1]
    print(ty)
    if ty == 'FD'  or ty == 'DF' or ty == 'DD' or ty == 'DFa':
        return 'juntas'
    else:
        return 'separadas'
    
def silabas(word):
    syllables = []
    types = defineLetters(word)
    explicit = identify(word)
    #syllables, ini = regla1(word, syllables)
    ini = 0
    newTypes = types[ini:len(word)+1]
    recordW = word[ini:len(word)+1]
    i = ini
    while i != len(word):
        newTypes = types[i:len(word)+1]
        #print(i, newTypes, syllables) 
        recordW = word[i:len(word)+1]
        explicit = explicit[i:len(word)+1]
        if 'VCV' in newTypes:
            if newTypes.index('VCV') == 0 :
                #print('entro a VCV')
                if (recordW[1] not in 'qg' and recordW[2] not in 'uü'):
                    syllables.append(recordW[0])
                    syllables.append(recordW[1] + recordW[2])
                    i += 3
                    continue
                else: 
                    syllables.append(recordW[0])
                    i += 1
                    continue
        if 'V' in newTypes:
            if newTypes.index('V') == 0:
                #print('entro a V')
                if syllables != [] and veriVocals(syllables[-1][-1]) != False:
                    #print('entro a V 1', veriDiptongo(syllables[-1][-1], recordW[0]))
                    if veriDiptongo(syllables[-1][-1], recordW[0]) == 'juntas':
                        syllables[-1] += (recordW[0])
                        i+=1
                        continue
                else: 
                    syllables.append(recordW[0])  
                    i+=1
                    continue
        #triptongo
        if 'CVVV' in newTypes:
            if types.index('CVVV') == 0:
                #print('entro a CVVV')
                #fuertes = abiertas
                # U insonora
                if (recordW[0] in 'gq' and recordW[1] in 'uü' and recordW[2] in 'ei'):
                    if veriDiptongo(recordW[2], recordW[3]) == 'juntas':
                        syllables.append(recordW[0]+recordW[1]+recordW[2]+recordW[3])
                        i += 4
                        continue
                    else:
                        syllables.append(recordW[0]+recordW[1]+recordW[2]+recordW[3])
                        i += 4
                        continue
                else:
                    if (explicit[1] == 'D' and explicit[2] == 'F' and explicit[3] == 'D') or (explicit[1] == 'D' and explicit[2] == 'Fa' and explicit[3] == 'D'):
                        syllables.append(recordW[0]+recordW[1]+recordW[2]+recordW[3])
                        i += 4
                        continue
                    
        if 'CVV' in newTypes:
            #print('entro CVV 1')
            if newTypes.index('CVV') == 0:
                #print('entro CVV')
                #print(explicit)
                #diptongo excepcion
                                
                if (recordW[0] in 'gq' and recordW[1] in 'uü' and recordW[2] in 'ei'):
                    #print('entro aquiiii 2')
                    syllables.append(recordW[0]+recordW[1]+recordW[2])
                    i += 3
                    continue
                #hiatos 
                if (explicit[1] == 'F' and explicit[2] == 'Da') or (explicit[1] == 'Da' and explicit[2] == 'F') or ( explicit[1] == 'F' and explicit[2] == 'F'):
                    #C F Da
                    #print('entro al tercero', explicit)
                    syllables.append(recordW[0]+recordW[1])
                    syllables.append(recordW[2])
                    i += 3
                    continue
                #diptongo
                if (explicit[1] == 'D' and explicit[2] == 'D'):
                    #print('entro al cuarto', explicit)
                    syllables.append(recordW[0] + recordW[1] + recordW[2])
                    i += 3
                    continue
                if (explicit[1] == 'D' and explicit[2] == 'F'):
                    #print('entro al quinto', explicit)
                    syllables.append(recordW[0] + recordW[1] + recordW[2])
                    i += 3
                    continue
        if 'CV' in newTypes:
            if newTypes.index('CV') == 0:
                #print('entro a CV')
                syllables.append(recordW[0] + recordW[1])
                i += 2
                continue
        if 'CCV' in newTypes:
            if newTypes.index('CCV') == 0:
                #print('entro a CCV')
                indiceI = newTypes.index('CCV')
                if (recordW[0:2]) in ['pr','br','dr','cr','fr', 'gr','kr','tr','fl', 'pl','gl','kl','cl','bl']:
                    #print('entro a CCV 1')
                    syllables.append(recordW[indiceI] + recordW[indiceI+1] + recordW[indiceI+2] )
                    i+=3 
                    continue
                
                #print(recordW[0:2])                   
                if recordW[0:2] in ['ch','rr', 'll']:
                    #print('entro a CCV 2')
                    if syllables != [] and veriConsonant(syllables[-1][-1]) != False:
                        syllables[-1] += recordW[0]
                        syllables.append(recordW[1] + recordW[2])
                        i += 3
                        continue
                    else:
                        syllables.append(recordW[0] + recordW[1] + recordW[2])
                        i += 3
                        continue
                elif recordW[1:3] in ['gu','gü', 'qu']: 
                    #print('entro a CCV 4')
                    if syllables != [] and veriConsonant(syllables[-1][-1]) == False:
                        syllables[-1] += recordW[0]
                        syllables.append(recordW[1] + recordW[2] + recordW[3])
                        i += 4
                else:
                    #print('entro a CCV 3')
                    if syllables != []:
                        syllables[-1] += (recordW[0])
                        syllables.append(recordW[1]+recordW[2]) 
                        i+=3      
                        continue
        if 'CCCV' in newTypes:
            if syllables != []:
                if newTypes.index('CCCV') == 0 and veriVocals(syllables[-1][-1]) != False:
                    #print('entro a CCCV')
                    if recordW[2] in ['l', 'r']:
                        syllables[-1] += (recordW[0])
                        syllables.append(recordW[1] + recordW[2] + recordW[3])
                        i += 4
                        continue
                    else:
                        syllables[-1] += (recordW[0] + recordW[1])
                        syllables.append(recordW[2] + recordW[3])
                        i += 4
                        continue
        if 'CCCCV' in newTypes:
            if syllables != []:
                if newTypes.index('CCCCV') == 0 and veriVocals(syllables[-1][-1]) != False:
                    #print('entro a CCCCV')
                    syllables[-1] += (recordW[0])
                    syllables.append(recordW[1] + recordW[2] + recordW[3] + recordW[4])
                    i += 5
                    continue
        if 'C' in newTypes and not('V' in newTypes):
            if syllables != []:
                syllables[-1] += recordW
                i += len(newTypes)
                continue
    return syllables  


def printSilabas(word):
    res = ''
    arrSyl = silabas(word)
    for i, sil in enumerate(arrSyl):
        if i == len(arrSyl)-1:
            res += sil + ""
        else:
            res += sil + "-"
    return res