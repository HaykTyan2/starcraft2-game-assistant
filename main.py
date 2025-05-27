import threading
from supply_depot import run_supply_monitor
from minimap_alert import run_minimap_alert

if __name__ == "__main__":
    t1 = threading.Thread(target=run_supply_monitor)
    t2 = threading.Thread(target=run_minimap_alert)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
