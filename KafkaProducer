pip install kafka-python

import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json
import requests
import time

producer = KafkaProducer(bootstrap_servers=['18.217.20.39:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

producer.send('demo_test1', value={'name':'vamsikrishna'})

API_KEY = '4e51ed05113e3e2560cefa3e577a44e3'  
API_URL = 'http://api.weatherstack.com/current'
KAFKA_TOPIC = 'demo_test1'

LOCATIONS = ['New Delhi','Tampa']
batch = []

def fetch_weather_data(location):
    """Fetch weather data for a specific location from the Weatherstack API."""
    url = f"{API_URL}?access_key={API_KEY}&query={location}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {location}: {e}")
        return None

def produce_weather_data():
    while True:
        weather_data_batch = []  # To store weather data for all locations

        # Fetch data for all locations at once
        for location in LOCATIONS:
            print(f"Fetching data for {location}...")
            weather_data = fetch_weather_data(location)
            if weather_data:
                if 'current' in weather_data:
                    weather_data_batch.append(weather_data)
                    print(f"Fetched data for {location}: {weather_data}")
                else:
                    print(f"Invalid response for {location}: {weather_data}")
            else:
                print(f"No data fetched for {location}")

        # Send all weather data for all locations to Kafka
        if weather_data_batch:
            for data in weather_data_batch:
                producer.send(KAFKA_TOPIC, value=data)
                producer.flush()
                print(f"Sent data to Kafka: {data}")

        producer.close()  # Close the producer after sending data for all locations

        # Wait for 24 hours before fetching data again
        print("Waiting for 24 hours before fetching data again...")
        time.sleep(86400)  # Wait for 24 hours (86400 seconds) before fetching data again


if __name__ == "__main__":
    try:
        print("Starting Kafka Producer...")
        produce_weather_data()
    except KeyboardInterrupt:
        print("Shutting down Kafka Producer.")
    except Exception as e:
        print(f"An error occurred: {e}")

