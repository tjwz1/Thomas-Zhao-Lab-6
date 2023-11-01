#Thomas Zhao
def menu():
  print('Menu')
  print(8*'-')
  print("1. Encode")
  print("2. Decode")
  print("3. Quit")
  print()
  
def encode(password):
  encode_password = ''
  x = 0
  for a in range(len(password)):
    x = int(password[a])+3
    if x>9:
      x = x%10
    encode_password += str(x)
    
def decode(password):
  decoded_password = ''
  x = 0
  for a in range(len(password)):
    x = int(password[a])-3
    if x<0:
      x = x + 10
    decoded_password += str(x)
  return decoded_password
  
if __name__ == "__main__":
    menu()
    run = True
    encoded_password= ''
    orig_password = ''
    while run:
      choice = input("Please enter an option: ")
      if choice =="1":
          password = input("Please enter your password to encode: ")
          encode(password)
          print("Your password has been encoded and stored!")
          print()
      if choice=='2':
          print("The encoded password is",encoded_password, end =' ')
          print("and the original password is",orig_password)
          print()
      if choice=='3':
          run = False
