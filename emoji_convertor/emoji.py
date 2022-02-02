

def emoji_convertor(input):

    user_input = input.split(" ")


    output = " "
    emoji = {

        ":)":'☺️',
        ":(":'😞'

    }


    for list in user_input:
        output += emoji.get(list,list) + " "

    return output