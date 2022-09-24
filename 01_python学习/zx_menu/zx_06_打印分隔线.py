
def print_line(char, times):
    """打印单行分割线

    :param char:分隔的字符
    :param times:字符的个数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char:分隔的字符
    :param times:字符的个数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


# print_lines("&", 5)
