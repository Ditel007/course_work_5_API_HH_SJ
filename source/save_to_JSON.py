import json


class JSONSaver:

    def __init__(self):
        self.__data = "data/vacancies.json"

    @property
    def data(self):
        return self.__data

    def form_json(self, vac_data):
        with open(self.data, 'w', encoding='utf8') as file:
            json.dump(vac_data, file, ensure_ascii=False, indent=4)

    def get_vacancies_list(self):
        try:
            with open(self.data, 'r', encoding='utf8') as file:
                vacancies_data = json.load(file)
        except:
            ValueError('Такой вакансии нет в файле')
        return vacancies_data

    def get_vacancy(self, vid):
        with open(self.data, 'r', encoding='utf8') as file:
            vacancies_data = json.load(file)
            try:
                for v in vacancies_data:
                    if v['id'] == vid:
                        return v
            except:
                ValueError('Вакансия не найдена')

    def delete_vacancy(self, vid):
        with open(self.data, 'r', encoding='utf8') as file:
            vacancies_data = json.load(file)
            try:
                for v in vacancies_data:
                    if v['id'] == vid:
                        vacancies_data.remove(v)
            except:
                ValueError('Такой вакансии уже нет в списке')
            with open(self.data, 'w', encoding='utf8') as file1:
                json.dump(vacancies_data, file1, ensure_ascii=False, indent=4)
