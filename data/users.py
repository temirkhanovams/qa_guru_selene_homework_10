import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    year: str
    month: str
    day: str
    subjects: str
    hobbies: str
    file: str
    address: str
    state: str
    city: str