from diaries.DiarySample import DiarySample
from diaries.MomokaDiary import MomokaDiary

diaries = [
    DiarySample(),
    MomokaDiary(),
    ]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()