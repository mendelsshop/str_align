'''
created by mendelsshop@gmail.com
'''
def center_string(string_name, space_length):
    ''''
    this function extends the length of string to match the length of another string 
    if length of string matches the length of the other one return unmodified string
    although there already is a python builtin function that does this: str.center(width)
    this function allows you to customize the ouptut string
    '''
    card_length = len(string_name)
    if  card_length == space_length:
        return string_name
    else:
        sum_len_blank = space_length - card_length
        left_pad = sum_len_blank % 2
        if left_pad != 0:
            left_pad = (sum_len_blank // 2) + 1
        else:
            left_pad = sum_len_blank / 2
        right_pad = sum_len_blank // 2
    blank = '' 
    return f'{blank: <{right_pad}}{string_name}{blank: >{left_pad}}'


def center_char_string(string_name, space_length,char = None,*,left_char = None,right_char = None):
    card_length = len(string_name)
    if  card_length == space_length:
        return string_name
    else:
        sum_len_blank = space_length - card_length
        left_pad = sum_len_blank % 2
        if left_pad != 0:
            left_pad = (sum_len_blank // 2) + 1
        else:
            left_pad = sum_len_blank / 2
        right_pad = sum_len_blank // 2
    blank = ''
    if char != None or left_char != None or right_char != None:
        if len(char) > 1: return 'char larger than 1'
        if len(char) == 0: return 'char less than than 1'
        if len(left_char) > 1: return 'char larger than 1'
        if len(left_char) == 0: return 'char less than than 1'
        if len(right_char) > 1: return 'char larger than 1'
        if len(right_char)== 0: return 'char less than than 1'
    if right_char != None and left_char != None:
        return f'{left_char}{blank:<{right_pad-1}}{string_name}{blank:>{left_pad-1}}{right_char}'
    elif right_char == None and left_char == None and char != None:
        return f'{char}{blank:<{right_pad-1}}{string_name}{blank:>{left_pad-1}}{char}'  
    elif right_char == None and left_char != None and char == None:
        return f'{left_char}{blank:<{right_pad}}{string_name}{blank:>{left_pad-1}}'     
    elif right_char != None and left_char == None and char == None:
        return f'{left_char}{blank:<{right_pad-1}}{string_name}{blank:>{left_pad}}' 
    else:
        return 'no char found'
def center_string_string(string_name, space_length,string = None,*,left_string = None,right_string = None):
    card_length = len(string_name)
    if  card_length == space_length:
        return string_name
    else:
        sum_len_blank = space_length - card_length
        left_pad = sum_len_blank % 2
        if left_pad != 0:
            left_pad = (sum_len_blank // 2) + 1
        else:
            left_pad = sum_len_blank / 2
        right_pad = sum_len_blank // 2
    blank = ''
    if left_string != None:
        if len(left_string) == 0: return 'a string entered for padding is equal to 0'
        if len(left_string) > left_pad: return 'a string entered for padding is larger than the space between the beginning or end of the main string'
    if right_string != None:
        if len(right_string) == 0: return 'a string entered for padding is equal to 0'
        if len(right_string) > right_pad: return 'a string entered for padding is larger than the space between the beginning or end of the main string'
    if string != None:
        if len(string) == 0: return 'a string entered for padding is equal to 0'
        if len(string) > left_pad: return 'a string entered for padding is larger than the space between the beginning or end of the main string'
        if len(string) > right_pad: return 'a string entered for padding is larger than the space between the beginning or end of the main string'
    if right_string != None and left_string != None:
        return f'{left_string}{blank:<{right_pad-1}}{string_name}{blank:>{left_pad-1}}{right_string}'
    elif right_string == None and left_string == None and string != None:
        return f'{string}{blank:<{right_pad-1}}{string_name}{blank:>{left_pad-1}}{string}'  
    elif right_string == None and left_string != None and string == None:
        return f'{left_string}{blank:<{right_pad}}{string_name}{blank:>{left_pad-1}}'     
    elif right_string != None and left_string == None and string == None:
        return f'{left_string}{blank:<{right_pad-1}}{string_name}{blank:>{left_pad}}' 
if __name__ == '__main__':
    extend_length = 20
    word_to_extend = 'Hello, World'
    print(f'Length to extend string to: {extend_length}')
    print(f'String to extend: {word_to_extend}')
    print(f'Usage: print(center_string({word_to_extend}, {extend_length}))')
    print(f'|{center_string(word_to_extend, extend_length)}|')
    print('Or using a variable')
    print(f'centered_string = (center_string({word_to_extend}, {extend_length}))')
    print('print(centered_string)')
    print(f'|{center_string(word_to_extend, extend_length)}|')
    print('note: vertical bar just used to demostrate functality') 
    z = center_string_string('hi', 11,'h')
    print(z)
