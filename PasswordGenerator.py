import random

def password_maker(password_length):
    possible_characters = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i",
                           "o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",
                           "Q","W","E","R","T","Y","U","I","O","P","A",'S','D','F','G','H','J','K',
                           'L','Z','X','C','V','B','N',"@","#","!","$","%","^","&",'*',"(",")","?",
                           "<",">","{","}","[","]","-","+"]
    random.shuffle(possible_characters)
    final_password = ""
    i = int(0)
    while i < password_length:
        final_password += possible_characters[random.randint(0,len(possible_characters)-1)]
        i += 1
    return final_password

password_length = int(input("Enter password Length: "))
print(password_maker(password_length))
