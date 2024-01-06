from silabas import veriVocals, silabas, printSilabas
def hayAcento(word):
    for letra in word.lower():
        if letra in 'áéíóú':
            return True
    return False

def getTypeWord(sylls, word):
    for i, syl in enumerate(reversed(sylls)):
        if (i == 0 and hayAcento(syl)) or (word.lower() in palabrasAgudas):
            return 'aguda'
        elif (i == 1 and hayAcento(syl)) or (word.lower() in palabrasGraves):
            return 'grave'
        elif (i == 2 and hayAcento(syl)):
            return 'esdrujula'
        elif (i == 3 and hayAcento(syl)):
            return 'sobre'
        else:
            return 'idk'
        
        
palabrasAgudas = [
    'abaratar', 'diluviar', 'maltratar',
    'abarcar', 'diseminar', 'mandar',
    'aborrecer', 'disentir', 'manipular',
    'acalorar', 'disgregar', 'mencionar',
    'acatar', 'doblez', 'mendigar',
    'aceptar', 'dominar', 'mental',
    'acicalar', 'dramatizar', 'mudar',
    'acomodar', 'dorar', 'mundial',
    'acoplar', 'dudar', 'musical',
    'acorralar', 'ecuatorial', 'musicalizar',
    'acusar', 'edificar', 'natural',
    'adaptador', 'embarcar', 'naturalidad',
    'adecuar', 'embaucar', 'necedad',
    'adiestrador', 'emplazar', 'necesidad',
    'adivinar', 'empezar', 'negociar',
    'adjudicador', 'emprendedor', 'neonatal',
    'adjudicar', 'encantar', 'neutral',
    'administrar', 'encasillar', 'obesidad',
    'admirador', 'encontrar', 'obsequiar',
    'adoptar', 'enfocar', 'obsesionar',
    'adorar', 'ensillar', 'ocupar',
    'aerosol', 'entrometer', 'ofender',
    'afectar', 'escolar', 'oficial',
    'afinidad', 'esconder', 'oficiar',
    'alcanzar', 'escribir', 'ofrendar',
    'ampliar', 'esencial', 'orientador',
    'animar', 'espiritual', 'oriental',
    'animosidad', 'establecer', 'orinar',
    'aniquilar', 'estipular', 'patinar',
    'anticipar', 'evadir', 'percibir',
    'ascender', 'expedir', 'peritoneal',
    'asesinar', 'explorar', 'persuadir',
    'asesor', 'facilitar', 'plantar',
    'asiduidad', 'favorecer', 'policial',
    'atender', 'febril', 'prometer',
    'atrocidad', 'financiar', 'proseguir',
    'azuzar', 'fragilidad', 'pulidor',
    'balancear', 'frivolidad', 'purificar',
    'billar', 'funcionar', 'racional',
    'bimestral', 'ganar', 'racionar',
    'binocular', 'garantizar', 'real',
    'blanqueador', 'generar', 'rectangular',
    'blanquear', 'generosidad', 'regresar',
    'borrar', 'genial', 'rentar',
    'bostezar', 'girar', 'reptar',
    'boxear', 'glacial', 'rescatar',
    'brevedad', 'glaciar', 'ritual',
    'bronceador', 'gladiador', 'rumiar',
    'brutal', 'gratitud', 'saborear',
    'burbujear', 'guardar', 'sacar',
    'cabezal', 'habitual', 'salar',
    'caducidad', 'habituar', 'salir',
    'calentar', 'hexagonal', 'saludar',
    'cantar', 'hostal', 'salvador',
    'cantor', 'hotel', 'sanear',
    'cañaveral', 'humedad', 'sanidad',
    'capacidad', 'humedecer', 'santidad',
    'causal', 'hundir', 'santiguar',
    'cavidad', 'implicar', 'separar',
    'cazar', 'importar', 'simpatizar',
    'central', 'incondicional', 'sobrenatural',
    'cepillar', 'inferior', 'soldar',
    'colocar', 'infiltrar', 'sumar',
    'combatir', 'ingenuidad', 'superior',
    'compensar', 'inicial', 'tejer',
    'competir', 'inmoral', 'timador',
    'compresor', 'insinuar', 'trabajar',
    'consolar', 'integridad', 'traer',
    'contener', 'interior', 'traicionar',
    'continental', 'interpretar', 'trasplantar',
    'contrariedad', 'intrigar', 'ungir',
    'contribuir', 'jalar', 'unidad',
    'corral', 'jocosidad', 'universal',
    'costillar', 'judicial', 'untar',
    'cruzar', 'jugar', 'urbanidad',
    'dejar', 'jurar', 'vecindad',
    'delinquir', 'justificar', 'ventilar',
    'denigrar', 'laminar', 'veracidad',
    'dental', 'legitimidad', 'verdad',
    'depositar', 'lesionar', 'vitorear',
    'desesperar', 'maldecir', 'vivir',
    'desperdiciar', 'memorizar', 'vivenciar','azar'
]


