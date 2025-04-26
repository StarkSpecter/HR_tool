"""

"""
import pprint

from pymongo import MongoClient
from bson import ObjectId


def my_dict(o):
    default = o.__dict__
    final = dict()
    for key, value in default.items():
        if key == "_Candidate___id" or key == "_Interview___id" or key == "_InterviewRound___id" or key == "_Interviewer___id":
            final["_id"] = value
        elif key == "_Candidate__birthdate" or key == "_Interview__end_time" or key == "_Interview__start_time" \
                or key == "_InterviewRound__datetime":
            final[key] = str(value)
        else:
            final[key] = value

    return final


def my_dict_no_id(o):
    default = o.__dict__
    final = dict()
    for key, value in default.items():
        if key == "_Candidate___id" or key == "_Interview___id" or key == "_InterviewRound___id" or key == "_Interviewer___id":
            pass
        elif key == "_Candidate__birthdate" or key == "_Interview__end_time" or key == "_Interview__start_time" \
                or key == "_InterviewRound__datetime":
            final[key] = str(value)
        else:
            final[key] = value
    return final


class DbDataStorage:

    def __init__(self, connection_type, connection_address):
        self.client = MongoClient(connection_type, connection_address)
        self.db = self.client.hr_database
        self.candidates = self.db.candidates
        self.interviews = self.db.interviews
        self.interview_rounds = self.db.interview_rounds
        self.interviewers = self.db.interviewers

    def get_candidate_by_id(self, _id):
        _id = ObjectId(_id)
        return self.candidates.find_one({"_id": _id})

    def get_all_candidates(self):
        return self.candidates.find()

    def add_candidate(self, candidate):
        self.candidates.insert_one(my_dict(candidate))

    def update_candidate(self, candidate):
        cand_id = candidate._id
        self.candidates.update_one({"_id": cand_id}, {"$set": my_dict_no_id(candidate)})

    def remove_candidate(self, _id):
        _id = ObjectId(_id)
        self.candidates.delete_one({"_id": _id})

    def get_interviews_for_candidate(self, cand_id):
        cand_id = ObjectId(cand_id)
        return self.interviews.find({"_Interview__candidate_id": cand_id})

    def get_interview_by_id(self, _id):
        _id = ObjectId(_id)
        return self.interviews.find_one({"_id": _id})

    def add_interview(self, interview):
        self.interviews.insert_one(my_dict(interview))

    def remove_interview(self, _id):
        _id = ObjectId(_id)
        self.interviews.delete_one({"_id": _id})

    def update_interview(self, interview):
        _id = interview._id
        self.interviews.update_one({"_id": _id}, {"$set": my_dict_no_id(interview)})

    def get_mark(self, _id):
        _id = ObjectId(_id)
        sum = 0
        rounds = self.interview_rounds.find({"_InterviewRound__interview_id": _id})
        for iround in rounds:
            sum += iround["_InterviewRound__mark"]
        mark = sum / len(rounds)
        self.interviews.update_one({"_id": _id}, {"$set": {"_Interview__mark": mark}})

    def get_rounds_for_interview(self, _id):
        _id = ObjectId(_id)
        return self.interview_rounds.find({"_InterviewRound__interview_id": _id})

    def get_round_by_id(self, _id):
        _id = ObjectId(_id)
        return self.interview_rounds.find_one({"_id": _id})

    def add_round(self, interview_round):
        self.interview_rounds.insert_one(my_dict(interview_round))

    def remove_round(self, _id):
        _id = ObjectId(_id)
        self.interview_rounds.delete_one({"_id": _id})

    def update_round(self, interviewround):
        round_id = interviewround._id
        self.interview_rounds.update_one({"_id": round_id}, {"$set": my_dict_no_id(interviewround)})

    def get_interviewer(self, _id):
        _id = ObjectId(_id)
        return self.interviewers.find_one({"_id": _id})

    def get_all_interviewers(self):
        return self.interviewers.find()

    def get_interviewers_for_round(self, round_id):
        round_id = ObjectId(round_id)
        return self.interviewers.find({"_Interviewer__interviewround_ids": round_id})

    def add_interviewer(self, interviewer):
        self.interviewers.insert_one(my_dict(interviewer))

    def remove_interviewer(self, _id):
        self.interviewers.delete_one({"_id": _id})

    def update_interviewer(self, interviewer):
        _id = interviewer._id
        self.interviewers.update_one({"_id": _id}, {"$set": my_dict_no_id(interviewer)})
