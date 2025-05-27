import threading
import keyboard
from supply_depot import run_supply_monitor
from minimap_alert import run_minimap_alert

# Create a shutdown event
stop_event = threading.Event()

def watch_for_exit():
    print("Press 'q' to quit the assistant.")
    keyboard.wait('q')
    print("Exit key pressed. Stopping...")
    stop_event.set()  # signal all threads to stop

if __name__ == "__main__":
    # Start exit watcher thread
    exit_thread = threading.Thread(target=watch_for_exit, daemon=True)
    exit_thread.start()

    # Start the assistant threads and pass the stop_event
    t1 = threading.Thread(target=run_supply_monitor, args=(stop_event,))
    t2 = threading.Thread(target=run_minimap_alert, args=(stop_event,))
    t1.start()
    t2.start()

    # Wait for both to finish
    t1.join()
    t2.join()

    print("Program exited cleanly.")
