class Band:

    all = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        self.__class__.all.append(self)

    def __repr__(self):
        return f'{self.name} - {self.members}'

    def get_members_names(self):
        members_names = ''
        for member in self.members:
            members_names += member.name + ' '
        return members_names

    def __str__(self):
        return f'The band is named {self.name}, the members are {self.get_members_names()}'

    def play_solos(self):
        solos = ''
        for member in self.members:
            solos += member.play_solo()
        return solos

    @classmethod
    def to_list(cls):
        list = ''
        for each in cls.all:
            list += each.__str__()

        return list

    @staticmethod
    def create_from_data(data):

        lines = data.split('\n')
        name = lines[0]
        members = []

        for i in range(1, len(lines)):
            members_list = lines[i].split(' on ')
            print(members_list)

            if members_list[1] == 'Guitar':
                members.append(Guitarist(members_list[0]))
            elif members_list[1] == 'Bass':
                members.append(Bassist(members_list[0]))
            elif members_list[1] == 'Drum':
                members.append(Drummer(members_list[0]))
        return Band(name, members)

class Musician:

    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __repr__(self):
        return f'{self.name} - {self.instrument} - {self.solo}'

    def __str__(self):
        return f'The musician is named {self.name} plays {self.instrument} and {self.solo}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return f'{self.name} plays {self.solo}. '


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name, 'guitar', 'guitar solo')

class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name, 'bass', 'bass solo')

class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name, 'drum', 'drum solo')
