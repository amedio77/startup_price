from datetime import datetime


class Util:
    @staticmethod
    def compare_dates(date1, date2):
        date_format = "%Y년 %m월 %d일"
        parsed_date1 = datetime.strptime(date1, date_format)
        parsed_date2 = datetime.strptime(date2, date_format)
        # # 두 날짜를 비교합니다.
        # if parsed_date1 == parsed_date2:
        #     return "두 날짜는 동일합니다."
        # elif parsed_date1 < parsed_date2:
        #     return f"{date1}은 {date2}보다 이전입니다."
        # else:
        #     return f"{date1}은 {date2}보다 이후입니다."
        # 두 날짜를 비교합니다.
        if parsed_date1 == parsed_date2:
            return 0
        elif parsed_date1 < parsed_date2:
            return 1
        else:
            return -1


