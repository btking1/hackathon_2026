from flask import Flask, jsonify, request
from weather_service import WeatherService

app = Flask(__name__)
service = WeatherService(api_key="abc123fake")


@app.route('/api/weather/<city>')
def get_weather(city):
    weather = service.get_current_weather(city)
    return jsonify(weather)


@app.route('/api/forecast/<city>')
def get_forecast(city):
    days = request.args.get('days', 5, type=int)
    forecast = service.get_forecast(city, days)
    return jsonify(forecast)


if __name__ == '__main__':
    app.run(debug=True)
