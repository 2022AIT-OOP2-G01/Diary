from diaries.DiarySample import DiarySample
from diaries.WakouDiary import WakouDiary
from diaries.MomokaDiary import MomokaDiary

diaries = [
    DiarySample(),
    MomokaDiary(),
    WakouDiary(),
    ]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()