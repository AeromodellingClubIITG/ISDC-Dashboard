import csv
import os
import time
import json
from datetime import datetime
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import cv2
from threading import Thread, Lock
from . import bmpsensor

# Directory for storing data
data_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(data_dir, exist_ok=True)

# Generate a new file for each server run
file_counter = len([f for f in os.listdir(data_dir) if f.startswith('sensor_data_mission_')]) + 1
csv_file_path = os.path.join(data_dir, f'sensor_data_mission_{file_counter:02d}.csv')

sensor_data = []
lock = Lock()

# Initialize the new CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Temperature (°C)", "Pressure (Pa)", "Altitude (m)"])


# Background thread for reading sensor data
def sensor_data_thread():
    global sensor_data
    while True:
        temp, pressure, altitude = bmpsensor.readBmp180()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Add data to the list
        with lock:
            sensor_data.append({
                "time": current_time,
                "temperature": temp,
                "pressure": pressure,
                "altitude": altitude
            })

            # Save data to the unique CSV file
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([current_time, temp, pressure, altitude])

        time.sleep(2)


# Start the sensor thread
Thread(target=sensor_data_thread, daemon=True).start()


# Video stream generator
def gen():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    file_number = len([name for name in os.listdir(data_dir) if name.startswith('video_')]) + 1
    out = cv2.VideoWriter(os.path.join(data_dir, f'video_{file_number:02d}.avi'),
                          cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    cap.release()
    out.release()


# Views
def index(request):
    return render(request, 'livefeed/index.html')


def video_feed(request):
    return StreamingHttpResponse(gen(), content_type='multipart/x-mixed-replace; boundary=frame')


def get_sensor_data(request):
    global sensor_data
    with lock:
        data_copy = list(sensor_data)
        sensor_data = []  # Clear after sending to avoid duplication
    return JsonResponse(data_copy, safe=False)
