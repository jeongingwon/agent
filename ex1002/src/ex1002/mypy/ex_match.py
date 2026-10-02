day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
        print("문서1")
        print("문서2")
        print("문서3")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")



# --------------------------------


day2 = 4

match day2:
    case 6:
        print("오늘은 화요일")
    case 7:
        print("오늘은 수요일")
    case _:
        print("일치하는 ㅏㅄ이 없으면 Case_ 출력함.")