class XboxState:
    def __init__(self):
        pass

    def event(self, event, debugging):
        if debugging:
            print("Event:",event)
#event.type == pygame.JOYBUTTONDOWN:
#                        if debugging:
#                            print("Button Pressed:", event.button)
