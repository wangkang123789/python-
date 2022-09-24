

def test(num):
    """

    :param num:
    :return:
    """
    print("a的地址是%d" % id(num))
    return num


a = 10
print("a的地址是%d" % id(a))
print("")
r = test(a)
print("r的地址是%d" % id(r))
