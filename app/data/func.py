import os
f_path = "storage.txt"
scedule = {
    "Понеділок" : ["Математика", "Хімія"],
    "Вівторок" : [],
    "Середа" : [],
    "Четвер" : [],
    "П'ятниця" : []
}



def open_storage(message:str, f_path) :
    if f_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        f_path = os.path.join(base_path, "storage2.txt")


    with open(f_path, "w", encoding="UTF-8") as f:
        f.write(message)


def test_name(f_path, **scedule):
    if f_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        f_path = os.path.join(base_path, "storage.txt")
    with open(f_path, "w", encoding="UTF-8") as f1:
        for day, subjects in scedule.items():
            f1.write(f"{day}: {', '.join(subjects)}\n")


def update_scedule(f_path, day ,**scedule):
    if f_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        f_path = os.path.join(base_path, "storage2.txt")
    with open(f_path, "r") as f:
        data = f.read()
    scedule.update([day, data])




def download_scedule(f_path: str = None):
    if f_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        f_path = os.path.join(base_path, "storage.txt")

    scedule = {}
    with open(f_path, "r", encoding="UTF-8") as file:
        for line in file:
            day, subjects = line.strip().split(": ")
            scedule[day] = subjects.split(", ")
    return scedule