# t.me/amirkho_eng
# GitHub: amirkho-py
# پیاده سازی الگوریتم رمزنگاری و رمزگشایی سزار




# Encryption
def caesar_encrypt(plaintext, shift): 
  ciphertext = ""
  for ch in plaintext:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      ciphertext += finalLetter
    else:
      ciphertext += ch
  return ciphertext
  


# Decryption
def caesar_decrypt(ciphertext, shift):
  plaintext = ""
  for ch in ciphertext:
    if ch.isalpha():
      stayInAlphabet = ord(ch) - shift
      if stayInAlphabet < ord('a'):
        stayInAlphabet += 26
      finalLetter = chr(stayInAlphabet)
      plaintext += finalLetter
    else:
      plaintext += ch
  return plaintext




