from abc import ABC, abstractmethod


class IDataInput(ABC):
    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def validate_user_input(self, input):
        pass

    @abstractmethod
    def create_p_listrik(self):
        pass
