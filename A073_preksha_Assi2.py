import time
import schedule
from plyer import notification

def send_break_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def hydration_alert():
    send_break_alert("Hydration Alert", "Time to drink a glass of water!")

def posture_check():
    send_break_alert("Posture Check", "Check your posture and do a quick stretch.")

schedule.every(10).seconds.do(hydration_alert)
schedule.every(20).seconds.do(posture_check)

if __name__ == "__main__":
    print("Starting Desktop Health & Break Reminder Daemon...")
    print("Press Ctrl+C to exit.")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected (Ctrl+C). Exiting the health daemon safely. Have a great day!")