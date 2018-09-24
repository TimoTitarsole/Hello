def new_password(newpassword):
    res = newpassword is not oldpassword and len(str(newpassword)) >= 6
    print(res)

oldpassword = 12345678
new_password(123456789)