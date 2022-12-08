from diaries.AbstractDiary import AbstractDiary

class MomokaDiary(AbstractDiary):
    def get_date(self):
        return "2023-2-3"

    def get_summary(self):
        return "たくさんの雪が降っていた。とても寒かった。"
    
    def get_author(self):
        return "ももか"