import abc


class IState(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('The abstract methods are not implemented everywhere...')

    @abc.abstractmethod
    def onStateEnter(self, entity):
        pass

    @abc.abstractmethod
    def onStateExecution(self, entity):
        pass

    @abc.abstractmethod
    def onStateExit(self, entity):
        pass
