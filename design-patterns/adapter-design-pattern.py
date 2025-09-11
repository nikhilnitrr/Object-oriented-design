from abc import ABC, abstractmethod

class ILegacyPrinter(ABC):
    @abstractmethod
    def output():
        pass

class ILatestPrinter(ABC):
    @abstractmethod
    def result():
        pass

# We only have concrete legacy printer
class Printer(ILegacyPrinter):
    def output(self):
        return "Printing a page"

class PrinterAdapter(ILatestPrinter):
    def __init__(self, printer : ILegacyPrinter):
        super().__init__()
        self.printer = printer
    
    def result(self):
        return self.printer.output()
    
if __name__ == "__main__":
    adapter = PrinterAdapter(Printer())
    print(adapter.result())