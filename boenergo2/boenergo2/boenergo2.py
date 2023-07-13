import random
from flask import Flask, request, jsonify

app = Flask(__name__)

color_probabilities = {
    'blue': 0.7,   # Вероятность синего цвета
    'green': 0.2,  # Вероятность зелёного цвета
    'red': 0.1     # Вероятность красного цвета
}

@app.route('/guess-color', methods=['POST'])
def guess_color():
    data = request.json
    item_number = data.get('item_number')

    if item_number is None:
        return jsonify({'error': 'Item number is missing.'}), 400

    if item_number > 100:
        return jsonify({'error': 'Item number cannot be greater than 100.'}), 400

    # Генерация случайного числа от 0 до 1
    random_number = random.uniform(0, 1)

    cumulative_probability = 0
    for color, probability in color_probabilities.items():
        cumulative_probability += probability

        # Если случайное число попало в интервал, соответствующий текущей вероятности,
        # то выбираем этот цвет
        if random_number <= cumulative_probability:
            return jsonify({'item_number': item_number, 'color': color})

    # Если ни один цвет не выбран (например, вероятности некорректно заданы),
    # возвращаем сообщение об ошибке
    return jsonify({'error': 'Failed to guess the color.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
