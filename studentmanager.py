from __future__ import annotations
from typing import List


class Student:
    STUDENT_LIST: List[Student] = []

    def __init__(self, name: str, surname: str):
        self.__id = Student.__get_next_id()
        self.name: str = name
        self.surname: str = surname
        self.__gradebook: dict = {}
        self.__gpa: float = 0
        self.__modality: str = "campus"
        Student.STUDENT_LIST.append(self)

    @staticmethod
    def __get_next_id() -> int:
        largest_id = 0
        for s in Student.STUDENT_LIST:
            if s.__id > largest_id:
                largest_id = s.__id
        return largest_id + 1

    @staticmethod
    def get_by_id(student_id: int) -> Student:
        for s in Student.STUDENT_LIST:
            if s.id == student_id:
                return s

    @property
    def id(self) -> int:
        return self.__id

    @property
    def gpa(self) -> float:
        return self.__gpa

    @property
    def gradebook(self) -> dict:
        return self.__gradebook

    @property
    def modality(self) -> str:
        return self.__modality

    @modality.setter
    def modality(self, value) -> None:
        if value == "campus" or value == "remote":
            self.__modality = value
        else:
            raise ValueError("Modality must be 'campus' or 'remote'")

    def __calculate_gpa(self) -> None:
        total_mark = 0
        for grade in self.__gradebook.values():
            total_mark += grade
        self.__gpa = total_mark / len(self.__gradebook)

    def add_grade(self, subject: str, mark: float) -> None:
        self.__gradebook[subject] = mark
        self.__calculate_gpa()

    def get_grade(self, subject: str) -> float:
        return self.__gradebook[subject]


class StudentTeacher(Student):
    def __init__(self, name: str, surname: str, teaching_area: str):
        super().__init__(name, surname)
        self.teaching_area: str = teaching_area

    def is_allowed_teaching(self) -> bool:
        return self.gpa >= 80
