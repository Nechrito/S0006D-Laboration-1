from ....engine.Entity import Entity
from ..IState import IState
from .Drink import Drink
from .Sleep import Sleep
from .CollectMoney import CollectMoney
from .Eat import Eat


class Global(IState):

    def __init__(self):
        self.currentState = None
        #self.cachedCondition = None

    def __repr__(self):
        pass

    def enter(self, entity: Entity):
        pass

    def execute(self, entity: Entity):

        # this is a failed test where I wanted to cache the condition, but is bad overall even if it would've worked
        #if self.cachedCondition is not None:
        #    if not self.cachedCondition.__closure__[0].cell_contents:
        #        return
        #    else:
        #        print("GLOBAL - true!")

        if entity.hunger >= 95 and not self.currentState == Eat:
            #self.cachedCondition = self.memoize(entity.hunger <= 5)
            self.currentState = Eat
            entity.change(Eat())

        elif entity.fatigue >= 95 and not self.currentState == Sleep:
            #self.cachedCondition = self.memoize(entity.fatigue <= 5)
            self.currentState = Sleep
            entity.change(Sleep())

        elif entity.thirst >= 95 and not self.currentState == Drink:
            #self.cachedCondition = self.memoize(entity.thirst <= 5)
            self.currentState = Drink
            entity.change(Drink())

        elif entity.bank <= 10 and not self.currentState == CollectMoney:
            #self.cachedCondition = self.memoize(entity.bank >= 30)
            self.currentState = CollectMoney
            entity.change(CollectMoney())

    def exit(self, entity: Entity):
        pass

    def memoize(self, func):
        self.cache = dict()

        def memoized_func(*args):
            if args in self.cache:
                return self.cache[args]

            result = func(*args)
            self.cache[args] = result
            return result

        return memoized_func
