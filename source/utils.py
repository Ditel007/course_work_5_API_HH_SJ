from source.API import HeadHunterAPI, SuperJobAPI
from source.save_to_JSON import JSONSaver
from source.vacancies import Vacancies

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver()


def vacancy_data(choose_data, top_n, keyword) -> list:
    """
    :param choose_data:
    :param top_n:
    :param keyword:
    :return: Список для JSON в зависимости от выбранной базы
    """
    vac_data = []
    if 'headhunter' in choose_data and 'superjob' in choose_data:
        for v in hh.host_to_api(top_n, keyword):
            vac_data.append(v)
        for v in sj.host_to_api(top_n, keyword):
            vac_data.append(v)
    elif 'headhunter' == choose_data:
        for v in hh.host_to_api(top_n, keyword):
            vac_data.append(v)
    elif 'superjob' == choose_data:
        for v in sj.host_to_api(top_n, keyword):
            vac_data.append(v)
    else:
        raise FileNotFoundError('Такой базы не существует')

    return vac_data


def form_vac_class(choose_data, top_n, keyword) -> list:
    """
    :param choose_data:
    :param top_n:
    :param keyword:
    :return: Список объектов класса Vacancies
    """
    data = vacancy_data(choose_data, top_n, keyword)

    vacancies = [
        Vacancies(
            vid=v['id'],
            title=v['title'],
            payment=v['payment'],
            date=v['date'],
            description=v['description'],
            candidate=v['candidate'],
            url=v['url']
        )
        for v in data
    ]
    return vacancies
