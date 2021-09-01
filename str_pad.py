''''
this function extends the length of string to match the length of another string 
if length of string matches the length of the other one return unmodified string
although there already is a python builtin function that does this: str.center(width)
this function allows you to customize the ouptut string
created by mendelsshop@gmail.com
'''
def center_string(cardname, space_length):
    card_length = len(cardname)
    if  card_length == space_length:
        return cardname
    else:
        sum_len_blank = space_length - card_length
        left_pad = sum_len_blank % 2
        if left_pad != 0:
            left_pad = (sum_len_blank // 2) + 1
        else:
            left_pad = sum_len_blank / 2
        right_pad = sum_len_blank // 2
    blank = '' 
    return f'{blank: <{right_pad}}{cardname}{blank: >{left_pad}}'

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
