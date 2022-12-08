from diaries.AbstractDiary import AbstractDiary

class WakouDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-08"

    def get_summary(self):
        return "物理実験しんどい"
    
    def get_author(self):
        return "小川"