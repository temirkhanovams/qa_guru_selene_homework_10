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


@dataclasses.dataclass
class ResultUser:
    full_name: str
    email: str
    gender: str
    phone: str
    birthday: str
    subjects: str
    hobbies: str
    file: str
    address: str
    state_city: str


admin = User(
    first_name='admin',
    last_name='admin',
    email='blabla@bla.bla',
    gender='Female',
    phone='9999999999',
    year='1992',
    month='December',
    day='1',
    subjects='Maths',
    hobbies='Reading',
    file='img.jpg',
    address='Moscow Leninskiy av. 120',
    state='NCR',
    city='Delhi'
)

admin_result = ResultUser(
    full_name='admin admin',
    email='blabla@bla.bla',
    gender='Female',
    phone='9999999999',
    birthday='01 December,1992',
    subjects='Maths',
    hobbies='Reading',
    file='img.jpg',
    address='Moscow Leninskiy av. 120',
    state_city='NCR Delhi'
)

simple_user = User(
    first_name="Марина",
    last_name="Темирханова",
    email='blabla@bla.bla',
    gender='Female',
    phone='9999999999',
    year='1992',
    month='December',
    day='1',
    subjects='Maths',
    hobbies='Reading',
    file='img.jpg',
    address='Moscow Leninskiy av. 120',
    state='NCR',
    city='Delhi'
)

simple_user_result = ResultUser(
    full_name='Марина Темирханова',
    email='blabla@bla.bla',
    gender='Female',
    phone='9999999999',
    birthday='01 December,1992',
    subjects='Maths',
    hobbies='Reading',
    file='img.jpg',
    address='Moscow Leninskiy av. 120',
    state_city='NCR Delhi'
)
