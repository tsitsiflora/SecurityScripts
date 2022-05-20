#this script splits and joins text together
message = """Hello world!
My name is Tsitsi.
I am a Security Engineer.
I like pentesting so much.
And coding as well."""

def split_and_join(message=message):
    '''Split the message by newline, then join with | (pipe),
        return the new output'''
    lines = message.split('\n')
    return '|'.join(lines)

new_message = split_and_join(message)
print(new_message)
