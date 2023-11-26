from flask import Flask, jsonify
from data.db_session import *
from data.models import OrderStatistics

app = Flask(__name__)
global_init()
session = create_session()


@app.route('/statistics')
def get_statistics():
    res = {}
    for i in session.query(OrderStatistics).all():
        res[i.id] = {
            "dish_id": i.dish_id,
            "category": i.category,
            "dish_title": i.dish_title,
            "price": i.price,
            "order_day": i.order_day,
            "week_day": i.week_day,
            "weather": i.weather,
            "weekend": i.weekend,
            "callories": i.callories,
            "proteins": i.proteins,
            "fats": i.fats,
            "carbohydrates": i.carbohydrates,
            "meat": i.meat,
            "raw_food": i.raw_food,
            "lenten_food": i.lenten_food,
            "milk_food": i.milk_food,
        }

    return jsonify(res)


if __name__ == '__main__':
    app.run()
