# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = ('нуль',)

ONES_FEMININE = {
    1: ('одна',),
    2: ('дві',),
    3: ('три',),
    4: ('чотири',),
    5: ('п\'ять',),
    6: ('шість',),
    7: ('сім',),
    8: ('вісім',),
    9: ('дев\'ять',),
}

ONES = {
    1: ('один',),
    2: ('два',),
    3: ('три',),
    4: ('чотири',),
    5: ('п\'ять',),
    6: ('шість',),
    7: ('сім',),
    8: ('вісім',),
    9: ('дев\'ять',),
}

TENS = {
    0: ('десять',),
    1: ('одинадцять',),
    2: ('дванадцять',),
    3: ('тринадцять',),
    4: ('чотирнадцять',),
    5: ('п\'ятнадцять',),
    6: ('шістнадцять',),
    7: ('сімнадцять',),
    8: ('вісімнадцять',),
    9: ('дев\'ятнадцять',),
}

TWENTIES = {
    2: ('двадцять',),
    3: ('тридцять',),
    4: ('сорок',),
    5: ('п\'ятдесят',),
    6: ('шістдесят',),
    7: ('сімдесят',),
    8: ('вісімдесят',),
    9: ('дев\'яносто',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двісті',),
    3: ('триста',),
    4: ('чотириста',),
    5: ('п\'ятсот',),
    6: ('шістсот',),
    7: ('сімсот',),
    8: ('вісімсот',),
    9: ('дев\'ятсот',),
}

THOUSANDS = {
    1: ('тисяча', 'тисячі', 'тисяч'),  # 10^3
    2: ('мільйон', 'мільйони', 'мільйонів'),  # 10^6
    3: ('мільярд', 'мільярди', 'мільярдів'),  # 10^9
    4: ('трильйон', 'трильйони', 'трильйонів'),  # 10^12
    5: ('квадрильйон', 'квадрильйони', 'квадрильйонів'),  # 10^15
    6: ('квінтильйон', 'квінтильйони', 'квінтильйонів'),  # 10^18
    7: ('секстильйон', 'секстильйони', 'секстильйонів'),  # 10^21
    8: ('септильйон', 'септильйони', 'септильйонів'),  # 10^24
    9: ('октильйон', 'октильйони', 'октильйонів'),  # 10^27
    10: ('нонільйон', 'нонільйони', 'нонільйонів'),  # 10^30
}

FEMININE_MONEY = ('AOA', 'BAM', 'BDT', 'BWP', 'CZK', 'DKK',
                  'ERN', 'HNL', 'HRK', 'IDR', 'INR', 'ISK',
                  'JPY', 'KPW', 'KRW', 'LKR', 'MOP', 'MRU',
                  'MUR', 'MVR', 'MWK', 'NGN', 'NIO', 'NOK',
                  'NPR', 'PKR', 'SCR', 'SEK', 'STN', 'TRY',
                  'WST', 'UAH', 'ZMW')
FEMININE_CENTS = ('ALL', 'BDT', 'BGN', 'BYN', 'GHS', 'HRK',
                  'ILS', 'INR', 'NPR', 'OMR', 'OMR', 'PKR',
                  'RSD', 'RUB', 'UAH')

GENERIC_DOLLARS = ('долар', 'долари', 'доларів')
GENERIC_CENTS = ('цент', 'центи', 'центів')


class Num2Word_UK(Num2Word_Base):
    CURRENCY_FORMS = {
        'AED': (('дирхам', 'дирхами', 'дирхамів'), ('філс', 'філси', 'філсів')),
        'AFN': (('афгані', 'афгані', 'афгані'), ('пул', 'пули', 'пулів')),
        'ALL': (('лек', 'леки', 'леків'), ('кіндарка', 'кіндарки', 'кіндарок')),
        'AMD': (('драм', 'драми', 'драмів'), ('лум', 'лум', 'лум')),
        'ANG': (('гульден', 'гульдени', 'гульденів'), GENERIC_CENTS),
        'AOA': (('кванза', 'кванзи', 'кванз'), ('сентимо', 'сентимо', 'сентимо')),
        'ARS': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'AUD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'AWG': (('флорин', 'флорини', 'флоринів'), GENERIC_CENTS),
        'AZN': (('манат', 'манати', 'манатів'), ('гяпік', 'гяпіки', 'гяпіків')),
        'BAM': (('марка', 'марки', 'марок'), ('фенінг', 'фенінги', 'фенінгів')),
        'BBD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BDT': (('така', 'таки', 'так'), ('пойша', 'пойші', 'пойш')),
        'BGN': (('лев', 'леви', 'левів'), ('стотинка', 'стотинки', 'стотинок')),
        'BHD': (('динар', 'динари', 'динарів'), ('філс', 'філси', 'філсів')),
        'BIF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'BMD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BND': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BOB': (('болівіано', 'болівіано', 'болівіано'), ('сентаво', 'сентаво', 'сентаво')),
        'BRL': (('реал', 'реали', 'реалів'), ('сентаво', 'сентаво', 'сентаво')),
        'BSD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BTN': (('нгултрум', 'нгултруми', 'нгултрумів'), ('четрум', 'четруми', 'четрумів')),
        'BWP': (('пула', 'пули', 'пул'), ('тхебе', 'тхебе', 'тхебе')),
        'BYN': (('рубель', 'рублі', 'рублів'), ('копійка', 'копійки', 'копійок')),
        'BZD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'CAD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'CDF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'CHF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'CLP': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'CNY': (('юань', 'юані', 'юанів'), ('финь', 'фині', 'финів')),
        'COP': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'CRC': (('колон', 'колони', 'колонів'), ('сентімо', 'сентімо', 'сентімо')),
        'CUC': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'CUP': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'CVE': (('ескудо', 'ескудо', 'ескудо'), ('сентаво', 'сентаво', 'сентаво')),
        'CZK': (('крона', 'крони', 'крон'), ('гелер', 'гелери', 'гелерів')),
        'DJF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'DKK': (('крона', 'крони', 'крон'), ('ере', 'ере', 'ере')),
        'DOP': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'DZD': (('динар', 'динари', 'динарів'), ('сантим', 'сантими', 'сантимів')),
        'EGP': (('фунт', 'фунти', 'фунтів'), ('піастр', 'піастри', 'піастрів')),
        'ERN': (('накфа', 'накфи', 'накф'), GENERIC_CENTS),
        'ETB': (('бир', 'бири', 'бирів'), GENERIC_CENTS),
        'EUR': (('євро', 'євро', 'євро'), GENERIC_CENTS),
        'FJD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'FKP': (('фунт', 'фунти', 'фунтів'), ('пенс', 'пенси', 'пенсів')),
        'GBP': (('фунт', 'фунти', 'фунтів'), ('пенс', 'пенси', 'пенсів')),
        'GEL': (('ларі', 'ларі', 'ларі'), ('тетрі', 'тетрі', 'тетрі')),
        'GHS': (('седі', 'седі', 'седі'), ('песева', 'песеви', 'песев')),
        'GIP': (('фунт', 'фунти', 'фунтів'), ('пенс', 'пенси', 'пенсів')),
        'GMD': (('даласі', 'даласі', 'даласі'), ('бутут', 'бутути', 'бутутів')),
        'GNF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'GTQ': (('кетсаль', 'кетсалі', 'кетсалів'), ('сентаво', 'сентаво', 'сентаво')),
        'GYD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'HKD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'HNL': (('лемпіра', 'лемпіри', 'лемпір'), ('сентаво', 'сентаво', 'сентаво')),
        'HRK': (('куна', 'куни', 'кун'), ('ліпа', 'ліпи', 'ліп')),
        'HTG': (('гурд', 'гурди', 'гурдів'), ('сантим', 'сантими', 'сантимів')),
        'HUF': (('форинт', 'форинти', 'форинтів'), ('філлер', 'філлери', 'філлерів')),
        'IDR': (('рупія', 'рупії', 'рупій'), GENERIC_CENTS),
        'ILS': (('шекель', 'шекелі', 'шекелів'), ('агора', 'агори', 'агор')),
        'INR': (('рупія', 'рупії', 'рупій'), ('пайса', 'пайси', 'пайс')),
        'IQD': (('динар', 'динари', 'динарів'), ('філс', 'філси', 'філсів')),
        'IRR': (('ріал', 'ріали', 'ріалів'), ('динар', 'динари', 'динарів')),
        'ISK': (('крона', 'крони', 'крон'), ('ейре', 'ейре', 'ейре')),
        'JMD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'JOD': (('динар', 'динари', 'динарів'), ('філс', 'філси', 'філсів')),
        'JPY': (('єна', 'єни', 'єн'), ('сен', 'сен', 'сен')),
        'KES': (('шилінг', 'шилінги', 'шилінгів'), GENERIC_CENTS),
        'KGS': (('сом', 'соми', 'сомів'), ('тиїн', 'тиїни', 'тиїнів')),
        'KHR': (('рієль', 'рієлі', 'рієлів'), ('су', 'су', 'су')),
        'KMF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'KPW': (('вона', 'вони', 'вон'), ('чон', 'чони', 'чонів')),
        'KRW': (('вона', 'вони', 'вон'), ('джеон', 'джеони', 'джеонів')),
        'KWD': (('динар', 'динари', 'динарів'), ('філс', 'філси', 'філсів')),
        'KYD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'KZT': (('теньге', 'теньге', 'теньге'), ('тиїн', 'тиїни', 'тиїнів')),
        'LAK': (('кіп', 'кіпи', 'кіпів'), ('ат', 'ати', 'атів')),
        'LBP': (('фунт', 'фунти', 'фунтів'), ('піастр', 'піастри', 'піастрів')),
        'LKR': (('рупія', 'рупії', 'рупій'), GENERIC_CENTS),
        'LRD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'LSL': (('лоті', 'малоті', 'малоті'), ('сенте', 'лісенте', 'лісенте')),
        'LYD': (('динар', 'динари', 'динарів'), ('дирхам', 'дирхами', 'дирхамів')),
        'MAD': (('дирхам', 'дирхами', 'дирхамів'), ('сантим', 'сантими', 'сантимів')),
        'MDL': (('лей', 'леї', 'леї'), ('бан', 'бані', 'бані')),
        'MGA': (('аріарі', 'аріарі', 'аріарі'), ('іраймбіланья', 'іраймбіланья', 'іраймбіланья')),
        'MKD': (('денар', 'денари', 'денарів'), ('дені', 'дені', 'дені')),
        'MMK': (('к\'ят', 'к\'ят', 'к\'ят'), ('п\'я', 'п\'я', 'п\'я')),
        'MNT': (('тугрик', 'тугрики', 'тугриків'), ('мунгу', 'мунгу', 'мунгу')),
        'MOP': (('патака', 'патакі', 'патак'), ('аво', 'аво', 'аво')),
        'MRU': (('угія', 'угії', 'угій'), ('хумс', 'хумс', 'хумс')),
        'MUR': (('рупія', 'рупії', 'рупій'), GENERIC_CENTS),
        'MVR': (('руфія', 'руфії', 'руфій'), ('ларі', 'ларі', 'ларі')),
        'MWK': (('квача', 'квачі', 'квач'), ('тамбала', 'тамбала', 'тамбала')),
        'MXN': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'MYR': (('рингіт', 'рингіти', 'рингітів'), GENERIC_CENTS),
        'MZN': (('метікал', 'метікали', 'метікалів'), ('сентаво', 'сентаво', 'сентаво')),
        'NAD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'NGN': (('найра', 'найри', 'найр'), ('кобо', 'кобо', 'кобо')),
        'NIO': (('кордоба', 'кордоби', 'кордоб'), ('сентаво', 'сентаво', 'сентаво')),
        'NOK': (('крона', 'крони', 'крон'), ('ере', 'ере', 'ере')),
        'NPR': (('рупія', 'рупії', 'рупій'), ('пайса', 'пайси', 'пайс')),
        'NZD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'OMR': (('ріал', 'ріали', 'ріалів'), ('байза', 'байзи', 'байз')),
        'PAB': (('бальбоа', 'бальбоа', 'бальбоа'), ('сентесімо', 'сентесімо', 'сентесімо')),
        'PEN': (('соль', 'соль', 'соль'), ('сентімо', 'сентімо', 'сентімо')),
        'PGK': (('кіна', 'кіна', 'кіна'), ('тойя', 'тойя', 'тойя')),
        'PHP': (('песо', 'песо', 'песо'), ('сентаво', 'сентаво', 'сентаво')),
        'PKR': (('рупія', 'рупії', 'рупій'), ('пайса', 'пайси', 'пайс')),
        'PLN': (('злотий', 'злоті', 'злотих'), ('грош', 'гроші', 'грошів')),
        'PYG': (('гуарані', 'гуарані', 'гуарані'), ('сентімо', 'сентімо', 'сентімо')),
        'QAR': (('ріал', 'ріали', 'ріалів'), ('дирхам', 'дирхами', 'дирхамів')),
        'RON': (('лей', 'леї', 'леї'), ('бан', 'бані', 'бані')),
        'RSD': (('динар', 'динари', 'динарів'), ('пара', 'пари', 'пар')),
        'RUB': (('рубль', 'рублі', 'рублів'), ('копійка', 'копійки', 'копійок')),
        'RWF': (('франк', 'франки', 'франків'), ('сантим', 'сантими', 'сантимів')),
        'SAR': (('ріал', 'ріали', 'ріалів'), ('халал', 'халали', 'халалів')),
        'SBD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'SCR': (('рупія', 'рупії', 'рупій'), GENERIC_CENTS),
        'SDG': (('фунт', 'фунти', 'фунтів'), ('піастр', 'піастри', 'піастрів')),
        'SEK': (('крона', 'крони', 'крон'), ('ере', 'ере', 'ере')),
        'SGD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'SHP': (('фунт', 'фунти', 'фунтів'), ('пенс', 'пенси', 'пенсів')),
        'SLL': (('леоне', 'леоне', 'леоне'), GENERIC_CENTS),
        'SOS': (('шилінг', 'шилінги', 'шилінгів'), GENERIC_CENTS),
        'SRD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'SSP': (('фунт', 'фунти', 'фунтів'), ('піастр', 'піастри', 'піастрів')),
        'STN': (('добра', 'добри', 'добр'), ('сентімо', 'сентімо', 'сентімо')),
        'SYP': (('фунт', 'фунти', 'фунтів'), ('піастр', 'піастри', 'піастрів')),
        'SZL': (('ліланґені', 'ліланґені', 'ліланґені'), GENERIC_CENTS),
        'THB': (('бат', 'бати', 'батів'), ('сатанг', 'сатанги', 'сатангів')),
        'TJS': (('сомоні', 'сомоні', 'сомоні'), ('дірам', 'дірами', 'дірамів')),
        'TMT': (('манат', 'манати', 'манатів'), ('тенге', 'тенге', 'тенге')),
        'TND': (('динар', 'динари', 'динарів'), ('міллім', 'мілліми', 'міллімів')),
        'TOP': (('паанга', 'паанга', 'паанга'), ('сеніті', 'сеніті', 'сеніті')),
        'TRY': (('ліра', 'ліри', 'лір'), ('куруш', 'куруші', 'курушів')),
        'TTD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'TWD': (('новий долар', 'нові долари', 'нових доларів'), GENERIC_CENTS),
        'TZS': (('шилінг', 'шилінги', 'шилінгів'), GENERIC_CENTS),
        'UAH': (('гривня', 'гривні', 'гривень'), ('копійка', 'копійки', 'копійок')),
        'UGX': (('шилінг', 'шилінги', 'шилінгів'), GENERIC_CENTS),
        'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'UYU': (('песо', 'песо', 'песо'), ('сентесімо', 'сентесімо', 'сентесімо')),
        'UZS': (('сум', 'суми', 'сумів'), ('тиїн', 'тиїни', 'тиїнів')),
        'VND': (('донг', 'донги', 'донгів'), ('су', 'су', 'су')),
        'WST': (('тала', 'тали', 'тал'), ('сене', 'сене', 'сене')),
        'XCD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'YER': (('ріал', 'ріали', 'ріалів'), ('філс', 'філси', 'філсів')),
        'ZAR': (('ранд', 'ранди', 'рандів'), GENERIC_CENTS),
        'ZMW': (('квача', 'квачі', 'квач'), ('нгве', 'нгве', 'нгве')),
    }

    def setup(self):
        self.negword = "мінус"
        self.pointword = "кома"

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            return '%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                self._int2word(int(right))
            )
        else:
            return self._int2word(int(n))

    def pluralize(self, n, forms):
        if n % 100 < 10 or n % 100 > 20:
            if n % 10 == 1:
                form = 0
            elif 5 > n % 10 > 1:
                form = 1
            else:
                form = 2
        else:
            form = 2

        return forms[form]

    def _int2word(self, n, feminine=False):
        if n < 0:
            return ' '.join([self.negword, self._int2word(abs(n))])

        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            if n3 > 0:
                words.append(HUNDREDS[n3][0])

            if n2 > 1:
                words.append(TWENTIES[n2][0])

            if n2 == 1:
                words.append(TENS[n1][0])
            # elif n1 > 0 and not (i > 0 and x == 1):
            elif n1 > 0:
                ones = ONES_FEMININE if i == 1 or feminine and i == 0 else ONES
                words.append(ones[n1][0])

            if i > 0:
                words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)

    def _money_verbose(self, number, currency):
        return self._int2word(number, currency in FEMININE_MONEY)

    def _cents_verbose(self, number, currency):
        return self._int2word(number, currency in FEMININE_CENTS)

    def to_ordinal(self, number):
        raise NotImplementedError()
