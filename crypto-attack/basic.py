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
    print("cipher_num:", cipher_num)

    # note: gmpy's to_binary uses a custom format (little endian + special GMPY header)!
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64

def decrypt(priv_k, cipher):
    """ We don't have the privary key, anyway :( """
    # you'll never get it!
    pass

def create_json(flag):
    
    data = {"flag" : "AQFgrkVrmP5nIIt4RKXCBMmA01nY6UCyC3qm6pMwTUnEXdT+aTF8vRJUF9KBYiTHvcYL31YHNdHnTvso0rArBnL+2mOTBe+68knmc7uR9ED4sA4AWEKOng0XTVhne5n7SJKI7t4HJVpwQFDMD34XAWczZEFbZWviUR5Ea4fC8FjIbOpqXu6DAiE4gOFHeTbJUJk3WNpDy7jXy0VO9Mc2KOFQYBzvEcgjXcq4q1BYhlNR1Mti37y0y5QREhjvCagePUvm3jS+vzWz5iGQAH3hocX7j6WS3vbBARSoutMnyVLYCBKTRx93hAdJcsS9dFcICc1+YlQMZJPx91rGBl3RRyRCyYacTmkjZDQ/WnfgCGnITnjNjPCK/bCX0JTUwS6vySi3WiLm9FhsY0gez7bFmYmasf7ujo9+SmLau8/h8sXipbshUoUpLHJGsrpTerWdWzHEyAG0BtH8bR4sZ+mkblfk0aCdHVNyHYlPr5nW+NzB7ZNrP5+42MK2DdkzmVqqvCquNLERxCNVNQp4gK717b5/PEuBbhG6kUsMZs7rx2td7b40tiUzX6qiournxg/jvUSJb5/bRf1gBC/4C/hE71aETRHksKv22LsnnTAG684gCEfYv4/VKFk7Pkmua1OWEte9CqJN56TYAcT43L85gwm3wGOkRzFbMpW0K1cS/K/jAg=="}
    print("data:", data)
    data_json = json.dumps(data)
    data = base64.b64encode(data_json.encode("ASCII"))
    print("data:", data)
    return data

def compute_t(Cb, d, n):
    # Calculate the modular inverse of 2
    two_inv = gmpy2.invert(2, n)

    # Calculate t
    t = (gmpy2.powmod(Cb, d, n) * two_inv) 
    return t

