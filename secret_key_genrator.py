import secrets
def secret_key_generator(length):
  secret_key = secrets.token_hex(length)
  return secret_key
if __name__ == "__main__":
  length = input("enter the length of the key you want to generate: ")
  print(secret_key_generator(length))
