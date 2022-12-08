from diaries.AbstractDiary import AbstractDiary

class SudaDiary(AbstractDiary):
    def get_date(self):
        return "2021-11-25"

    def get_summary(self):
        return "紅葉ライトアップを見に行きました。めっちゃ綺麗でした。"
    
    def get_author(self):
        return "Suda"