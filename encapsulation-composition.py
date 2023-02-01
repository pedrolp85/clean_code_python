class BankAccount:
    TOTAL_BANK_ACCOUNTS = 0

    def __init__(self):
        BankAccount.TOTAL_BANK_ACCOUNTS += 1
        self.count_id = BankAccount.TOTAL_BANK_ACCOUNTS


# Encapsulation vs Composition -> The same think
# Encapsulation vs Inherence ->


class WriteFile:
    def write_file(self, data):
        data_to_write = self._format(data)
        file.write(data_to_write)

    @abstractmethod
    def _format(data):
        pass


class WriteFileJSON(WriteFile):
    def _format(data):
        return json.dumps(data)


class WriteFileYAML(WriteFile):
    def _format(data):
        return yaml.dumps(data)


class LoadAndSave:
    writer: WriteFile

    def __init__(self, writer: WriteFile = WriteFileYAML()):
        self.writer = writer

    def load_save(self):
        data = requests.get("https://google.com")
        self.writer.write_file(data)
