class I18n:
    ja = None
    en = None
    cn = None

    def __init__(self, ja, en, cn):
        self.ja = ja
        self.en = en
        self.cn = cn

    @staticmethod
    def simple(data):
        return I18n(data, data, data)

    @staticmethod
    def complex(ja, en, cn):
        return I18n(ja, en, cn)

    def to_dict(self):
        return dict(
            ja=self.ja,
            en=self.en,
            cn=self.cn,
        )