palabrasGraves = [
    'abanderado', 'cocinero', 'mesa',
    'abandonado', 'colcha', 'mochila',
    'abanico', 'colmillo', 'muestra',
    'abarrotado', 'colombia', 'mueve',
    'abarrotes', 'comadreja', 'nubes',
    'abasto', 'come', 'nublado',
    'abeja', 'como', 'ojos',
    'abortivo', 'compra', 'olas',
    'abrasivo', 'computadora', 'ombligo',
    'abrigo', 'conjuro', 'ordena',
    'absoluto', 'consume', 'organiza',
    'abuela', 'corre', 'oso',
    'abuelo', 'corrige', 'pantera',
    'acarreo', 'corta', 'para',
    'acondicionado', 'cortinas', 'parlante',
    'acuarela', 'cuaderno', 'pecas',
    'acuario', 'cuadro', 'peces',
    'acusado', 'cuanto', 'pecho',
    'administrativo', 'cuchara', 'pelo',
    'adorno', 'cuchillo', 'pera',
    'aduana', 'cuello', 'pera',
    'adulto', 'cuenta', 'perfume',
    'adulto', 'desordena', 'perro',
    'adultos', 'diente', 'pestañas',
    'agua', 'disco', 'piedra',
    'aire', 'domingo', 'pierna',
    'alcantarilla', 'elefante', 'pintura',
    'alfombra', 'elefante', 'piscis',
    'almacena', 'empresa', 'plancha',
    'almohada', 'enchufe', 'planeta',
    'amarillo', 'enojo', 'planifica',
    'amazonas', 'ensalada', 'playa',
    'analiza', 'escorpio', 'pluma',
    'anonadada', 'escribe', 'pone',
    'antes', 'espera', 'poroto',
    'anulares', 'estadio', 'puerto',
    'arena', 'estima', 'quien',
    'argentina', 'estrellas', 'rama',
    'arrecife', 'estructura', 'recibe',
    'asume', 'estudia', 'redacta',
    'atento', 'estupefacta', 'regla',
    'avispa', 'eugenesia', 'remera',
    'balanza', 'eugenia', 'resumen',
    'banana', 'figura', 'revisa',
    'banana', 'flaca', 'rinoceronte',
    'banco', 'folio', 'roca',
    'bandada', 'fruta', 'rompe',
    'bandido', 'fuente', 'ropa',
    'baño', 'galaxias', 'rosario',
    'banquero', 'ganado', 'saludo',
    'bota', 'gases', 'santo',
    'botana', 'gato', 'serio',
    'bote', 'genio', 'signos',
    'buena', 'gordo', 'silla',
    'bufanda', 'guitarra', 'sorprendida',
    'busca', 'gusano', 'suerte',
    'caballo', 'hormigas', 'superpone',
    'cabello', 'ingenio', 'surge',
    'cable', 'intento', 'tamarindo',
    'cachetes', 'jirafa', 'tapado',
    'cadera', 'juega', 'teclado',
    'calzado', 'jueves', 'teclas',
    'cama', 'jueves', 'temperatura',
    'caminata', 'jugo', 'termo',
    'camisa', 'ladrillo', 'tetilla',
    'camiseta', 'leche', 'tierra',
    'camote', 'libro', 'tocadiscos',
    'campo', 'limpieza', 'toma',
    'capricornio', 'llueve', 'tonto',
    'cara', 'lluvia', 'trampa',
    'cardumen', 'lunar', 'trapo',
    'carmen', 'lunes', 'universo',
    'carpeta', 'maestra', 'vaca',
    'cejas', 'mala', 'vaso',
    'chango', 'manda', 'vende',
    'chaqueta', 'manteca', 'venga',
    'chile', 'manzana', 'vicuña',
    'choclo', 'mariano', 'viernes',
    'cielo', 'martes', 'volumen',
    'clavo', 'martillo', 'vuelo',
    'cloaca', 'mate', 'vuelos',
    'cocina', 'media', 'zapatillas',
    'cocina', 'memoriza', 'zapato'
]


def veriSinalefa(w1, w2):
    if veriVocals(w1[-1]) != False:
        if (veriVocals(w2[0]) != False) or (w2[0] in 'hH' and veriVocals(w2[1]) != False):
            return True
    return False

def metricasVerso(palabrasVerso):
    newVerso = ''
    countsyl = 0
    counSinalefa = 0
    for i, palabra in enumerate(palabrasVerso):
        sylls = silabas(palabra)
        countsyl += len(sylls)
        newVerso += printSilabas(palabra)
        if i != len(palabrasVerso)-1:
            if veriSinalefa(palabra, palabrasVerso[i+1]):
                counSinalefa += 1
            else:
                newVerso += ' '
    if getTypeWord(sylls, palabrasVerso[-1]) == 'esdrujula':
        countsyl -= 1
    if getTypeWord(sylls, palabrasVerso[-1]) == 'aguda':
        countsyl += 1
    countsyl-=counSinalefa
    newVerso += '\t' + str(countsyl) + ' Silabas'
    if counSinalefa != 0: 
        newVerso += '\t' + str(counSinalefa) + ' Sinalefas'
        
    return newVerso
