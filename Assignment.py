# Mini Project: Emoji Converter
# Covert text-based emotions into emojis.
# (without using any loop or if )

msg = input("Enter your message:")

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😢")
msg = msg.replace(":D", "😃")
msg = msg.replace("<3", "❤️")

print(msg)