import abc

from src.code.ai.Character import Character


class IState(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def onStateEnter(self, entity: Character):
        pass

    @abc.abstractmethod
    def onStateExecution(self, entity: Character):
        pass

    @abc.abstractmethod
    def onStateExit(self, entity: Character):
        pass
