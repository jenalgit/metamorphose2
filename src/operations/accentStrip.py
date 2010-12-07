# -*- coding: utf-8 -*-
#
# Copyright (c) 2007, Ianaré Sévi <ianare@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

"""
Strip accents and splits linked letters from the full set of Unicode
Latin characters for ASCII compatability.

Usage:
import accentStrip
noAccents = accentStrip.auto_convert(u'some string with accents') automatically choose best method
noAccents = accentStrip.full_convert(u'some string with accents') full conversion, slow for large strings
noAccents = accentStrip.fast_convert(u'some string with accents') no squashing but much faster for large strings

Input is Unicode, the output is Unicode which will map directly to ASCII.
Up to you to convert to/from your encoding.
"""

from __future__ import print_function


# dictionary used to convert characters
lookup = {
    # uppercase
    u'À' : u'A',
    u'�?' : u'A',
    u'Â' : u'A',
    u'Ã' : u'A',
    u'Ä' : u'A',
    u'Å' : u'A',
    u'Ā' : u'A',
    u'Ă' : u'A',
    u'Ą' : u'A',
    u'Ḁ' : u'A',
    u'Ạ' : u'A',
    u'Ả' : u'A',
    u'Ấ' : u'A',
    u'Ầ' : u'A',
    u'Ẫ' : u'A',
    u'Ậ' : u'A',
    u'Ắ' : u'A',
    u'Ằ' : u'A',
    u'Ẳ' : u'A',
    u'Ẵ' : u'A',
    u'Ặ' : u'A',
    u'Ḃ' : u'B',
    u'Ḅ' : u'B',
    u'Ḇ' : u'B',
    u'Ƀ' : u'B',
    u'Ç' : u'C',
    u'Ć' : u'C',
    u'Ĉ' : u'C',
    u'Ċ' : u'C',
    u'Č' : u'C',
    u'Ḉ' : u'C',
    u'Ď' : u'D',
    u'�?' : u'D',
    u'Ḋ' : u'D',
    u'Ḍ' : u'D',
    u'Ḏ' : u'D',
    u'�?' : u'D',
    u'Ḓ' : u'D',
    u'È' : u'E',
    u'É' : u'E',
    u'Ê' : u'E',
    u'Ë' : u'E',
    u'Ē' : u'E',
    u'Ĕ' : u'E',
    u'Ė' : u'E',
    u'Ę' : u'E',
    u'Ě' : u'E',
    u'Ḕ' : u'E',
    u'Ḗ' : u'E',
    u'Ḙ' : u'E',
    u'Ḛ' : u'E',
    u'Ḝ' : u'E',
    u'Ẹ' : u'E',
    u'Ẻ' : u'E',
    u'Ẽ' : u'E',
    u'Ế' : u'E',
    u'Ề' : u'E',
    u'Ể' : u'E',
    u'Ễ' : u'E',
    u'Ệ' : u'E',
    u'Ɇ' : u'E',
    u'Ḟ' : u'F',
    u'Ĝ' : u'G',
    u'Ğ' : u'G',
    u'Ġ' : u'G',
    u'Ģ' : u'G',
    u'Ḡ' : u'G',
    u'Ĥ' : u'H',
    u'Ħ' : u'H',
    u'Ḣ' : u'H',
    u'Ḥ' : u'H',
    u'Ḧ' : u'H',
    u'Ḩ' : u'H',
    u'Ḫ' : u'H',
    u'Ⱨ' : u'H',
    u'Ì' : u'I',
    u'�?' : u'I',
    u'Î' : u'I',
    u'�?' : u'I',
    u'Ĩ' : u'I',
    u'Ī' : u'I',
    u'Ĭ' : u'I',
    u'Į' : u'I',
    u'İ' : u'I',
    u'Ḭ' : u'I',
    u'Ḯ' : u'I',
    u'Ỉ' : u'I',
    u'Ị' : u'I',
    u'Ĵ' : u'J',
    u'Ɉ' : u'J',
    u'Ķ' : u'K',
    u'Ḱ' : u'K',
    u'Ḳ' : u'K',
    u'Ḵ' : u'K',
    u'Ⱪ' : u'K',
    u'Ĺ' : u'L',
    u'Ļ' : u'L',
    u'Ľ' : u'L',
    u'Ŀ' : u'L',
    u'�?' : u'L',
    u'Ḷ' : u'L',
    u'Ḹ' : u'L',
    u'Ḻ' : u'L',
    u'Ḽ' : u'L',
    u'Ⱡ' : u'L',
    u'Ɫ' : u'L',
    u'Ḿ' : u'M',
    u'Ṁ' : u'M',
    u'Ṃ' : u'M',
    u'Ñ' : u'N',
    u'Ń' : u'N',
    u'Ņ' : u'N',
    u'Ň' : u'N',
    u'Ŋ' : u'N',
    u'Ṅ' : u'N',
    u'Ṇ' : u'N',
    u'Ṉ' : u'N',
    u'Ṋ' : u'N',
    u'Ò' : u'O',
    u'Ó' : u'O',
    u'Ô' : u'O',
    u'Õ' : u'O',
    u'Ö' : u'O',
    u'Ø' : u'O',
    u'Ō' : u'O',
    u'Ŏ' : u'O',
    u'�?' : u'O',
    u'Ṍ' : u'O',
    u'Ṏ' : u'O',
    u'�?' : u'O',
    u'Ṓ' : u'O',
    u'Ọ' : u'O',
    u'Ỏ' : u'O',
    u'�?' : u'O',
    u'Ồ' : u'O',
    u'Ổ' : u'O',
    u'Ỗ' : u'O',
    u'Ộ' : u'O',
    u'Ớ' : u'O',
    u'Ờ' : u'O',
    u'Ở' : u'O',
    u'Ỡ' : u'O',
    u'Ợ' : u'O',
    u'Ṕ' : u'P',
    u'Ṗ' : u'P',
    u'Ɋ' : u'Q',
    u'Ŕ' : u'R',
    u'Ŗ' : u'R',
    u'Ř' : u'R',
    u'Ṙ' : u'R',
    u'Ṛ' : u'R',
    u'Ṝ' : u'R',
    u'Ṟ' : u'R',
    u'Ɽ' : u'R',
    u'Ɍ' : u'R',
    u'Ś' : u'S',
    u'Ŝ' : u'S',
    u'Ş' : u'S',
    u'Š' : u'S',
    u'Ṡ' : u'S',
    u'Ṣ' : u'S',
    u'Ṥ' : u'S',
    u'Ṧ' : u'S',
    u'Ṩ' : u'S',
    u'Ţ' : u'T',
    u'Ť' : u'T',
    u'Ŧ' : u'T',
    u'Ṫ' : u'T',
    u'Ṭ' : u'T',
    u'Ṯ' : u'T',
    u'Ṱ' : u'T',
    u'Ù' : u'U',
    u'Ú' : u'U',
    u'Û' : u'U',
    u'Ü' : u'U',
    u'Ũ' : u'U',
    u'Ū' : u'U',
    u'Ŭ' : u'U',
    u'Ů' : u'U',
    u'Ű' : u'U',
    u'Ų' : u'U',
    u'Ṳ' : u'U',
    u'Ṵ' : u'U',
    u'Ṷ' : u'U',
    u'Ṹ' : u'U',
    u'Ṻ' : u'U',
    u'Ụ' : u'U',
    u'Ủ' : u'U',
    u'Ứ' : u'U',
    u'Ừ' : u'U',
    u'Ử' : u'U',
    u'Ữ' : u'U',
    u'Ự' : u'U',
    u'Ʉ' : u'U',
    u'Ṽ' : u'V',
    u'Ṿ' : u'V',
    u'Ŵ' : u'W',
    u'Ẁ' : u'W',
    u'Ẃ' : u'W',
    u'Ẅ' : u'W',
    u'Ẇ' : u'W',
    u'Ẉ' : u'W',
    u'Ẋ' : u'X',
    u'Ẍ' : u'X',
    u'�?' : u'Y',
    u'Ŷ' : u'Y',
    u'Ÿ' : u'Y',
    u'Ẏ' : u'Y',
    u'Ỳ' : u'Y',
    u'Ỵ' : u'Y',
    u'Ỷ' : u'Y',
    u'Ỹ' : u'Y',
    u'Ɏ' : u'Y',
    u'Ź' : u'Z',
    u'Ż' : u'Z',
    u'Ž' : u'Z',
    u'�?' : u'Z',
    u'Ẓ' : u'Z',
    u'Ẕ' : u'Z',
    u'Ⱬ' : u'Z',

    # lowercase
    u'à' : u'a',
    u'á' : u'a',
    u'â' : u'a',
    u'ã' : u'a',
    u'ä' : u'a',
    u'å' : u'a',
    u'�?' : u'a',
    u'ă' : u'a',
    u'ą' : u'a',
    u'�?' : u'a',
    u'ạ' : u'a',
    u'ả' : u'a',
    u'ấ' : u'a',
    u'ầ' : u'a',
    u'ẫ' : u'a',
    u'ậ' : u'a',
    u'ắ' : u'a',
    u'ằ' : u'a',
    u'ẳ' : u'a',
    u'ẵ' : u'a',
    u'ặ' : u'a',
    u'ḃ' : u'b',
    u'ḅ' : u'b',
    u'ḇ' : u'b',
    u'ƀ' : u'b',
    u'ç' : u'c',
    u'ć' : u'c',
    u'ĉ' : u'c',
    u'ċ' : u'c',
    u'�?' : u'c',
    u'ḉ' : u'c',
    u'�?' : u'd',
    u'ð' : u'd',
    u'ḋ' : u'd',
    u'�?' : u'd',
    u'�?' : u'd',
    u'ḑ' : u'd',
    u'ḓ' : u'd',
    u'è' : u'e',
    u'é' : u'e',
    u'ê' : u'e',
    u'ë' : u'e',
    u'ē' : u'e',
    u'ĕ' : u'e',
    u'ė' : u'e',
    u'ę' : u'e',
    u'ě' : u'e',
    u'ḕ' : u'e',
    u'ḗ' : u'e',
    u'ḙ' : u'e',
    u'ḛ' : u'e',
    u'�?' : u'e',
    u'ẹ' : u'e',
    u'ẻ' : u'e',
    u'ẽ' : u'e',
    u'ế' : u'e',
    u'�?' : u'e',
    u'ể' : u'e',
    u'ễ' : u'e',
    u'ệ' : u'e',
    u'ɇ' : u'e',
    u'ḟ' : u'f',
    u'�?' : u'g',
    u'ğ' : u'g',
    u'ġ' : u'g',
    u'ģ' : u'g',
    u'ḡ' : u'g',
    u'ĥ' : u'h',
    u'ħ' : u'h',
    u'ḣ' : u'h',
    u'ḥ' : u'h',
    u'ḧ' : u'h',
    u'ḩ' : u'h',
    u'ḫ' : u'h',
    u'ⱨ' : u'h',
    u'ì' : u'i',
    u'í' : u'i',
    u'î' : u'i',
    u'ï' : u'i',
    u'ĩ' : u'i',
    u'ī' : u'i',
    u'ĭ' : u'i',
    u'į' : u'i',
    u'i' : u'i',
    u'ḭ' : u'i',
    u'ḯ' : u'i',
    u'ỉ' : u'i',
    u'ĵ' : u'j',
    u'ɉ' : u'j',
    u'ķ' : u'k',
    u'ḱ' : u'k',
    u'ḳ' : u'k',
    u'ḵ' : u'k',
    u'ⱪ' : u'k',
    u'ĺ' : u'l',
    u'ļ' : u'l',
    u'ľ' : u'l',
    u'ŀ' : u'l',
    u'ł' : u'l',
    u'ḷ' : u'l',
    u'ḹ' : u'l',
    u'ḻ' : u'l',
    u'ḽ' : u'l',
    u'ⱡ' : u'l',
    u'ɫ' : u'l',
    u'ḿ' : u'm',
    u'�?' : u'm',
    u'ṃ' : u'm',
    u'ñ' : u'n',
    u'ń' : u'n',
    u'ņ' : u'n',
    u'ň' : u'n',
    u'ŋ' : u'n',
    u'ṅ' : u'n',
    u'ṇ' : u'n',
    u'ṉ' : u'n',
    u'ṋ' : u'n',
    u'ò' : u'o',
    u'ó' : u'o',
    u'ô' : u'o',
    u'õ' : u'o',
    u'ö' : u'o',
    u'ø' : u'o',
    u'�?' : u'o',
    u'�?' : u'o',
    u'ő' : u'o',
    u'�?' : u'o',
    u'�?' : u'o',
    u'ṑ' : u'o',
    u'ṓ' : u'o',
    u'�?' : u'o',
    u'�?' : u'o',
    u'ố' : u'o',
    u'ồ' : u'o',
    u'ổ' : u'o',
    u'ỗ' : u'o',
    u'ộ' : u'o',
    u'ớ' : u'o',
    u'�?' : u'o',
    u'ở' : u'o',
    u'ỡ' : u'o',
    u'ợ' : u'o',
    u'ṕ' : u'p',
    u'ṗ' : u'p',
    u'ɋ' : u'q',
    u'ŕ' : u'r',
    u'ŗ' : u'r',
    u'ř' : u'r',
    u'ṙ' : u'r',
    u'ṛ' : u'r',
    u'�?' : u'r',
    u'ṟ' : u'r',
    u'ɽ' : u'r',
    u'�?' : u'r',
    u'ś' : u's',
    u'�?' : u's',
    u'ş' : u's',
    u'š' : u's',
    u'ṡ' : u's',
    u'ṣ' : u's',
    u'ṥ' : u's',
    u'ṧ' : u's',
    u'ṩ' : u's',
    u'ţ' : u't',
    u'ť' : u't',
    u'ŧ' : u't',
    u'ṫ' : u't',
    u'ṭ' : u't',
    u'ṯ' : u't',
    u'ṱ' : u't',
    u'ù' : u'u',
    u'ú' : u'u',
    u'û' : u'u',
    u'ü' : u'u',
    u'ũ' : u'u',
    u'ū' : u'u',
    u'ŭ' : u'u',
    u'ů' : u'u',
    u'ű' : u'u',
    u'ų' : u'u',
    u'ṳ' : u'u',
    u'ṵ' : u'u',
    u'ṷ' : u'u',
    u'ṹ' : u'u',
    u'ṻ' : u'u',
    u'ụ' : u'u',
    u'ủ' : u'u',
    u'ứ' : u'u',
    u'ừ' : u'u',
    u'ử' : u'u',
    u'ữ' : u'u',
    u'ự' : u'u',
    u'ʉ' : u'u',
    u'ṽ' : u'v',
    u'ṿ' : u'v',
    u'ⱴ' : u'v',
    u'ŵ' : u'w',
    u'�?' : u'w',
    u'ẃ' : u'w',
    u'ẅ' : u'w',
    u'ẇ' : u'w',
    u'ẉ' : u'w',
    u'ẋ' : u'x',
    u'�?' : u'x',
    u'ý' : u'y',
    u'ŷ' : u'y',
    u'ÿ' : u'y',
    u'�?' : u'y',
    u'ỳ' : u'y',
    u'ỵ' : u'y',
    u'ỷ' : u'y',
    u'ỹ' : u'y',
    u'�?' : u'y',
    u'ź' : u'z',
    u'ż' : u'z',
    u'ž' : u'z',
    u'ẑ' : u'z',
    u'ẓ' : u'z',
    u'ẕ' : u'z',
    u'ⱬ' : u'z',

    # ligatures
    u'Æ' : u'AE',
    u'Ǣ' : u'AE',
    u'Ǽ' : u'AE',
    u'Œ' : u'OE',
    u'Ǆ' : u'DZ',
    u'Ǉ' : u'LJ',
    u'Ǌ' : u'NJ',
    u'Ŋ' : u'Ng',
    u'Ǳ' : u'DZ',

    u'æ' : u'ae',
    u'ǣ' : u'ae',
    u'ǽ' : u'ae',
    u'œ' : u'oe',
    u'ǆ' : u'dz',
    u'ǉ' : u'lj',
    u'ǌ' : u'nj',
    u'ŋ' : u'ng',
    u'ǳ' : u'dz',
    u'ﬀ' : u'ff',
    u'�?' : u'fi',
    u'ﬂ' : u'fl',
    u'ﬃ' : u'ffi',
    u'ﬄ' : u'ffl',
    u'ﬆ' : u'st',
    u'ß' : u'ss',

    # punctuation
    u'¿' : u'?',
    u'¡' : u'!',

    # miscellaneous
    u'µ' : u'u',
    u'«' : u'<',
    u'»' : u'>',
    u'©' : u'(c)',
    u'®' : u'(R)',
    #u'×' : u'x',
    u'×' : u'*',
    u'÷' : u'/',
    u'¢' : u'c',
    u'£' : u'L',
    u'¥' : u'Y',
    u'€' : u'E',
}


