from diaries.AbstractDiary import AbstractDiary

class RenDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-07"

    def get_summary(self):
        return "バイト"
    
    def get_author(self):
        return "Ren"