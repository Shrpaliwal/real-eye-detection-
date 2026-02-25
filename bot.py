import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response= False, required_words=[]):
    if required_words is None:
        required_words = []
    message_certainity = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainity += 1

    # calculates the percentage of recognised words in a user message
    percentage = float(message_certainity)/float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_message(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

# response ------------------------------------------------------------------------------------------------------------
    response('hello!',['hello','hi','whatsup','hey','namaste','hii','kemcho'],single_response=[True])
    response(long.R_RAM,['jay','shri','ram'], required_words=['jay','shri','ram'])
    response('I\'m doing fine, what about you?',['how','are','you','doing'], required_words=['how'])
    response('Thank you!',['i','loved','to','talk','to','you'], required_words=['loved','talk','to','you'])
    response(long.R_EATING,['what','you','eat'], required_words=['you','eat'])
    response('how can i help you...',['not','feeling','well'], required_words=['not','feeling','good'])
    response('its my pleasure' ,['thank','you'], required_words=['thank','you'])
    response(long.R_FESTIVAL,['hindu','festival',], required_words=['hindu','festival'])
    response(long.R_FEST,['krishna','janamashtmi'], required_words=['krishna','janamashtmi'])
    response(long.R_GANESH,['ganesh','chaturthi','chaut','chauth','chaturti'], required_words=['ganesh'])
    response(long.R_WEATHER,['weather','mausam','baarish'], required_words=['weather'])
    response(long.R_QUES,['egg','hen'],required_words=['hen','egg'])
    response(long.R_JOKE,['tell','me','joke'],required_words=['joke'])
    response('thanks buddy.',['thats','funny'],required_words=['funny'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
def get_response(user_input):
    split_message = re.split(r'\s+|[,;:!?.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response


# testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))