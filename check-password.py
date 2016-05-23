# Get a password to test.
password = raw_input("Tell me your password, and I'll tell you how long it'll take to guess    :: ")

def guess_password(password):
    count = 0
    for source in ["1000000.txt", "all_words.txt"]:
        with open(source, "r") as password_source:
            for guess in password_source.readlines():
                guess = guess.strip("\n")
                count += 1
                if password.lower() == guess.lower():
                    return count

    # We didn't guess from the first 1,000,000 passwords. How about simple English words?
    #  ...TODO: compound words, like "correcthorsebatterystaple". Some words are more predictable than others, so the overall entropy actually isn't too massive.

    # The password wasn't guessed from the simple dictionary attack, so what's the overall entropy?
    # For now, let's assume 128 ascii chars -> 7 bits of entropy per char.
    h = 94 ** len(password)
    count += h
    return count

# Guesses per second from https://security.stackexchange.com/questions/43683/is-it-possible-to-brute-force-all-8-character-passwords-in-an-offline-attack
guesses = guess_password(password)
seconds_basic = guesses / 1000000000
seconds_encryption = guesses / 364000
seconds_WPA = guesses / 1500

print "Apparently, I'd have guessed " + password + " in " + str(guesses) +" tries, using very naive methods!"

# From https://stackoverflow.com/questions/775049/python-time-seconds-to-hms:
m_basic, s_basic = divmod(seconds_basic, 60)
h_basic, m_basic = divmod(m_basic, 60)
m_encryption, s_encryption = divmod(seconds_encryption, 60)
h_encryption, m_encryption = divmod(m_encryption, 60)
m_WPA, s_WPA = divmod(seconds_WPA, 60)
h_WPA, m_WPA = divmod(m_WPA, 60)

print
print "To crack that as a regular password, it would take\t %dh %02dm %02ds." % (h_basic, m_basic, s_basic)
print "To crack that as an encryption password, it would take\t %dh %02dm %02ds." % (h_encryption, m_encryption, s_encryption)
print "To crack that as a wifi password, it would take\t %dh %02dm %02ds." % (h_WPA, m_WPA, s_WPA)
print
