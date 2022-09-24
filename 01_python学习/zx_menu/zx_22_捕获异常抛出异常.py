def InputPasswd():
    passwd = input("请输入密码：")

    if len(passwd) >= 8:
        return passwd

    # 当密码长度小于八位时，创建一个异常，使用Exception来创建异常
    ex = Exception("密码长度小于八位")
    # 抛出异常要用raise，而不是return
    # return ex
    raise ex


try:
    pd = InputPasswd()
    print(pd)
except Exception as result:
    print("错误是：%s" % result)
else:
    print("尝试成功")
