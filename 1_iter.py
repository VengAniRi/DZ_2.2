import json

class CountryIter:
    def __init__(self):
        with open('countries.json', 'r', encoding='utf-8') as f:
            obj_list = json.load(f)
        self.contries_list = []
        for obj in obj_list:
            self.contries_list.append(obj['name']['common'])
        # альтернативный вариант создания заполненного списка
        # self.contries_list = [obj['name']['common'] for obj in obj_list]
        self.counter = 0
        self.limit = len(self.contries_list)
        self.fname = 'output.txt'
        f = open(self.fname, 'w', encoding='utf-8')
        f.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            name = self.contries_list[self.counter]
            url = "https://wikipedia.org/wiki/" + name
            with open(self.fname, 'a', encoding='utf-8') as f:
                f.write(f'{name} - {url}\n')
            self.counter += 1
            return name, url
        else:
            raise StopIteration

iterator = CountryIter()

for el in iterator:
    print(el)
