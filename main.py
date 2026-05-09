class LogMixin:
    def log(self, msg):
        print(f"  [{self.__class__.__name__}] {msg}")

class SerializeMixin:
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith("_")}
    def to_json(self):
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False)

class ValidateMixin:
    def validate(self):
        for k, v in self.__dict__.items():
            if v is None:
                raise ValueError(f"'{k}' None bo'lishi mumkin emas!")
        return True

class User(LogMixin, SerializeMixin, ValidateMixin):
    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    def save(self):
        self.validate()
        self.log(f"Saqlandi: {self.name}")

if __name__ == "__main__":
    u = User("Ali", "ali@mail.com", 21)
    u.save()
    print(u.to_dict())
    print(u.to_json())

    try:
        u2 = User("Vali", None, 22)
        u2.validate()
    except ValueError as e:
        print(f"  Xato: {e}")
