class Computer:
    def __init__(self, name, ram, processor):
        # self.name means "my name"
        # self.ram means "my ram"
        # self.processor means "my processor"
        self.name = name
        self.ram = ram
        self.processor = processor

    def info(self):
        # self tells Python to use THIS computer's name, ram, and processor
        return f"{self.name} computer with {self.ram}GB RAM and {self.processor} processor."


# Create two different computers
laptop = Computer("Dell Laptop", "4GB", "Intel i3")
desktop = Computer("HP Desktop", "8GB", "Intel i5")

# When we call info(), self helps Python know which computer's info to show
print(laptop.info())  # Uses laptop's name, ram, and processor
print(desktop.info())  # Uses desktop's name, ram, and processor