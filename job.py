# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# YOUR NAME

class Job:

    def __init__(self, value = None, data = None):
        self.priority = value
        self.message = data

    def __eq__(self, job):
        if self.priority == job.priority:
             return True
        else:
             return False

