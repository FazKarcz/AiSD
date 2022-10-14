class Dom:
    color: str
    ile_okien: int

    def __init__(self, color: str,ile_okien: int) -> None:
        self.color = color
        self.ile_okien = ile_okien

    def jaki_kolor(self) -> str:
        return f'elewacja ma kolor: {self.color}'

    def more_okna(self,ilosc: int) -> None:
        self.ile_okien += ilosc


dom1 = Dom('Czarny',4)
dom2 = Dom('Nie czarny',5)

print(f'Dom nr1 ma {dom1.ile_okien} okien')
print(f'Dom nr2 ma {dom2.ile_okien} okien')
dom2.more_okna(4)
print(f'Dom nr1 ma {dom1.ile_okien} okien')
print(f'Dom nr2 ma {dom2.ile_okien} okien')

print(dom1.jaki_kolor())
print(dom2.jaki_kolor())
