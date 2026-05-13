import os
import json

FILENAME = "records.json"

class Tracker:
    def __init__(self):
        self.data_list = []
        self.load()

    def p_proc(self, s):
        try:
            a = s.split('/')
            if len(a) < 3:
                return None
            return {"n": a[0], "p": int(a[1]), "t": a[2]}
        except (ValueError, IndexError):
            return None

    def save(self):
        try:
            with open(FILENAME, "w") as f:
                json.dump(self.data_list, f)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load(self):
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as f:
                    self.data_list = json.load(f)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading data: {e}")

    def add_entry(self, raw_data):
        res = self.p_proc(raw_data)
        if res is not None:
            self.data_list.append(res)
            print("Entry added successfully.")
        else:
            print("Error: Invalid input format.")
            print("Please use the format: name/price/category")
            print("Example: lunch/100/food")

    def show_entries(self):
        print(json.dumps(self.data_list, indent=4))
    def calculate_totals(self):
        from collections import defaultdict

        total = 0
        cate_dict = defaultdict(int)

        for d in self.data_list:
            total += d['p']
            cate_dict[d['t']] += d['p']

        return total, dict(cate_dict)

def main():
    tracker = Tracker()
    print("Welcome to System v0.1 Build 2026")
    
    while True:
        cmd = input("> ")
        
        if cmd == "exit":
            tracker.save()
            total, cate_dict = tracker.calculate_totals()
            print("Total Spend: " + str(total))
            print("Categories: " + str(cate_dict))
            break
            
        elif cmd.startswith("add "):
            raw_data = cmd[4:]
            tracker.add_entry(raw_data)
        
        elif cmd == "show":
            tracker.show_entries()
            
        elif cmd == "reset_data":
            confirmation = input("Are you sure you want to reset all data? This action cannot be undone. (yes/no): ")
            if confirmation.lower() == "yes":
                tracker.data_list.clear()
                if os.path.exists(FILENAME):
                    os.remove(FILENAME)
                print("All data has been reset.")
            else:
                print("Reset operation canceled.")

if __name__ == "__main__":
    main()