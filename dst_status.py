def DST_LEVEL(x):
    if 1 == x:
        return"배송준비중"
    elif 2 == x:
        return "집화완료"
    elif 3 == x:
        return "배송중"
    elif 4 == x:
        return "지점 도착"
    elif 5 == x:
        return "배송출발"
    elif 6 == x:
        return "배송 완료"
    else:
        return "Error"


def DST_CompleteYN(y):
    if "Y" == y:
        return "배송이 완료되었습니다."
    elif "N" == y:

        return "배송중 ... ... ..."
    else:
        return "Error"