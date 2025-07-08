from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

print("Connecting to Mission Planner SITL...")
vehicle = connect("udp:127.0.0.1:14550", wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    print("Waiting for drone to become armable...")
    while not vehicle.is_armable:
        time.sleep(1)

    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print(f"Taking off to {aTargetAltitude} meters...")
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        alt = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {alt:.2f}")
        if alt >= aTargetAltitude * 0.95:
            break
        time.sleep(1)

arm_and_takeoff(10)

print("Hovering for 10 seconds...")
time.sleep(10)

print("Returning to Launch...")
vehicle.mode = VehicleMode("RTL")

time.sleep(10)
vehicle.close()
print("Mission Complete.")
