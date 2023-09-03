def main(size, text_align, text):
    """wertyui"""
    if text_align == "center":
        print(text.center(size))
    elif text_align == "left":
        print(text.ljust(size))
    elif text_align == "right":
        print(text.rjust(size))
main(int(input()), str(input()), str(input()))