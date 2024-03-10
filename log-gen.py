import argparse
from datetime import datetime, timedelta

class LogGenerate:
    param = ""

    def __init__(self, param_):
        self.param = param_
    
    def print_date(self, date_obj):
        print(date_obj.strftime('%Y/%m/%d(%a)'))
        day = date_obj.strftime('%d')
        print(day)

    def generate(self):
        print(f"param : {self.param}")
        try:
            parse_date = datetime.strptime(self.param, '%Y%m')
            first_day = datetime(parse_date.year, parse_date.month, 1)

            while parse_date.month == first_day.month:
                self.print_date(parse_date)
                parse_date += timedelta(days=1)
        except ValueError:
            print('Invalid Value')     


def main(parm):
    obj = LogGenerate(param)
    obj.generate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="parse cmd line")
    parser.add_argument('-o','--output', type=str, required=False)
    args = parser.parse_args()

    param = 0
    print('file name', args.output)
    if args.output == None:
        today = datetime.now()
        param = today.strftime("%Y%m")
    else:
        param = args.output

    main(param)
