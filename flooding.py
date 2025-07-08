from pymavlink import mavutil
import time

# Connect to SITL drone (change IP if needed)
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

# Wait for the heartbeat msg to find the system ID
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

# Function to send dummy attitude messages rapidly
def simulate_high_traffic():
    print("Simulating MAVLink traffic flood...")
    for i in range(1000):  # Flood with 1000 messages
        master.mav.attitude_send(
            time.time(),      # timestamp
            0.1, 0.2, 0.3,     # roll, pitch, yaw
            0.01, 0.02, 0.03   # rollspeed, pitchspeed, yawspeed
        )
        time.sleep(0.01)  # ~100 msgs/sec

simulate_high_traffic()
