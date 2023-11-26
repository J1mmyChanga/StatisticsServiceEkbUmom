import datetime
import calendar

from data.db_session import global_init, create_session
from data.models import Dishs, OrderStatistics
from random import *

global_init()
session = create_session()

d1 = Dishs(title='Каша молочная 3 злака', category='Завтраки', price=80, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d2 = Dishs(title='Каша ячневая постная с фруктами', category='Завтраки', price=100, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d3 = Dishs(title='Жареная ветчина', category='Завтраки', price=70, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d4 = Dishs(title='Пудинг творожный с бананом', category='Завтраки', price=90, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d5 = Dishs(title='Драники картофельные с зеленью', category='Завтраки', price=125, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d6 = Dishs(title='Оладьи из кабачков ', category='Завтраки', price=80, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d7 = Dishs(title='Брускета с беконом', category='Завтраки', price=75, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d8 = Dishs(title='Яйцо отварное', category='Завтраки', price=80, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d9 = Dishs(title='Яичница глазунья', category='Завтраки', price=95, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d10 = Dishs(title='Омлет с зеленым луком', category='Завтраки', price=85, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d11 = Dishs(title='Филе Кеты в кляре', category='Основные блюда', price=105, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d12 = Dishs(title='Филе куриное запеченное с кабачками и сыром', category='Основные блюда', price=105, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d13 = Dishs(title='Свинина по-французски', category='Основные блюда', price=140, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d14 = Dishs(title='Котлета по киевски', category='Основные блюда', price=90, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d15 = Dishs(title='Курица жареная с аджикой', category='Основные блюда', price=95, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d16 = Dishs(title='Каша гречневая томленная', category='Гарниры', price=70, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d17 = Dishs(title='Тыква запеченая с розмарином', category='Гарниры', price=85, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d18 = Dishs(title='Рагу овощное', category='Гарниры', price=100, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d19 = Dishs(title='Рис отварной с карри', category='Гарниры', price=80, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d20 = Dishs(title='Салат из крабовых палочек с огурцами', category='Закуски и салаты', price=75, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d21 = Dishs(title='Салат Ассорти из морской капусты', category='Закуски и салаты', price=65, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d22 = Dishs(title='Салат Звёздный', category='Закуски и салаты', price=70, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d23 = Dishs(title='Салат колбасный', category='Закуски и салаты', price=85, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d24 = Dishs(title='Салат Чап-ча с болгарским перцем', category='Закуски и салаты', price=90, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d25 = Dishs(title='Суп-крем из шампиньонов', category='Первые блюда', price=110, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d26 = Dishs(title='Борщ Сибирский с курой', category='Первые блюда', price=140, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
d27 = Dishs(title='Суп Палиц', category='Первые блюда', price=120, callories=randint(120, 470), proteins=randint(3, 50), fats=randint(3, 70), carbohydrates=randint(5, 90))
for i in range(1, 28):
    session.add(eval(f'd{i}'))

def random_date():
    start_date = datetime.datetime.now()
    end_date = start_date + datetime.timedelta(days=10)
    random_date = start_date + (end_date - start_date) * random()
    return random_date.date()

def create_data(n):
    order_day = random_date()
    dish = session.query(Dishs).filter(Dishs.id == n)[0]
    dish_id = dish.id
    category = dish.category
    dish_title = dish.title
    price = dish.price
    callories = dish.callories
    proteins = dish.proteins
    fats = dish.fats
    carbohydrates = dish.carbohydrates
    week_day=calendar.day_name[order_day.weekday()]
    weekend = 1 if order_day.weekday() >= 5 else 0
    meat = choice([True, False])
    raw_food = choice([True, False])
    lenten_food = choice([True, False])
    milk_food = choice([True, False])
    weather = choice(['Пасмурно', 'Дождливо', 'Солнечно', 'Жарко', 'Холодно', 'Сыро'])

    order = OrderStatistics(dish_id=dish_id, category=category, dish_title=dish_title, price=price, callories=callories, proteins=proteins, fats=fats,
                            carbohydrates=carbohydrates, week_day=week_day, weekend=weekend, meat=meat, raw_food=raw_food, lenten_food=lenten_food,
                            milk_food=milk_food, order_day=order_day, weather=weather
                            )
    return order


for i in range(100):
    session.add(create_data(randint(1, 27)))
a = []
session.commit()