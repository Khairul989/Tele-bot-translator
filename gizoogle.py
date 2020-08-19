from googletrans import Translator
import googletrans


def translateText(input_text, user_name):
    translator = Translator()
    r = input_text  # hi
    # result=''
    try:

        if r.find('/start') != -1:
            return "Hello, {}. 🤖\n\nTry the /help command for assistance.\n>> Instructions: \n\t /start - to start " \
                   "the bot \n\t /help - How to use this bot \n\t /lang - Display available languages".format(
                user_name)

        elif r.find('/help') != -1:
            return "\nHow do I use this translator ?\n\n> Desired Language: Text \n> Example:\n \t \t ja: Saya budak baru belajar."\
                   "Note(Desired language and input text must not have any quotation symbol)\n\n To see " \
                   "all available languages try the /lang command.\n "

        elif r.find('/lang') != -1:
            return googletrans.LANGUAGES

        elif r.find(':') == -1:
            return "You have entered an invalid input, {}. 😡\n\n /start - to start the bot".format(
                user_name)

        elif r[2] == ':':
            s = r[3:]
            lan = r[0:2]
            result = translator.translate(s, dest=lan)

        elif r[3] == ':':
            s = r[4:]
            lan = r[0:2]
            result = translator.translate(s, dest=lan)
            # googletrans.LANGUAGES

        return result.text

    except:
        return "Failed to translate. 🛑\nTry the /help command for guidelines."