if __name__ == "__main__":
    # example public key
    pub_k = {"e": 189713, "n": 12523911496999053285608838317154273691314435769181047026664037010936596965785660270448810262688404708499919448246477716615337413132959242636424387334467469263762476174361171738987538007491744206828565049888852118198968835303806559094678522074422690248383909133047428330479250523445640995430120943914611652415980377491273825704703834486598014456514618613047767715827619949827200057892504490928299097373766963125244797744792433566225025293899715373904306740177238649116591418485220573845233739777029694316573876672732618014222107340655054071033042797190672455915525675457233585758061065063231930335790760370816632554313}
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
    # cipher = base64.b64encode(cipher)
    
    my_message_b64 = "eyJuIjogMTI1MjM5MTE0OTY5OTkwNTMyODU2MDg4MzgzMTcxNTQyNzM2OTEzMTQ0MzU3NjkxODEwNDcwMjY2NjQwMzcwMTA5MzY1OTY5NjU3ODU2NjAyNzA0NDg4MTAyNjI2ODg0MDQ3MDg0OTk5MTk0NDgyNDY0Nzc3MTY2MTUzMzc0MTMxMzI5NTkyNDI2MzY0MjQzODczMzQ0Njc0NjkyNjM3NjI0NzYxNzQzNjExNzE3Mzg5ODc1MzgwMDc0OTE3NDQyMDY4Mjg1NjUwNDk4ODg4NTIxMTgxOTg5Njg4MzUzMDM4MDY1NTkwOTQ2Nzg1MjIwNzQ0MjI2OTAyNDgzODM5MDkxMzMwNDc0MjgzMzA0NzkyNTA1MjM0NDU2NDA5OTU0MzAxMjA5NDM5MTQ2MTE2NTI0MTU5ODAzNzc0OTEyNzM4MjU3MDQ3MDM4MzQ0ODY1OTgwMTQ0NTY1MTQ2MTg2MTMwNDc3Njc3MTU4Mjc2MTk5NDk4MjcyMDAwNTc4OTI1MDQ0OTA5MjgyOTkwOTczNzM3NjY5NjMxMjUyNDQ3OTc3NDQ3OTI0MzM1NjYyMjUwMjUyOTM4OTk3MTUzNzM5MDQzMDY3NDAxNzcyMzg2NDkxMTY1OTE0MTg0ODUyMjA1NzM4NDUyMzM3Mzk3NzcwMjk2OTQzMTY1NzM4NzY2NzI3MzI2MTgwMTQyMjIxMDczNDA2NTUwNTQwNzEwMzMwNDI3OTcxOTA2NzI0NTU5MTU1MjU2NzU0NTcyMzM1ODU3NTgwNjEwNjUwNjMyMzE5MzAzMzU3OTA3NjAzNzA4MTY2MzI1NTQzMTMsICJlIjogMTg5NzEzLCAiZmxhZyI6ICJBUUVCTWcxUzRSNEtjLzZCMVpRUTRTWEJkeUFudHJPRS8yRk15bkN6K3hTLzdpTWd3S2g5bHdBWWE1ZlJVbWN5K2pWdnNpZUZjTGpDa0RNN3ZhSUhPUmhiVENDY1RQd0pKcTQ1UVMzRFYybENOUG1DY0FWNUdHVm9KWEpUci9RN0ZqaUYvSG9rVEdRZFQrZzZDVFJXU05INlRMYmErMmlJS1VQbm8velJkQ1dkL3diWGxNck45SkcvL3lJdkEvdzRuTTE1cXBCcksybDhMeU0rcmZxZ1lZcUVVYmFUR1RoWEJ0d09BSUR6ZEJzbGhxekkrK00weHRhbGxVQ2hqYWRrV3hPVEUyNHptTmdyY2o0bEJIRDBKZUtCTlhWZlBaOUVhcUlLZzlUR09XZmFyWmpKTXU2SzdMdmxvci9YRG1Menh5ajJ4bGNEanR6TUowZkE5QUdIRGhrTSJ9"
    my_message_b64_2 = b'eyJuIjogMTI1MjM5MTE0OTY5OTkwNTMyODU2MDg4MzgzMTcxNTQyNzM2OTEzMTQ0MzU3NjkxODEwNDcwMjY2NjQwMzcwMTA5MzY1OTY5NjU3ODU2NjAyNzA0NDg4MTAyNjI2ODg0MDQ3MDg0OTk5MTk0NDgyNDY0Nzc3MTY2MTUzMzc0MTMxMzI5NTkyNDI2MzY0MjQzODczMzQ0Njc0NjkyNjM3NjI0NzYxNzQzNjExNzE3Mzg5ODc1MzgwMDc0OTE3NDQyMDY4Mjg1NjUwNDk4ODg4NTIxMTgxOTg5Njg4MzUzMDM4MDY1NTkwOTQ2Nzg1MjIwNzQ0MjI2OTAyNDgzODM5MDkxMzMwNDc0MjgzMzA0NzkyNTA1MjM0NDU2NDA5OTU0MzAxMjA5NDM5MTQ2MTE2NTI0MTU5ODAzNzc0OTEyNzM4MjU3MDQ3MDM4MzQ0ODY1OTgwMTQ0NTY1MTQ2MTg2MTMwNDc3Njc3MTU4Mjc2MTk5NDk4MjcyMDAwNTc4OTI1MDQ0OTA5MjgyOTkwOTczNzM3NjY5NjMxMjUyNDQ3OTc3NDQ3OTI0MzM1NjYyMjUwMjUyOTM4OTk3MTUzNzM5MDQzMDY3NDAxNzcyMzg2NDkxMTY1OTE0MTg0ODUyMjA1NzM4NDUyMzM3Mzk3NzcwMjk2OTQzMTY1NzM4NzY2NzI3MzI2MTgwMTQyMjIxMDczNDA2NTUwNTQwNzEwMzMwNDI3OTcxOTA2NzI0NTU5MTU1MjU2NzU0NTcyMzM1ODU3NTgwNjEwNjUwNjMyMzE5MzAzMzU3OTA3NjAzNzA4MTY2MzI1NTQzMTMsICJlIjogMTg5NzEzLCAiZmxhZyI6ICJBUUVCTWcxUzRSNEtjLzZCMVpRUTRTWEJkeUFudHJPRS8yRk15bkN6K3hTLzdpTWd3S2g5bHdBWWE1ZlJVbWN5K2pWdnNpZUZjTGpDa0RNN3ZhSUhPUmhiVENDY1RQd0pKcTQ1UVMzRFYybENOUG1DY0FWNUdHVm9KWEpUci9RN0ZqaUYvSG9rVEdRZFQrZzZDVFJXU05INlRMYmErMmlJS1VQbm8velJkQ1dkL3diWGxNck45SkcvL3lJdkEvdzRuTTE1cXBCcksybDhMeU0rcmZxZ1lZcUVVYmFUR1RoWEJ0d09BSUR6ZEJzbGhxekkrK00weHRhbGxVQ2hqYWRrV3hPVEUyNHptTmdyY2o0bEJIRDBKZUtCTlhWZlBaOUVhcUlLZzlUR09XZmFyWmpKTXU2SzdMdmxvci9YRG1Menh5ajJ4bGNEanR6TUowZkE5QUdIRGhrTSJ9'
    message = base64.b64decode(my_message_b64)
    print("message_1:", message)
    message = base64.b64decode(my_message_b64_2)
    print("message_2:", message)

    my_flag = "AQEBMg1S4R4Kc/6B1ZQQ4SXBdyAntrOE/2FMynCz+xS/7iMgwKh9lwAYa5fRUmcy+jVvsieFcLjCkDM7vaIHORhbTCCcTPwJJq45QS3DV2lCNPmCcAV5GGVoJXJTr/Q7FjiF/HokTGQdT+g6CTRWSNH6TLba+2iIKUPno/zRdCWd/wbXlMrN9JG//yIvA/w4nM15qpBrK2l8LyM+rfqgYYqEUbaTGThXBtwOAIDzdBslhqzI++M0xtallUChjadkWxOTE24zmNgrcj4lBHD0JeKBNXVfPZ9EaqIKg9TGOWfarZjJMu6K7Lvlor/XDmLzxyj2xlcDjtzMJ0fA9AGHDhkM"
    C = gmpy2.from_binary(base64.b64decode(my_flag))
    r = encrypt(pub_k, 2)
    r = gmpy2.from_binary(base64.b64decode(r))
    print("C:", C)
    print("r:", r)
    Cprim = C * r
    print("Cprim:", Cprim)
    Cprim = base64.b64encode(gmpy2.to_binary(Cprim))
    print("Cprim:", Cprim)


    msg_to_send = create_json(cipher)
    print("msg_to_send:", msg_to_send)

    bytes_flag = b'\xa6\xe0\xca\xd2\xe6\xd0\x8c\xd8\xc2\xce\xf6\x82\x9e\xb0\xcc`\x94\xb2\x84\xaa\xae\xe8\xca\xaa\xf0\xf0\xa8\xae\x9er\xce\xd0n\xca\xc4hn\xf0\x84\xa0\x8cr\xa4\xfa'
    bytes_flag = int.from_bytes(bytes_flag, byteorder='big')
    bytes_flag = bytes_flag // 2
    x = number_to_str(bytes_flag)
    print("x:", x)
    
    bytes_flag = bytes_flag.to_bytes((bytes_flag.bit_length() + 7) // 8, byteorder='big')

    print("bytes_flag:", bytes_flag)
