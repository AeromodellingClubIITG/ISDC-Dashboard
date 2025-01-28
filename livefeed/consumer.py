import json
import paramiko
from channels.generic.websocket import AsyncWebsocketConsumer

class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Start fetching sensor data over SSH in real-time
        host = "us1.pitunnel.net"
        username = "raj"
        password = "raj"
        command = "tail -f /path/to/sensor_data.txt"  # Adjust command as needed

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            _, stdout, _ = ssh.exec_command(command)

            # Continuously fetch data and send it to the client
            for line in iter(stdout.readline, ""):
                if line.strip():
                    await self.send(json.dumps({"data": line.strip()}))

        except Exception as e:
            await self.send(json.dumps({"error": str(e)}))
        finally:
            ssh.close()

    async def disconnect(self, close_code):
        pass
