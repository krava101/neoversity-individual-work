from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value  

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if value is None or not value.strip():
            raise ValueError("Name є обов'язковим!")
        super().__init__(value.strip())
    ...

class Phone(Field):
    def __init__(self, value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone повинен складатись з 10 цифр!")
        super().__init__(value)
    ...

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        phone_field = Phone(phone)
        for p in self.phones:
            if p.value == phone_field.value:
                self.phones.remove(p)
                return
        raise ValueError(f'Номер "{phone}" не знайдено!')
    
    def find_phone(self, phone: str):
        phone_field = Phone(phone)
        for p in self.phones:
            if p.value == phone_field.value:
                return p
        return None
    
    def edit_phone(self, old_phone: str, new_phone: str):
        phone_field = Phone(old_phone)
        new_phone_field = Phone(new_phone)
        for i, p in enumerate(self.phones):
            if p.value == phone_field.value:
                self.phones[i] = new_phone_field
                return
        raise ValueError(f'Номер "{old_phone}" не знайдено!')
                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name is None or not name.strip():
            raise ValueError("Введіть ім'я!")
        return self.data.get(name.strip())
    
    def delete(self, name: str):
        if name is None or not name.strip():
            raise ValueError("Введіть ім'я!")
        return self.data.pop(name.strip(), None)

    ...

# Міні перевірка
if __name__ == "__main__":
        # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")