#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = name
        self._job = job

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        approved_jobs = ["Teacher", "Engineer", "Doctor"]  # Example approved jobs
        if value in approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
