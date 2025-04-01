input_name = input("Please enter your name: ")
input_message = input("Would you like a happy or mid message?: ")

def happymessage(name):
    print("You're doing great ", name, "! Do what makes you happy.", sep="")

def midmessage(name):
    print("You are doing satisfactory ", name, ". Do what is required of you.", sep="")

# happymessage("Jesus")
# happymessage("Dr. Wolfe")
# midmessage("John Doe")

if input_message.lower() == "happy":
    happymessage(input_name)
elif input_message.lower() == "mid":
    midmessage(input_name)
else:
    print("I do not understand...")
