class Vacancies:

    def __init__(self, vid: int, title: str, payment: int, date, description: str, candidate: str, url):
        self.vid = vid
        self.title = title
        self.payment = payment
        self.date = date
        self.description = description
        self.candidate = candidate
        self.url = url

    def __str__(self):
        return f'{self.vid}\n'\
               f'{self.title}\n'\
               f'{self.payment}\n'\
               f'{self.description}\n'\
               f'{self.candidate}\n'\
               f'{self.url}\n' \
               f''f'------------------\n'

    def __gt__(self, other):
        if isinstance(self, other):
            return self.payment > other.payment