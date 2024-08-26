from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from unixtodate import ToDate
from genp import password_generation


if __name__ == '__main__':
    now_date = datetime.date.today()
    print(now_date)
    calculate_salary()
    get_employees()
    n_date = ToDate(1724291652)
    print(f'{n_date.get_days_and_word(lang='ru')} прошло с момента зачисления в штат сотрудников 1, 2')
    print(password_generation(True, True,True,8))

