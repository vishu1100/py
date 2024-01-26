from gpiozero import LED
import keyboard
import time

class SmartHomeSystem:
    def __init__(self):
        self.lights = {
            'living_room': LED(17),  # Simulated GPIO pin for living room lights
            'bedroom': LED(18)       # Simulated GPIO pin for bedroom lights
        }
        self.temperature = 22  # Simulated room temperature in Celsius

    def control_lights(self, room, action):
        light = self.lights.get(room)
        if light:
            if action == 'on':
                light.on()
                print(f"{room.capitalize()} lights turned ON.")
            elif action == 'off':
                light.off()
                print(f"{room.capitalize()} lights turned OFF.")
            else:
                print("Invalid action. Use 'on' or 'off'.")
        else:
            print(f"No lights found in the {room}.")

    def control_temperature(self, action):
        if action == 'increase':
            self.temperature += 1
        elif action == 'decrease':
            self.temperature -= 1
        else:
            print("Invalid action. Use 'increase' or 'decrease'.")
            return

        print(f"Temperature adjusted to {self.temperature}°C.")

    def run(self):
        print("Smart Home Automation System")
        print("Press 'q' to quit.")

        while True:
            try:
                key_event = keyboard.read_event()
                if key_event.event_type == keyboard.KEY_DOWN:
                    key_name = key_event.name.lower()

                    if key_name == 'q':
                        print("Exiting Smart Home System.")
                        break

                    elif key_name in ('on', 'off'):
                        room = input("Enter room (e.g., living_room): ")
                        self.control_lights(room, key_name)

                    elif key_name in ('increase', 'decrease'):
                        self.control_temperature(key_name)

            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    smart_home_system = SmartHomeSystem()
    smart_home_system.run()
