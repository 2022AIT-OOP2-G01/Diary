from diaries.DiarySample import DiarySample
from diaries.K21038Diary import K21038Diary
diaries = [
    DiarySample(),
    K21038Diary(),
    ]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()