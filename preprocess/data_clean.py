import pandas as pd
import re
import emojis
from urlextract import URLExtract


def preprocess(text):  # sourcery skip: assign-if-exp
    extractor = URLExtract()
    for url in extractor.gen_urls(text):
        text = text.replace(url,'<URL>')
    emj = emojis.get(text)
    for i in emj:
        if i in text:
            text = text.replace(i,'<emoji>')
    text = convert_fa_numbers(text)
    text = convert_ar_characters(text)
    # regex to detect and replace all smileys in the text with <smiley>
    text = re.sub(r"(:\s?\)|:-\)|\(\s?:|\(-:|:\'\)|:\s?D|8-\)|:\s?\||;\s?\)|:-\*|:-\||:-\(|:\s?P|:-P|:-p|:-b|:-O|:-o|:-0|:-\@|:\$|:-\^|:-&|:-\*|:-\+|:-\~|:-\`|:-\>|:-\<|:-\}|:-\{|\[:\s?\]|\[:\s?\]|:\s?\]|:\s?\[|:\s?\}|:\s?\{)",'<smiley>',text)
    text = text.lower() # we lowercase here to prevent changes in the URLs and smileys
    text = text.strip()
    text = re.sub(r'[<>#.:()"\'!?؟،,@$%^&*_+\[\]/]', ' ', text)
    text = re.sub(r'[\s]{2,}', ' ', text)
    text = re.sub(r'(\w)\1{2,}', r'\1',text)
    if re.search(r'[\u0600-\u06FF]', text):
        return(text)
    else:
        return 'None'


def convert_ar_characters(input_str):
    """
    Converts Arabic chars to related Persian unicode char
    :param input_str: String contains Arabic chars
    :return: New str with converted arabic chars
    """
    mapping = {
        'ك': 'ک',
        'ى': 'ی',
        'ي': 'ی',
        'ئ':'ی',
        'إ':'ا',
        'أ':'ا',
        'ة':'ه',
        'ؤ':'و'
    }
    return _multiple_replace(mapping, input_str)


def _multiple_replace(mapping, text):
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

def convert_fa_numbers(input_str):
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)
