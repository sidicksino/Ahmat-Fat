from django.shortcuts import render

import requests

def home_view(request):
    try:
        response = requests.get('https://api.coincap.io/v2/assets?limit=3', timeout=5)
        response_json = response.json()
        data = response_json.get('data', [])
        print(f"Crypto Data: {data}")
    except Exception as e:
        print(f"Error fetching data: {e}")
        # Fallback Mock Data for when API fails (e.g. no internet)
        data = [
            {'name': 'Bitcoin', 'symbol': 'BTC', 'priceUsd': '95000.00', 'changePercent24Hr': '2.5'},
            {'name': 'Ethereum', 'symbol': 'ETH', 'priceUsd': '4500.00', 'changePercent24Hr': '-1.2'},
            {'name': 'Tether', 'symbol': 'USDT', 'priceUsd': '1.00', 'changePercent24Hr': '0.01'},
        ]

    return render(request, 'API/home.html', {'crypto_data': data})
