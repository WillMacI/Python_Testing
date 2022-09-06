#msg to be encrypted
orig_msg = input("Msg to encrypt:");
msg_upper = orig_msg.upper()
msg_stripped = msg_upper.replace(" ", "");
#key to be used
key = input("Encryption key:");
key_upper = key.upper();
#alphabet
alphabet = ["", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
count = 0;
encrypted_msg = [];
for msg_letter in msg_stripped:
    if count == len(key_upper):
        count = 0;
    #find pos of letter in alphabet
    msg_letter_pos = alphabet.index(msg_letter);
    key_letter = key_upper[count];
    key_letter_pos = alphabet.index(key_letter);
    new_letter_pos = msg_letter_pos + key_letter_pos;
    count = count + 1;
    if (new_letter_pos > 27):
        new_letter_pos = new_letter_pos - 26;
        new_letter_pos = new_letter_pos - 1;
        new_letter = alphabet[new_letter_pos];
        encrypted_msg.append(new_letter);
    else:
        new_letter_pos = new_letter_pos - 1;
        new_letter = alphabet[new_letter_pos];
        encrypted_msg.append(new_letter);
encrypted_msg = ' '.join([str(elem) for elem in encrypted_msg])
encrypted_msg = encrypted_msg.replace(" ", "");
print("");
print("Encrypted msg: ", encrypted_msg);
