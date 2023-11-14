from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
import operator
import math 
import re
import numpy as np 

stop_words = set(stopwords.words('spanish') + list(punctuation))
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def getFile(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

        
def clean2(textoTokenizado):
    newTokens = []
    for token in textoTokenizado:
        pattern = r"[^a-zA-Z0-9 \n.,()áéóíúÁÉÍÓÚ]"

        stripped = re.sub(pattern, "", token)

        # Change any whitespace to one space
        stripped = ' '.join(stripped.split())

        # Remove start and end white spaces
        stripped = stripped.strip()
        
        newTokens.append(stripped)
    return newTokens

def clean(textoTokenizado):
    newTokens = []
    for token in textoTokenizado:
        pattern = r"[^a-zA-Z0-9 \n]"

        stripped = re.sub(pattern, "", token)

        # Change any whitespace to one space
        stripped = ' '.join(stripped.split())

        # Remove start and end white spaces
        stripped = stripped.strip()
        
        newTokens.append(stripped)
    return newTokens

def global_frequency(txtClean):

    freq_table = {}
    text = ' '.join(txtClean) #join the cleaned sentences to get the text 
    words = word_tokenize(text)
    for word in words:
        word = word.lower()
        word = ps.stem(word)
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
                
    return freq_table

def get_keywords(txtClean, n):

    freq_table = global_frequency(txtClean)
    #sort in descending order
    freq_table_sorted = sorted(freq_table.items(), key = operator.itemgetter(1), reverse = False) 
    #print(freq_table_sorted)
    keywords = []
    for i in range(0, n):  #taking first 5 most frequent words
        keywords.append(freq_table_sorted[i][0])
    return keywords

def contar_diccionarios_con_palabra(matriz, palabra):
    contador = 0
    for i in range(1, matriz.shape[0]):
        temp = matriz[i, 2]
        if palabra in temp:
            contador += 1
    return contador


def frequency(sentences):
    A = np.empty((len(sentences) + 1, 6), dtype=object)
    for i, sent in enumerate(sentences, start=1):
        words = sent.split()
        count = len(words)
        # numero de palabras por oracion
        A[i, 0] = count
        #frecuencia de palabra en oracion
        A[i, 1] = {}
        #TF de palabra en oracion
        A[i, 2] = {}
        
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            word = ps.stem(word)
            if word not in stop_words:
                if word in  A[i, 1]:
                     A[i, 1][word] += 1
                else:
                     A[i, 1][word] = 1
    
        for word, freq in  A[i, 1].items():
             A[i, 2][word] = freq / count
    
    #se calcula el idf
    for i, sent in enumerate(sentences, start=1):
        A[i, 3] = {}
        for word in A[i, 2]:
            count = contar_diccionarios_con_palabra(A, word)
            #print(word, len(sentences)+1, '/', count, ' = ',len(sentences)+1 / count)
            A[i, 3][word] = math.log(len(sentences)+1 / count)

    # se calcula la TF-IDF
    for i, sent in enumerate(sentences, start=1):
        A[i, 4] = {}
        for word in A[i, 2]:
            A[i, 4][word] = A[i, 2][word] * A[i, 3][word]
            
    return A

def weigh_keywords2(txtClean, A, n):
    keywords = get_keywords(txtClean, n)
    for i in range(1, A.shape[0]):
        for word in A[i, 4]:
            if word in keywords:
                A[i, 4][word] =  A[i, 4][word] * 2
    return A

def get_sent_score2(A):
    for i in range(1, A.shape[0]):
        A[i, 5] = 0
        for word in A[i, 4]:
            A[i, 5] =  A[i, 5] + A[i, 4][word]
    return A

def get_summary2(oraciones, A):
    summary = []
    prom = np.mean(A[1:, 5])
    for i in range(1, A.shape[0]):
        if A[i, 5] > prom:
            summary.append(oraciones[i-1])
    summary = ' '.join(summary)
    return summary


def resumir(file, n):
    texto = getFile(file)
    print(len(texto))
    for i in range(0, n):
        textoTokenizado = sent_tokenize(texto)
        clean1 = clean2(textoTokenizado)
        txtClean = clean(clean1)
        datos = frequency(txtClean)
        datos_modificados = weigh_keywords2(txtClean, datos, 7)
        sentence_info = get_sent_score2(datos_modificados)
        summary = get_summary2(textoTokenizado, sentence_info)
        print(len(summary))
        texto = summary
    return summary
resumen = resumir('texto.txt', 1)

print(resumen)

