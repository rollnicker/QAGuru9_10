import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


student = User(first_name='Kek',
               last_name='Cheburek',
               email='kekovich@mail.ru',
               gender="Other",
               mobile='8985123456',
               year_of_birth='1990',
               month_of_birth='January',
               day_of_birth="15",
               subjects='Maths',
               hobbies="Reading",
               picture='pepe.jpeg',
               address='omsk',
               state='NCR',
               city='Delhi')

man = User(first_name='Lol',
           last_name='Net',
           email='super@mail.ru',
           gender="Male",
           mobile='8985001020',
           year_of_birth='2003',
           month_of_birth='September',
           day_of_birth="20",
           subjects='English',
           hobbies="Music",
           picture='pepe.jpeg',
           address='Moscow City',
           state='Uttar Pradesh',
           city='Agra')
