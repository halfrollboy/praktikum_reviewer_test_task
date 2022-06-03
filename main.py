import datetime as dt

# Нет докстрингов к классам и функциям
class Record: 
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            # Не верно написаны переносы для if
            dt.datetime.now().date() if 
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator: 
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    # Желательно писать тайпхинтинги
    # Т.Е. типы того что ты передаёшь напримерн (record: str)
    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # Использовать переменные цикла с маленькой буквы
        # с большой буквы используются только названия классов
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Надо использовать докстринги для описания действия функций
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            # Нельзя использовать бэкслэши в f строках 
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # Можно не писать else а просто вернуть в return самой функции
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        # Попробовать поменять множественные if на более понятную конструкцию.
        # Не надо использование то currency_type то currency
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            # Использовать только один язык для обызначений
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                # Нельзя использовать операции в f строках  
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # Не использовать бэкслэши в f строчках
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
    # Можно не переопределять он автоматически наследуется
    def get_week_stats(self):
        # Если не переопределять то будет работать без super 
        super().get_week_stats() 


# Нет  if __name__ == "__main__":