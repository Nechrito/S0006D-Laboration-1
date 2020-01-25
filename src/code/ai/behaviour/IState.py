import abc

from src.code.engine.Entity import Entity


class IState(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __repr__(self):
        pass

    @abc.abstractmethod
    def onStateEnter(self, entity: Entity):
        pass

    @abc.abstractmethod
    def onStateExecution(self, entity: Entity):
        pass

    @abc.abstractmethod
    def onStateExit(self, entity: Entity):
        pass


