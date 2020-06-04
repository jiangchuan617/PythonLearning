import message_package
message_package.send_message.seed('hello')
txt = message_package.receive_message.receive()
print(txt)