# The full ASCII set
allow = u" :!\"#$%&'()*+,-./0123456789;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def test(showOriginal=True):
    """Run a simple test."""
    test = u"¡ŦĦË Ɋṻî�?ḵ Ƀ�?�?�?ñ Ḟø�? Ɉṻḿṗş Ṏṽ�?ŗ Ŧĥệ Ⱡåẕÿ Ğṑð! ¿Cette œuvre là? Große. �?"
    if showOriginal:
        print(test)
    print( full_convert(test) )


def auto_convert(s, rplc=u"_"):
    """Choose the fastest option automatically."""
    if len(s) < len(lookup):
        return full_convert(s, rplc)
    else:
        return fast_convert(s)

def full_convert(s, rplc=u"_"):
    """
    Complete conversion including unknown character squashing.

    Best results but longest execution time. Good for small strings, or when
    unsquashed characters pose a problem.
    """
    rs = u""
    for i in s:
        # already ASCII
        if i in allow:
            rs += i
        # char in lookup table, strip accent
        elif lookup.has_key(i):
            rs += lookup[i]
        # unknown char, squash
        else:
            rs += rplc
    return rs

def fast_convert(s):
    """
    Convert accents but does not squash unknown characters.

    Good for large strings such as files if unsquashed characters do not
    pose problems.
    """
    for i in lookup.keys():
        # change characters from lookuplist
        s=s.replace(i,lookup[i])
    return s
