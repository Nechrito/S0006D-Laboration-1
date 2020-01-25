from src.code.engine.Game import Game

# Only executes the main method if this module is executed as the main script
if __name__ == "__main__":

    instance = Game()
    instance.load()

    while True:
        instance.update()
        instance.draw()
