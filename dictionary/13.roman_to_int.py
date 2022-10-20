class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            # consider special case first
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,

            # normal cases
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        for k, v in dic.items():
            res += s.count(k) * v
            s = s.replace(k, '')
        return res