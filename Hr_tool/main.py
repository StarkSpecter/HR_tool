"""

"""
from hr_tool_logic.candidate import Candidate
from hr_tool_logic.interview import Interview
from hr_tool_logic.interviewround import InterviewRound
from hr_tool_logic.interviewer import Interviewer
from DataStorage.data_storage import my_dict_no_id, my_dict
from Repository.candidate_repository import CandidateRepository
from Repository.interview_repository import InterviewRepository
from Repository.interviewround_repository import InterviewRoundRepository
from Repository.interviewer_repository import InterviewerRepository
from Repository.repository import Repository
from bson import ObjectId
import pprint as pp
# from DataStorage.data_storage import my_dict
from DataStorage.data_storage import DbDataStorage

from datetime import date, datetime


def cand_create():
    print("Введите имя (обязательное поле):")
    cand_name = input()
    cand = Candidate(cand_name)
    print("Введите роль кандидита ")
    cand.role = input()
    print("Введите количество лет опыта (от 0 до 50) ")
    cand.yoe = int(input())
    print("Введите емэйл кандидита ")
    cand.email = input()
    print("Введите номер телефона кандидита ")
    cand.phone_number = input()
    print("Введите LinkedIn кандидита ")
    cand.linkedin = input()
    print("Введите дату рождения кандидита в формате 'Год, месяц, число' ")
    ls = list(map(int, input().split()))
    cand.birthdate = date(ls[0], ls[1], ls[2])
    print("Введите 1 если кандидит в черном списке ")
    if input() == "1":
        cand.is_blacklisted = True
    print("Введите заметки о кандидате")
    cand.notes = input()
    print(cand._id)
    rep.candidate_rep.add_candidate(cand)


def cand_view():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    pp.pprint(rep.candidate_rep.get_candidate_by_id(input()))


