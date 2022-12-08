from diaries.DiarySample import DiarySample
from diaries.TakabayashiDiary import TakabayashiDiary

diaries = [
    DiarySample(),
    TakabayashiDiary(),
    ]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()