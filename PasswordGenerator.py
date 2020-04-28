def generatePasswords(lengthOfPasswords, numberOfPasswords):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@.'
    passwords = []
    for p in range(numberOfPasswords):
        password = ''
        for c in range(lengthOfPasswords):
            password += (random.choice(chars))
        passwords.append(password)
    return passwords
