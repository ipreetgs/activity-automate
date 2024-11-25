import pyautogui
import time
import random
from datetime import datetime
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('teams_activity.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class TeamsActivityMaintainer:
    def __init__(self, interval_minutes=4):
        self.interval_minutes = interval_minutes
        self.running = True
        
    def move_mouse_slightly(self):
        """Move mouse a small random amount from current position"""
        current_x, current_y = pyautogui.position()
        offset_x = random.randint(-100, 100)
        offset_y = random.randint(-100, 100)
        
        try:
            # Move mouse smoothly to new position
            pyautogui.moveTo(
                current_x + offset_x,
                current_y + offset_y,
                duration=0.5
            )
            # Return to original position
            pyautogui.moveTo(current_x, current_y, duration=0.5)
            
        except Exception as e:
            logging.error(f"Error moving mouse: {str(e)}")
    
    def simulate_keypress(self):
        """Press and release a harmless key (shift)"""
        try:
            pyautogui.press('shift')
        except Exception as e:
            logging.error(f"Error simulating keypress: {str(e)}")
    
    def maintain_activity(self):
        """Main loop to maintain activity"""
        logging.info("Starting Teams activity maintenance")
        
        try:
            while self.running:
                current_time = datetime.now().strftime("%H:%M:%S")
                logging.info(f"Performing activity simulation at {current_time}")
                
                # Randomly choose between mouse movement and keypress
                if random.choice([True, False]):
                    self.move_mouse_slightly()
                    logging.info("Moved mouse")
                else:
                    self.simulate_keypress()
                    logging.info("Simulated keypress")
                
                # Sleep for the specified interval with some randomness
                sleep_time = self.interval_minutes * 60 + random.randint(-30, 30)
                time.sleep(sleep_time)
                
        except KeyboardInterrupt:
            logging.info("Activity maintenance stopped by user")
            self.running = False
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            self.running = False

if __name__ == "__main__":
    # Create and run the activity maintainer
    maintainer = TeamsActivityMaintainer(interval_minutes=4)
    maintainer.maintain_activity()
