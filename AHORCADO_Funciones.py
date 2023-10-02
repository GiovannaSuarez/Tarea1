# AHORCADO_FUNCIONES
def check_word(letter,word,hidden_word):
    checker = hidden_word
    hidden_word = list(hidden_word)
    for i in range(0,len(word),1):
        if word[i]==letter:
            hidden_word[i]=letter
    hidden_word = "".join(hidden_word)
    return hidden_word

def already_used(used_words, letter):
    used_words = list(used_words)
    used_words.append(letter)
    used_words = "".join(used_words)
    return used_words

            


