from source.utils import form_vac_class, vacancy_data
from source.API import HeadHunterAPI, SuperJobAPI
from source.save_to_JSON import JSONSaver

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver()


def user_interface():
    choose_data = input("Введите платформу, с которой хотите получить вакансии (HeadHunter или SuperJob):\n").lower()
    top_n = int(input("Введите количество вакансий, которое хотите получить (от 1 до 100):\n"))
    keyword = input("Введите ключевое слово для поиска вакансий:\n")

    vac_data = vacancy_data(choose_data, top_n, keyword)
    show_data = form_vac_class(choose_data, top_n, keyword)

    js.form_json(vac_data)

    for v in show_data:
        print(v)


def get_one_vacancy():
    vid_show = int(input("Введите ID вакансии, чтобы показать её отдельно:\n"))
    print(js.get_vacancy(vid_show))


def del_vacancy():
    vid_del = int(input("Введите ID вакансии,чтобы удалить её из списка:\n"))
    js.delete_vacancy(vid_del)
    print("Вакансия удалена")


if __name__ == '__main__':
    user_interface()
    a = input("Если хотите удалить какую-то вакансию из списка введите - 1, если хотите рассмотреть отдельно вакансию "
              "из списка нажмите - 2\n")
    if a == 1:
        del_vacancy()
    elif a == 2:
        get_one_vacancy()
    else:
        print('Не понимаю вашу команду, до свидания!')
