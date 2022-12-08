from diaries.DiarySample import DiarySample
from diaries.TakabayashiDiary import TakabayashiDiary
from diaries.WakouDiary import WakouDiary
from diaries.MomokaDiary import MomokaDiary
from diaries.K21038Diary import K21038Diary
from diaries.RenDiary import RenDiary
from diaries.SudaDiary import SudaDiary

diaries = [
    DiarySample(),
    TakabayashiDiary(),
    MomokaDiary(),
    WakouDiary(),
    K21038Diary(),
    RenDiary(),
    SudaDiary(),
 ]

for d in diaries:
    print("--------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()