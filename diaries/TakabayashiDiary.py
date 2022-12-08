from diaries.AbstractDiary import AbstractDiary

class TakabayashiDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-07"

    def get_summary(self):
        return "物理実験のレポートを書いた。"
    
    def get_author(self):
        return "たかばやし"