from channels import Group

def ws_add (message): #connect
    message.reply_channel.send({"accept":True})
    Group('chat').add(message.reply_channel)


def ws_message(message) : #receve
    Group('chat').send({'text': message.content['text']})

def ws_desconnect(message) : #disconnect
    Group('chat').discard(message.reply_channel)