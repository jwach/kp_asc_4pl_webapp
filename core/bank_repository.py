class Preset:
    def __init__(self, l1, l2, l3, l4, kd):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.kd = kd


class Bank:
    def __init__(self, bank_id, p1, p2, p3):
        self.bank_id = bank_id
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


class BankRepository:
    def __init__(self, banks=None):
        if banks is None:
            self.banks = self._get_empty_banks()
        else:
            self.banks = banks

    def _get_empty_banks(self):
        for i in range(1, 99):
            self.banks.append(Bank(i,
                                   Preset(False, False, False, False, False),
                                   Preset(False, False, False, False, False),
                                   Preset(False, False, False, False, False)))
        return self.banks

    def get(self):
        return self.banks
