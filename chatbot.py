import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highnest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highnest_prob
        highnest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response=True)
    
    response('Estoy bien y tú?', ['como', 'estas', 'va', 'sientes'], required_words=['como'])
    response('Estamos ubicados en la calle 24 número 124', ['ubicados', 'direccion', 'donde', 'ubidación'], single_response=True)
    response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

    best_match = max(highnest_prob, key=highnest_prob.get)
    return unknown() if highnest_prob[best_match] < 1 else best_match

def unknown():
    response = ['¿Puedes decirlo de nuevo? ', 'No estoy seguro de lo que quieres', 'Búscalo en Google a ver qué tal'][random.randrange(3)]
    return response



while True:
    print("BOT: " + get_response(input('TÚ: ')))





