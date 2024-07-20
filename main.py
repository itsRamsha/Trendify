from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data for trend prediction
data = {
    'Clothing': {

        'Shirts': {
            'yearly': {
                '2020': 300, '2021': 320, '2022': 340, '2023': 360, '2024': 380,
                '2025': 400, '2026': 420, '2027': 440, '2028': 460, '2029': 480,
                '2030': 500, '2031': 520
            },
            'monthly': {
                'January': 30, 'February': 40, 'March': 50, 'April': 60,
                'May': 70, 'June': 80, 'July': 90, 'August': 100,
                'September': 110, 'October': 120, 'November': 130, 'December': 140
            }
        },
        'Pants': {
            'yearly': {
                '2020': 250, '2021': 270, '2022': 290, '2023': 310, '2024': 330,
                '2025': 350, '2026': 370, '2027': 390, '2028': 410, '2029': 430,
                '2030': 450, '2031': 470
            },
            'monthly': {
                'January': 25, 'February': 35, 'March': 45, 'April': 55,
                'May': 65, 'June': 75, 'July': 85, 'August': 95,
                'September': 105, 'October': 115, 'November': 125, 'December': 135
            }
        },
        'Dresses': {
            'yearly': {
                '2020': 200, '2021': 210, '2022': 220, '2023': 230, '2024': 240,
                '2025': 250, '2026': 260, '2027': 270, '2028': 280, '2029': 290,
                '2030': 300, '2031': 310
            },
            'monthly': {
                'January': 20, 'February': 30, 'March': 40, 'April': 50,
                'May': 60, 'June': 70, 'July': 80, 'August': 90,
                'September': 100, 'October': 110, 'November': 120, 'December': 130
            }
        }
    },
    'Footwear': {

        'Shoes': {
            'yearly': {
                '2020': 300, '2021': 320, '2022': 340, '2023': 360, '2024': 380,
                '2025': 400, '2026': 420, '2027': 440, '2028': 460, '2029': 480,
                '2030': 500, '2031': 520
            },
            'monthly': {
                'January': 30, 'February': 40, 'March': 50, 'April': 60,
                'May': 70, 'June': 80, 'July': 90, 'August': 100,
                'September': 110, 'October': 120, 'November': 130, 'December': 140
            }
        },
        'Slippers': {
            'yearly': {
                '2020': 250, '2021': 270, '2022': 290, '2023': 310, '2024': 330,
                '2025': 350, '2026': 370, '2027': 390, '2028': 410, '2029': 430,
                '2030': 450, '2031': 470
            },
            'monthly': {
                'January': 135, 'February': 95, 'March': 45, 'April': 155,
                'May': 165, 'June': 75, 'July': 85, 'August': 195,
                'September': 10, 'October': 15, 'November': 125, 'December': 35
            }
        },
        'Sandals': {
            'yearly': {
                '2020': 200, '2021': 210, '2022': 220, '2023': 230, '2024': 240,
                '2025': 250, '2026': 260, '2027': 270, '2028': 280, '2029': 290,
                '2030': 300, '2031': 310
            },
            'monthly': {
                'January': 20, 'February': 30, 'March': 40, 'April': 50,
                'May': 60, 'June': 70, 'July': 80, 'August': 90,
                'September': 100, 'October': 110, 'November': 120, 'December': 130
            }
        }
    },
    'Accessories': {

        'Hats': {
            'yearly': {
                '2020': 300, '2021': 320, '2022': 340, '2023': 360, '2024': 380,
                '2025': 400, '2026': 420, '2027': 440, '2028': 460, '2029': 480,
                '2030': 500, '2031': 520
            },
            'monthly': {
                'January': 30, 'February': 40, 'March': 50, 'April': 60,
                'May': 70, 'June': 80, 'July': 90, 'August': 100,
                'September': 110, 'October': 120, 'November': 130, 'December': 140
            }
        },
        'Belts': {
            'yearly': {
                '2020': 250, '2021': 270, '2022': 290, '2023': 310, '2024': 330,
                '2025': 350, '2026': 370, '2027': 390, '2028': 410, '2029': 430,
                '2030': 450, '2031': 470
            },
            'monthly': {
                'January': 25, 'February': 35, 'March': 45, 'April': 55,
                'May': 65, 'June': 75, 'July': 85, 'August': 95,
                'September': 105, 'October': 115, 'November': 125, 'December': 135
            }
        },
        'Scarves': {
            'yearly': {
                '2020': 200, '2021': 210, '2022': 220, '2023': 230, '2024': 240,
                '2025': 250, '2026': 260, '2027': 270, '2028': 280, '2029': 290,
                '2030': 300, '2031': 310
            },
            'monthly': {
                'January': 20, 'February': 30, 'March': 40, 'April': 50,
                'May': 60, 'June': 70, 'July': 80, 'August': 90,
                'September': 100, 'October': 110, 'November': 120, 'December': 130
            }
        }
    }
}


@app.route('/')
def dash():
    return render_template('dash.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    request_data = request.get_json()
    product = request_data.get('product')
    timeframe = request_data.get('timeframe')
    subcategory = request_data.get('subcategory')
    print(product, timeframe, subcategory)
    if subcategory:
        result = data.get(product, {}).get(subcategory, {}).get(timeframe, {})
        print(result)
    else:
        result = data.get(product, {}).get(timeframe, {})
        print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