def cand_remove():
    print("Введите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    print(rep.candidate_rep.remove_candidate(input()))


def cand_update():
    print("Введите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand = input()
    cand = ObjectId(cand)
    print("Введите поля которые хотите изменить:")
    print("Введите имя ")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__name": line}})
    print("Введите роль кандидита ")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__role": line}})
    print("Введите количество лет опыта (от 0 до 50) ")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__yoe": int(line)}})
    print("Введите емэйл кандидита ")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__email": line}})
    print("Введите номер телефона кандидита ")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__phone_number": line}})
    print("Введите LinkedIn кандидaта ")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__linkedin": line}})
    print("Введите дату рождения кандидита в формате 'Год, месяц, число' ")
    ls = list(map(int, input().split()))
    if ls:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__birthdate": date(ls[0], ls[1], ls[2])}})
    print("Введите 1 если кандидит в черном списке ")
    if input() == "1":
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__is_blacklisted": True}})
    print("Введите заметки о кандидате")
    line = input()
    if line:
        mydb.candidates.update_one({"_id": cand}, {"$set": {"_Candidate__notes": line}})


def interview_create():
    print("Введите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    interview = Interview(ObjectId(cand_id))
    print("Введите дату начала собесeдований в формате 'Год, месяц, число'")
    ls = list(map(int, input().split()))
    interview.start_time = date(ls[0], ls[1], ls[2])
    print("Выберите статус: 1 для 'Active', 0 для 'Archived'")
    if input() == "0":
        interview.status = "Archived"
    print(interview._id)
    print(interview.__dict__)
    rep.interview_repository.add_interview(interview)


def interview_update():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    interview = ObjectId(input())
    print("Введите дату начала собесодований в формате 'Год, месяц, число'")
    ls = list(map(int, input().split()))
    if ls:
        mydb.interviews.update_one({"_id": interview}, {"$set": {"_Interview__notes": date(ls[0], ls[1], ls[2])}})
    print("Выберите статус: 1 для 'Active', 0 для 'Archived'")
    aboba = input()
    if aboba == "0":
        mydb.interviews.update_one({"_id": interview}, {"$set": {"_Interview__status": "archieved"}})
    elif aboba == "1":
        mydb.interviews.update_one({"_id": interview}, {"$set": {"_Interview__status": "Active"}})


def interview_remove():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    rep.interview_repository.remove_interview(input())


def interview_view():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    pp.pprint(rep.interview_repository.get_interview_by_id(input()))


def interviews_view_for_cand():
    print("Введите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    views = rep.interview_repository.get_interviews_for_candidate(input())
    for view in views:
        pp.pprint(view)


def interview_get_mark():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    rep.interview_repository.get_mark(input())


def round_create():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    iround = InterviewRound(ObjectId(input()))
    print("Введите время проведения раунда в формате 'Год, месяц, число, часы, минуты' ")
    ls = list(map(int, input().split()))
    if ls:
        iround.datetime = datetime(ls[0], ls[1], ls[2], ls[3], ls[4])
    print("Введите тип раунда")
    iround.round_type = input()
    print("Введите формат раунда")
    iround.round_format = input()
    print("Выберите статус раунда: 1 для 'upcoming', 0 для 'ended'")
    if input == "0":
        iround.status = 'ended'
    print("Введите оценку за раунд")
    iround.mark = int(input())
    rep.interviewround_repository.add_round(iround)


def round_view():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    interview_id = input()
    print("Введите _id раунда")
    for round in rep.interviewround_repository.get_rounds_for_interview(interview_id):
        print(round["_id"], end=" ")
        print(round["_InterviewRound__datetime"], end= " ")
        print(round["_InterviewRound__round_type"])
    pp.pprint(rep.interviewround_repository.get_round_by_id(input()))


def round_update():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    interview_id = input()
    print("Введите _id раунда")
    for round in rep.interviewround_repository.get_rounds_for_interview(interview_id):
        print(round["_id"], end=" ")
        print(round["_InterviewRound__datetime"], end=" ")
        print(round["_InterviewRound__round_type"])
    iround = ObjectId(input())
    print("Введите поля которые хотите изменить:")
    print("Введите время проведения ")
    ls = list(map(int, input().split()))
    if ls:
        mydb.interview_rounds.update_one({"_id": iround}, {"$set": {"_InterviewRound__datetime": datetime(ls[0], ls[1], ls[2], ls[4], ls[5])}})
    print("Введите тип раунда")
    line = input()
    if line:
        mydb.interview_rounds.update_one({"_id": iround}, {"$set": {"_InterviewRound__round_type": line}})
    print("Введите формат раунда")
    line = input()
    if line:
        mydb.interview_rounds.update_one({"_id": iround}, {"$set": {"_InterviewRound__round_format": line}})
    print("Выберите статус раунда: 1 для 'upcoming', 0 для 'ended'")
    line = input()
    if line == "0":
        mydb.interview_rounds.update_one({"_id": iround}, {"$set": {"_InterviewRound__status": 'upcoming'}})
    if line == "1":
        mydb.interview_rounds.update_one({"_id": iround}, {"$set": {"_InterviewRound__status": 'ended'}})
    print("Введите оценку за раунд")
    line = input()
    if line:
        mydb.interview_rounds.update_one({"_id": iround}, {"$set": {"_InterviewRound__mark": int(line)}})


def round_remove():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    interview_id = input()
    print("Введите _id раунда")
    for round in rep.interviewround_repository.get_rounds_for_interview(interview_id):
        print(round["_id"], end=" ")
        print(round["_InterviewRound__datetime"], end=" ")
        print(round["_InterviewRound__round_type"])
    rep.interviewround_repository.remove_round(input())


def rounds_view():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    irounds = rep.interviewround_repository.get_rounds_for_interview(input())
    for iround in irounds:
        pp.pprint(iround)


def round_add_interviewer():
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    interview_id = input()
    print("Введите _id раунда")
    for round in rep.interviewround_repository.get_rounds_for_interview(interview_id):
        print(round["_id"], end=" ")
        print(round["_InterviewRound__datetime"], end=" ")
        print(round["_InterviewRound__round_type"])
    iround = input()
    wers = rep.interviewer_repository.get_all_interviewers()
    for wer in wers:
        print(wer["_id"], end=" ")
        print(wer["_Interviewer__name"], end = " ")
        print(wer["_Interviewer__title"])
    print("Введите _id интервьювера")
    wer = input()
    iround = rep.interviewround_repository.get_round_by_id(iround)
    list = iround["_Interviewer__interviewround_ids"]
    list.append(wer)
    mydb.interview_rounds.update_one({"_id": iround["_id"]}, {"$set": {"_Interviewer__interviewround_ids": list}})


def interviewer_create():
    print("Введите имя (обязательное поле)")
    name = input()
    interviewer = Interviewer(name)
    print("Введите емайл")
    interviewer.email = input()
    print("Введите должность")
    interviewer.title = input()
    rep.interviewer_repository.add_interviewer(interviewer)


def interviewer_view():
    wers = rep.interviewer_repository.get_all_interviewers()
    for wer in wers:
        print(wer["_id"], end=" ")
        print(wer["_Interviewer__name"])
    print("Введите _id интервьювера ")
    print(rep.interviewer_repository.get_interviewer(input()))


def interviewer_view_rounds():
    wers = rep.interviewer_repository.get_all_interviewers()
    for wer in wers:
        print(wer["_id"], end=" ")
        print(wer["_Interviewer__name"])
    print("Введите _id интервьювера ")
    print("Введите _id интервьювера ")
    _id = input()
    list = []
    for rid in rep.interviewer_repository.get_interviewer(_id).interviewround_ids:
        list.append(rep.interviewround_repository.find_one({"_id": rid}))
    for lis in list:
        pp.pprint(lis)


def interviewer_update():
    wers = rep.interviewer_repository.get_all_interviewers()
    for wer in wers:
        print(wer["_id"], end=" ")
        print(wer["_Interviewer__name"])
    print("Введите _id интервьювера ")
    interviewer = rep.interviewer_repository.get_interviewer(input())
    _id = interviewer["_id"]
    print("Введите поля которые хотите изменить:")
    print("Введите имя")
    line = input()
    if line:
        mydb.interviewers.update_one({"_id": _id}, {"$set": {"_Interviewer__name": line}})
    print("Введите емайл")
    line = input()
    if line:
        mydb.interviewers.update_one({"_id": _id}, {"$set": {"_Interviewer__email": line}})
    print("Введите должность")
    line = input()
    if line:
        mydb.interviewers.update_one({"_id": _id}, {"$set": {"_Interviewer__title": line}})


def interviewer_remove():
    wers = rep.interviewer_repository.get_all_interviewers()
    for wer in wers:
        print(wer["_id"], end=" ")
        print(wer["_Interviewer__name"])
    print("Введите _id интервьювера ")
    rep.interviewer_repository.remove_interviewer(input())


def interviewer_add_round():
    wers = rep.interviewer_repository.get_all_interviewers()
    for wer in wers:
        print(wer["_id"], end=" ")
        print(wer["_Interviewer__name"])
    print("Введите _id интервьювера")
    interviewer = rep.interviewer_repository.get_interviewer(input())
    list = interviewer["_Interviewer__interviewround_ids"]
    print("Выберите _id кандидата")
    for cand in rep.candidate_rep.get_all_candidates():
        print(cand["_id"], end=" ")
        print(cand["_Candidate__name"])
    cand_id = input()
    print("Введите _id интервью")
    for interview in rep.interview_repository.get_interviews_for_candidate(cand_id):
        print(interview["_id"], end=" ")
        print(interview["_Interview__status"])
    interview_id = input()
    print("Введите _id раунда")
    for round in rep.interviewround_repository.get_rounds_for_interview(interview_id):
        print(round["_id"], end=" ")
        print(round["_InterviewRound__datetime"], end=" ")
        print(round["_InterviewRound__round_type"])
    list.append(input())
    mydb.interviewers.update_one({"_id": interviewer["_id"]}, {"$set": {"_Interviewer__interviewround_ids" : list}} )


connection_type = "localhost"
connection_address = 27017

mydb = DbDataStorage(connection_type, connection_address)
rep = Repository(mydb, CandidateRepository, InterviewRepository, InterviewRoundRepository, InterviewerRepository)

while True:
    print("Введите номер объекта для взаимодействия")
    print("1: Кандидат")
    print("2: Интервью")
    print("3: Интервью раунд")
    print("4: Интервьювер")
    print("5: Выход")
    input1 = input()
    if input1 == "1":
        print("Введите номер операции:")
        print("1: Создание")
        print("2: Просмотр")
        print("3: Изменение")
        print("4: Удаление")
        print("5: Назад")
        input2 = input()
        if input2 == "1":
            cand_create()
        elif input2 == "2":
            cand_view()
        elif input2 == "3":
            cand_update()
        elif input2 == "4":
            cand_remove()
        elif input2 == "5":
            continue
        else:
            print("Что-то сломалось")
    if input1 == "2":
        print("Введите номер операции:")
        print("1: Создание")
        print("2: Просмотр интервью")
        print("3: Просмотр всех интервью у кандидата")
        print("4: Изменение")
        print("5: Удаление")
        print("6: Вычисление оценки")
        print("7: Назад")
        input2 = input()
        if input2 == "1":
            interview_create()
        elif input2 == "2":
            interview_view()
        elif input2 == "3":
            interviews_view_for_cand()
        elif input2 == "4":
            interview_update()
        elif input2 == "5":
            interview_remove()
        elif input2 == "6":
            interview_get_mark()
        elif input2 == "7":
            continue
        else:
            print("Что-то сломалось")
    if input1 == "3":
        print("Введите номер операции:")
        print("1: Создание")
        print("2: Просмотр раунда")
        print("3: Просмотр раундов для интервью")
        print("4: Изменение")
        print("5: Удаление")
        print("6: Добавить интервьювера")
        print("7: Назад")
        input2 = input()
        if input2 == "1":
            round_create()
        elif input2 == "2":
            round_view()
        elif input2 == "3":
            rounds_view()
        elif input2 == "4":
            round_update()
        elif input2 == "5":
            round_remove()
        elif input2 == "6":
            round_add_interviewer()
        elif input2 == "7":
            continue
        else:
            print("Что-то сломалось")
    if input1 == "4":
        print("Введите номер операции:")
        print("1: Создание")
        print("2: Просмотр интервьювера")
        print("3: Просмотр раундов у этого интервьювера")
        print("4: Изменение")
        print("5: Удаление")
        print("6: Добавить раунд")
        print("7: Назад")
        input2 = input()
        if input2 == "1":
            interviewer_create()
        elif input2 == "2":
            interviewer_view()
        elif input2 == "3":
            interviewer_view_rounds()
        elif input2 == "4":
            interviewer_update()
        elif input2 == "5":
            interviewer_remove()
        elif input2 == "6":
            interviewer_add_round()
        elif input2 == "7":
            continue
        else:
            print("Что-то сломалось")
    if input1 == "5":
        break
        exit()

# # # ya = Candidate("Elisabeth", role="Poet", yoe = 20, phone_number="12124567890", birthdate=date(1985, 6, 21), notes = "<3 <3 <3")
# # #
# # #
# # # myrep = Repository(mydb, CandidateRepository, InterviewRepository, InterviewRoundRepository, InterviewerRepository)
# # # mydb.add_candidate(ya)
# # # cands = mydb.get_all_candidates()
# # # print(cands)
# # #
# # #
# # # interview = Interview(ya._id, decision="Hire", status="archived")
# # # mydb.add_interview(interview)
# # #
# # #
# # # iround = InterviewRound(interview._id, round_type="creative", round_format="offline", mark=100, status="Ended")
# # #
# # # mydb.add_round(iround)
# #
#



















# ya = Candidate("Sah")
# print(ya, end=" ")
# pp.pprint(ya.__dict__)
# pp.pprint(my_dict(ya))
# print(my_dict(ya)["_id"] == ya._id)
# print()
# interview = Interview(ya._id)
# print(interview, end=" ")
# pp.pprint(interview.__dict__)
# pp.pprint(my_dict(interview))
# print()
# iround = InterviewRound(interview._id)
# print(iround, end=" ")
# pp.pprint(iround.__dict__)
# pp.pprint(my_dict(iround))
# print()
# interviewer = Interviewer("Specter")
# print(interviewer, end=" ")
# pp.pprint(interviewer.__dict__)
# pp.pprint(my_dict(interviewer))
