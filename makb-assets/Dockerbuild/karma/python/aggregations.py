class concat:
    def __init__(self, column_name, separator):
        self.result = ""
        self.separator = separator
        self.isFirst = True
        self.columnName = column_name

    def transform(self):
        return getValue(self.columnName)

    def accumulate(self, val):
        if self.isFirst:
            self.result += val
            self.isFirst = False
        else:
            self.result += self.separator + val

    def getResult(self):
        return self.result
