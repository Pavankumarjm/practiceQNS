def reverse_only_letters(s):
    arr = list(s)
    left, right = 0, len(arr) - 1

    def is_letter(char):
        return char.isalpha()

    while left < right:
        if not is_letter(arr[left]):
            left += 1
        elif not is_letter(arr[right]):
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return "".join(arr)