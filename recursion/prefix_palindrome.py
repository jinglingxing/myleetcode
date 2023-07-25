# Constraint: 0<=len(s)<=1000
# Given a string:
# 1.) Take all prefixes of the string and choose the longest palindrome between them.
# 2.) If chosen prefix has at least two characters, cut this from s and go back to step 1 with the updated string.
# Otherwise, end the algo with the current string s.
# e.g. s = "aaacodedoc", return ""; s = "codesignal", return codesignal

def check_palindrome(prefix):
    return prefix == prefix[::-1]


def prefix_palindrome(s):
    arr1 = []
    arr2 = []
    i = 0
    j = 1
    while j <= len(s):
        arr1.append(s[i:j])
        j += 1

    for item in arr1:
        if check_palindrome(item) and len(item) >= 2:
            arr2.append(item)

    if len(arr2) == 0:
        return s
    else:
        updated_string = s.strip(arr2[-1])
        if updated_string:
            prefix_palindrome(updated_string)
        return ''


if __name__ == '__main__':
    s1 = "aaacodedoc"
    s2 = "codesignal"
    print(prefix_palindrome(s1))
    print(prefix_palindrome(s2))
