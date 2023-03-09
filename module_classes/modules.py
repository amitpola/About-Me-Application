from dataclasses import dataclass
from utils import utils

@dataclass
class Person():
    name : str
    unique_id : str
    passion : str
    contact_number : str
    about_description : str
    skills : list

class StartOperations:
    def execute(self):
        utils.welcome_message()
        option_selected = int(input())
        utils.perform_operation(option_selected)