from diaries.DiarySample import DiarySample
from diaries.WakouDiary import WakouDiary

diaries = [
    DiarySample(),
    WakouDiary(),
    ]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()