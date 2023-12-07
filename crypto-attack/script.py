#!/usr/bin/env python3

import base64
import json
import gmpy2


def str_to_number(text):
    """ Encodes a text to a long number representation (big endian). """
    return int.from_bytes(text.encode("ASCII"), 'big')

def number_to_str(num):
    """ Decodes a text to a long number representation (big endian). """
    num = int(num)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('ASCII')

def encrypt(pub_k, msg_num):
    """ We only managed to steal this function... """
    cipher_num = gmpy2.powmod(msg_num, pub_k["e"], pub_k["n"])
    # note: gmpy's to_binary uses a custom format (little endian + special GMPY header)!
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64

def decrypt(priv_k, cipher):
    """ We don't have the privary key, anyway 🙁 """
    # you'll never get it!
    pass

def decrypt_on_server(priv_k, cipher):
    cipher = gmpy2.from_binary(cipher)
    dec_msg = gmpy2.powmod(cipher, priv_k["d"], priv_k["n"])
    return dec_msg

if __name__ == "__main__":
    # example public key
    pub_k = {"e": 17, "n": 1221540932698357538969048008476734604937734436157953593060163}
    # generate a message
    message = "Test Message 1234"
    # note: encrypt requires a number
    msg_num = str_to_number(message)
    # test the reverse
    print("Message:", number_to_str(msg_num))
    # encrypt the message
    cipher = encrypt(pub_k, msg_num)
    print("Ciphertext:", cipher)
    # encode the message to the server's format
    # todo...


    cipher2 = "eyJuIjogMTQ2MTE0NDY5NzE3OTk4NDAzMzQ5NzY1MTM3ODU1NDAwMTk1NDczNTgxNzQ3NjYxMjg2MjAyNjI3MTU3NDI0ODA3MzM2MTQwOTcyOTcyMDY3NzAyNjUyMTg4MTQ1NTg2MTI5MDI4NDQ4OTI2OTE4MTI5MDEwMTQ5NTYyMjI3NDkwOTY5NjQ4OTk4MDY1MDAzNDk1Mjk3MDAxMDcwMTczNzA5MzkwNDg4OTc4NjMxODYxMjczNjcwMDU4MjM3NjI0NTM4MDE4NTY2MjM3MjcxNDcyMDg0NjE0MDM3Mzk3ODQyNDE3MDY2MTQ3NzA4MzY2NTU5MjQxNzgyMTM4NTI5MTgwNzI2MTM4OTc3MzYwNDAwOTY4MTMxMDAxNjAzODc2ODQ5OTY0ODE4NjkyNjM2OTczNzU4OTk0MTUwMTM4MTM2OTQ4NDExNzk1ODY3ODkxODc4MzM4MDAxMzEyMDI5MTk0MDAyMzU0NDA5MDQwMDEyMDgzNTUzMTMyNjk3NDEwMTc0ODk1MTY0MDQ3OTIxOTM5NzQzOTYyNDQyMzcxNDUzOTg4MjY4NjY4ODQzNTcxNDIzOTI1NDM5OTA1MDIwNTc5MzM5ODgzMDgwMzI3NDY2OTIzNTY4ODQzOTc3NjMxNDU2MTI0MTgyODY1MDI2Njk1OTA2NzQwNDU5NjA3Nzc3NzE4MTM5NDA3NzEyMzE1MzI4NDIwMjk5MzUxODQxMjg3Nzk4NDcwNzE4NzA3NTI5MjM3NDAyODcwMzk1MjQwNDQ5MjA5MDUyMzQ4MDE2Nzc5MTgxNzU2NTg5MDk1MDU2NzQ0NjExMzksICJlIjogMTIyNTczLCAiZmxhZyI6ICJBUUY4bjlXOHE5ZTRRSWtwdzVQYm9reEt3RlZ2Ulc1bDZvUFhEWFlWa1U3TTg4UVcrT3ltTEFoeE9VV2xYcnNZVGZ1K1MxN2pyN2VpaXdTYjZtRVZpS25OcGI2L1ZyR2lvbnUveTBWTGhPRkFodjdiaGJtZ0wxWVpuTmh3S1hmdFJtMWI1M3FVQU5pOEo2ckZrbFZJdXRmSnY1TWRXUk5mNDlXK2lTT242ZnI0UTZDbEw0SGVWQVBwVE8rWEt0cUVPYkJxeGIwT20zMVJrVHZNRU9MS2JWNW16b2Rxa09INFVBQzRkS3ZYYjZGWW1lWHNXVjRtNDZPMzRMNC9la1grWGsxVjA4a2p5RmRhY1pkS2M0dFlkNGdJZ3BNTlZWOHVtbkNML2hvbWJDa1dCY1NCNnVwVnl6cEpiRXQrd3dzazR5d2RGU0tUL243eXNBUXlBSVFIa2x0aiJ9"
    cipher3 = b'AQG4poGcJFY8SS75NmEJEcqqXTPNSP2XK0eC'

    cipher2 = base64.b64decode(cipher2)
    cipher3 = base64.b64decode(cipher3)

    print("cipher2:", cipher2)

    data_dict = json.loads(cipher2)

    # Extract values
    n_value = data_dict["n"]
    e_value = data_dict["e"]
    flag_value = data_dict["flag"]

    print("n:", n_value)
    print("e:", e_value)
    print("flag:", flag_value)

    new_data = {'n': n_value, 'e': e_value, 'flag': flag_value}
    print("new_data:", new_data)
    new_data = json.dumps(new_data)
    new_data = base64.b64encode(new_data.encode("ASCII"))

    print("data:", new_data)
    print("SAME:", data_dict)

    
    #flag_value = base64.b64encode(str_to_number(flag_value).to_bytes((str_to_number(flag_value).bit_length() + 7) // 8, byteorder='big'))

    #print("flag:", flag_value)

    # cipher2 = base64.b64encode(cipher2)
    # print("Ciphertext2:", cipher2)

    p = 1043712484569908249601271985137
    q = 1170380685061680196764234806899

    phi = (p-1)*(q-1)
    d = gmpy2.invert(pub_k["e"], phi)

    #priv_k = {"d": d, "n": 1221540932698357538969048008476734604937734436157953593060163}
    #decrypted_msg_num = decrypt_on_server(priv_k, cipher)
    #decrypted_message = number_to_str(decrypted_msg_num)
    #print("Decrypted Message:", decrypted_message)