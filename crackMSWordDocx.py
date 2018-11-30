# Done by Sangameswaran R S
import msoffcrypto
from nltk.corpus import brown


def check_password(passwordC):
    try:
        file = msoffcrypto.OfficeFile(open("Crack Me.docx", "rb"))
        file.load_key(password=passwordC)
        file.decrypt(open("decrypted.docx", "wb"))
        return True
    except Exception as e:
        print("INCORRECT PASSWORD")
    return False


def entry_point():
    wordlist = brown.words()
    for word in wordlist:
        flag = check_password(word)
        if flag:
            print('Password is :'+str(word))
            print("OPEN DECRYPTED.DOCX")
            break


entry_point()
