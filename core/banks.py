import cPickle


class Preset:
    def __init__(self, l1=False, l2=False, l3=False, l4=False, kd=False):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.kd = kd


class Bank:
    def __init__(self, name, pa, pb, pc):
        if name:
            if len(name) > 9:
                raise Exception('Bank name cannot be longer than 9 characters')
            self.name = name.upper()
        self.pa = pa
        self.pb = pb
        self.pc = pc


class BankRepository:
    def __init__(self, bank_file):
        self.bank_file = bank_file
        try:
            self._load()
        except:  # maybe too harsh?
            self.banks = self._get_empty_banks()
            self._dump()

    def get_all(self):
        self._load()
        return self.banks

    def get(self, bank_id):
        self._load()
        return self.banks[bank_id]

    def update(self, bank_id, bank):
        self.banks[bank_id] = bank
        self._dump()

    def _get_empty_banks(self):
        banks = {}
        for i in range(1, 100):
            banks[i] = (Bank(None,
                             Preset(False, False, False, False, False),
                             Preset(False, False, False, False, False),
                             Preset(False, False, False, False, False)))
        return banks

    def _dump(self):
        with open(self.bank_file, 'wb') as f:
            cPickle.dump(self.banks, f, 2)

    def _load(self):
        with open(self.bank_file, 'rb') as f:
            self.banks = cPickle.load(f)
