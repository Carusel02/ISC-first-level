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
    """ We don't have the privary key, anyway :( """
    # you'll never get it!
    pass

def compute_Cb(C, e, n):
    # Decode the Base64-encoded C
    # C_binary = base64.b64decode(C_base64)

    # Convert the binary data to an integer
    C = int.from_bytes(C, byteorder='big')

    # Compute 2^e mod n
    two_exp_e = gmpy2.powmod(2, e, n)

    # Compute Cb = C * 2^e mod n
    Cb = gmpy2.mod(C * two_exp_e, n)
    # Cb = (C * two_exp_e) % n

    return Cb

def compute_t(Cb, d, n):
    # Calculate the modular inverse of 2
    two_inv = gmpy2.invert(2, n)

    # Calculate t
    t = (gmpy2.powmod(Cb, d, n) * two_inv) 
    return t

def create_json(flag):

    data = {"flag" : flag}
    data_json = json.dumps(data)
    data = base64.b64encode(data_json.encode("ASCII"))
    return data

if __name__ == "__main__":
    # example public key
    pub_k = {"e": 122573, "n": 14611446971799840334976513785540019547358174766128620262715742480733614097297206770265218814558612902844892691812901014956222749096964899806500349529700107017370939048897863186127367005823762453801856623727147208461403739784241706614770836655924178213852918072613897736040096813100160387684996481869263697375899415013813694841179586789187833800131202919400235440904001208355313269741017489516404792193974396244237145398826866884357142392543990502057933988308032746692356884397763145612418286502669590674045960777771813940771231532842029935184128779847071870752923740287039524044920905234801677918175658909505674461139}
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



    message = "eyJuIjogMTI1MjM5MTE0OTY5OTkwNTMyODU2MDg4MzgzMTcxNTQyNzM2OTEzMTQ0MzU3NjkxODEwNDcwMjY2NjQwMzcwMTA5MzY1OTY5NjU3ODU2NjAyNzA0NDg4MTAyNjI2ODg0MDQ3MDg0OTk5MTk0NDgyNDY0Nzc3MTY2MTUzMzc0MTMxMzI5NTkyNDI2MzY0MjQzODczMzQ0Njc0NjkyNjM3NjI0NzYxNzQzNjExNzE3Mzg5ODc1MzgwMDc0OTE3NDQyMDY4Mjg1NjUwNDk4ODg4NTIxMTgxOTg5Njg4MzUzMDM4MDY1NTkwOTQ2Nzg1MjIwNzQ0MjI2OTAyNDgzODM5MDkxMzMwNDc0MjgzMzA0NzkyNTA1MjM0NDU2NDA5OTU0MzAxMjA5NDM5MTQ2MTE2NTI0MTU5ODAzNzc0OTEyNzM4MjU3MDQ3MDM4MzQ0ODY1OTgwMTQ0NTY1MTQ2MTg2MTMwNDc3Njc3MTU4Mjc2MTk5NDk4MjcyMDAwNTc4OTI1MDQ0OTA5MjgyOTkwOTczNzM3NjY5NjMxMjUyNDQ3OTc3NDQ3OTI0MzM1NjYyMjUwMjUyOTM4OTk3MTUzNzM5MDQzMDY3NDAxNzcyMzg2NDkxMTY1OTE0MTg0ODUyMjA1NzM4NDUyMzM3Mzk3NzcwMjk2OTQzMTY1NzM4NzY2NzI3MzI2MTgwMTQyMjIxMDczNDA2NTUwNTQwNzEwMzMwNDI3OTcxOTA2NzI0NTU5MTU1MjU2NzU0NTcyMzM1ODU3NTgwNjEwNjUwNjMyMzE5MzAzMzU3OTA3NjAzNzA4MTY2MzI1NTQzMTMsICJlIjogMTg5NzEzLCAiZmxhZyI6ICJBUUVCTWcxUzRSNEtjLzZCMVpRUTRTWEJkeUFudHJPRS8yRk15bkN6K3hTLzdpTWd3S2g5bHdBWWE1ZlJVbWN5K2pWdnNpZUZjTGpDa0RNN3ZhSUhPUmhiVENDY1RQd0pKcTQ1UVMzRFYybENOUG1DY0FWNUdHVm9KWEpUci9RN0ZqaUYvSG9rVEdRZFQrZzZDVFJXU05INlRMYmErMmlJS1VQbm8velJkQ1dkL3diWGxNck45SkcvL3lJdkEvdzRuTTE1cXBCcksybDhMeU0rcmZxZ1lZcUVVYmFUR1RoWEJ0d09BSUR6ZEJzbGhxekkrK00weHRhbGxVQ2hqYWRrV3hPVEUyNHptTmdyY2o0bEJIRDBKZUtCTlhWZlBaOUVhcUlLZzlUR09XZmFyWmpKTXU2SzdMdmxvci9YRG1Menh5ajJ4bGNEanR6TUowZkE5QUdIRGhrTSJ9"
    dictionary = json.loads(base64.b64decode(message))
    dictionary["flag"] = "abc"
    print("dictionary : ", dictionary)

    # base 64 encoded cipher
    cipher_flag_64 = b'AQF8n9W8q9e4QIkpw5PbokxKwFVvRW5l6oPXDXYVkU7M88QW+OymLAhxOUWlXrsYTfu+S17jr7eiiwSb6mEViKnNpb6/VrGionu/y0VLhOFAhv7bhbmgL1YZnNhwKXftRm1b53qUANi8J6rFklVIutfJv5MdWRNf49W+iSOn6fr4Q6ClL4HeVAPpTO+XKtqEObBqxb0Om31RkTvMEOLKbV5mzodqkOH4UAC4dKvXb6FYmeXsWV4m46O34L4/ekX+Xk1V08kjyFdacZdKc4tYd4gIgpMNVV8umnCL/hombCkWBcSB6upVyzpJbEt+wwsk4ywdFSKT/n7ysAQyAIQHkltj'
    cipher_flag_num = gmpy2.from_binary(base64.b64decode(cipher_flag_64))
    C = cipher_flag_num
    print("C : ", C)
    # r
    r = gmpy2.powmod(2, pub_k["e"], pub_k["n"])
    # C * r pow e mod n
    Cprim = C * r
    send_cipher = base64.b64encode(gmpy2.to_binary(Cprim))
    print("SEND CIPHER : ", send_cipher)

    json_obj = "AQEEA5ztmVdqcPBR9KqaPPAO79Ipq4Tg/0qrGL2V9gzDoFNy+pwRW2QBliUUz/avg/eVKAdrPiRs30mMRBrElcIPo0Ywuqc7tSVB0fcgd4pvRMQfqPGwgjDWLUyYulhIlCj0AU9fNTCBKZt+b2eGGrcfq5HeqA143/MBhLgoGlhjsvz4ACg8mOkKWvKtStT4P/GG/HZUXDiIYJGByTqg6j+91pp7LjeasF1HNtcT8/dtkl9id7KgfKvUauQodnXqqUavPrWxuSa6aFy6SoTTSARKEK/XqdWIUMUw7kp2R7vk7SBPBfB6zmikWQ0W3w6DluBHSfMDPg9DZ8gLOvlegnPBxx86d31xWCI97oJRyqRDV6OBac25s0Uu36rKoCyHh+0KfiTeXqXhGPhN07kFr2AJmo9c0ZP7w8hW87/SHBjNKDyEW3MkNNyxtcfd7mO7FoiHv5dEIC7J84KXTVMoYuWd/w1+kVkJjfJGR75fMxqOLP51Jnih4nUvoSDEiPP6YA2Vfi2FFiR+FtaXvq6iWcwffJJ2cWMUE2kMGv5g66Pjp8XcDHbwlsZ+Mzc1JidglfRpaopsqeUMhEyAvnxbg6qYm0KYAwZ141AVdejhXG4iW0zRl00U2dDKXkTPMNUFre5D+kbdG4HDxlIUaUVPX1haJuZ52UPhnH6psQ6H5HLPLA=="

    print("SEND : ", create_json(json_obj))
    
    decrypted_flag = b'\x14S\x9f-\xf8\xc5\xf2U\x1a\x14\xbd\xfdc\x10\xc2B\xa7^\x87\x9f\xf2\xad\xc6\xd0,7\x08\x85S\x01!\x0c\x15\xe7\xfe\x1bM\x81\xdf=\xf28\xbfs\xc6\xc0\xc7\x83\x1c\x16\x84\xdd\xa7\x7f\x8c\xef\xf5D\xcc\xadj\xede\xe1HJ\x80s\x90\x7fl7,z\x87\xd6\xfa\xa3>P\xe2a`\x94\x94S/?X\xb7S\x9c\xf0_Y\x8e=\xf0\x11\xc2@\x0c\xb1\x8e=_\xce\xe1\x88\xa7,\xf2\x93a\xeb\xa9\x92\x8e"@\xad\xf4=t\xda\x0c4b\xc8\x0e\x05\xbcM\x15\xa3\x99h\xeeQ\xbf\x1b\xdcc\xe9z\xc2\xfc\x00;\x18R\x86\xf6\x06A\rA1V\xae\xa1db\xd5\x04I\xd4\x9b\xcd\xce\xd28\xaf\x00T\x9f\xdf\x16\x10U\xec\xc1\xa28\xa6\xdb\xc6\xa3\x19]\xd1\'~\x8cz\x93\xeb\xf0\xc3\x19$\xa7k\x1a\xf6\x1b4\xf9]\x1f$\xf8\xf2\xb9\xd0\xabz\x85V\xe6\xd0ak\n\xa4\x19\xd7\xab\xa6u\xb0\x1a\xcf\xe5\x19p\x08\xfc\xa4s_\xa40Hm[\xcb\x17Zjz_*zO#'
    decrypted_flag_num = base64.b64decode((decrypted_flag))
    decrypted_flag_num = int.from_bytes(decrypted_flag_num, byteorder='big')
    res = gmpy2.invert(decrypted_flag_num, pub_k["n"])
    res = res // 2
    res = number_to_str(res)
    print("res : ", res)

    print("decrypted_flag_num : ", decrypted_flag_num)


    msg_num = 2
    eve = encrypt(pub_k, msg_num)
    C = b'AQF8n9W8q9e4QIkpw5PbokxKwFVvRW5l6oPXDXYVkU7M88QW+OymLAhxOUWlXrsYTfu+S17jr7eiiwSb6mEViKnNpb6/VrGionu/y0VLhOFAhv7bhbmgL1YZnNhwKXftRm1b53qUANi8J6rFklVIutfJv5MdWRNf49W+iSOn6fr4Q6ClL4HeVAPpTO+XKtqEObBqxb0Om31RkTvMEOLKbV5mzodqkOH4UAC4dKvXb6FYmeXsWV4m46O34L4/ekX+Xk1V08kjyFdacZdKc4tYd4gIgpMNVV8umnCL/hombCkWBcSB6upVyzpJbEt+wwsk4ywdFSKT/n7ysAQyAIQHkltj'
    print("Eve : ", eve)
    Cb = compute_Cb(C, pub_k["e"], pub_k["n"])
    Cb = base64.b64encode(gmpy2.to_binary(Cb))
    print("Cb : ", Cb)
    Cbd = b'$\x14P7\xf1\xac\x17\x9fj\xfb\x08\xf8\xcc\'\x1c\nyS\\\xa6SV\x14*\x0c:\xfd\xe9\x1c\xf1U\x8f\xe0D\xe0\x95\xbb\x07\xef{\x18\x89\x1e\xa7\x1dx\x07(\xc2\xe8gc\xd5dca\xd7/\x07\x02\x95\x9fJ\x9d\x13!\xfb\xfe\xd5MhMR\xdc\xdd\xa0\x1c\x0ern\xc6\xa3\xdf\xc6\x9b\x133t\xa8^+h\xa3\r\xc5\xed\xb6\xe3\xf0)\xc8\x19\xd0s\x82W\xfbp=\xa73~\xdb<-\x0e\x97\x94\xd8\xfd\xe0\xc1\x96\xdf\xea\x1b\xa4\xca\x93\xcb3\x9e\x9c\x1dj\xfb\x8d?Sq,&"\x81\x97\xf6\x8e\xa17\x08\r{\xc2\xa06\xa2G\xb85\xba"\x98\xa7\x1eU \xb9\x9c]\x87~U+=\\N\xb9E\xe8$\x91\x03%\x8a\xe0\x07\xa0\xfbM\x81 \x14\xe8j\xad`\x87%#\xd0l$0\xd0\x9e\x866\xb6\x13\x8b\x9e\xdc\xfa?BO(\xbb3\xbf\x0e\x993\x00\xcf\x83lKv\xc2\xbf\x82\xee\x7f\xda}\xe6~\'\x82\xc4*(2H\xeeeC\xd8o\xcb\xb7\xbb\xcc\xf5\xc4'
    Cbd = int.from_bytes(Cbd, byteorder='big')
    # t = int.from_bytes(Cbd, byteorder='big')
    # t = t // 2
    # t = number_to_str(t)
    # print("t : ", t)

    result_t = compute_t(Cbd, pub_k["e"], pub_k["n"])
    # print("result_t : ", number_to_str(result_t))
