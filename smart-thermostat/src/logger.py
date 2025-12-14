from datetime import datetime

class ThermostatLogger:
    
    def __init__(self, log_file='thermostat.log'):    
        self.log_file = log_file
    
    def lof(self, temperature, mode):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, "a") as f:
            f.write(f"{timestamp} | {temperature} | {mode}\n")