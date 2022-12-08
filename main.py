from diaries.DiarySample import DiarySample
from diaries.SudaDiary import SudaDiary

diaries = [
    DiarySample(),
    SudaDiary(),
]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()