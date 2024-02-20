message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

# Strat
# secret = message[message.find("🔑")+1:]
# print(secret)
# output = secret.upper()
# print(output)
# print(code)

# if(output == code):
#   print("You are an hacker 🎊")
# else:
#   print("try again")

# Task 2: 🔑
# No, secret is present
# message2 = "    🚨🔍📱secret_code✌️"
# if (message2.find("🔑") == -1):
#   print("No, secret is present")
# else:
#   secret = message2[message2.find("🔑")+1:]
#   print(secret)
#   output = secret.upper()
#   print(output)
#   print(code)
#   if(output == code):
#     print("You are an hacker 🎊")
#   else:
#     print("try again")

# Task 3: 🔑
message3 = "    🚨🔍📱🔑****secret_code✌️(((("
# if (message3.find("🔑") == -1):
#   print("No, secret is present")
# else:
#   strippedmsg3 = message3.replace("*", "").replace("(", "")
#   print(strippedmsg3)
#   secret = strippedmsg3[strippedmsg3.find("🔑")+1:]
#   print(secret)
#   output = secret.upper()
#   print(output)
#   print(code)
#   if(output == code):
#     print("You are an hacker 🎊")
#   else:
#     print("try again")
if (message3.find("🔑") == -1):
  print("No, secret is present")
else:
  secret = message3[message3.find("🔑") + 1:]
  print(secret)
  # Dot chaining
  strippedsecret = secret.strip("*").strip("(")
  output = strippedsecret.upper()
  print(output)
  print(code)
  if (output == code):
    print("You are an hacker 🎊")
  else:
    print("try again")
