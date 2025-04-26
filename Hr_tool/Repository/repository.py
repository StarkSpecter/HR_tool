"""
This module defines a class for a repository
"""


class Repository:

    def __init__(self, data_storage, CandidateRepository, InterviewRepository, InterviewRoundRepository, InterviewerRepository):
        self.__data_storage = data_storage

        self.candidate_rep = CandidateRepository(self.__data_storage)

        self.interview_repository = InterviewRepository(self.__data_storage)

        self.interviewround_repository = InterviewRoundRepository(self.__data_storage)

        self.interviewer_repository = InterviewerRepository(self.__data_storage)
