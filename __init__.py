from mycroft import MycroftSkill, intent_file_handler


class ExamplePrompts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('prompts.example.intent')
    def handle_prompts_example(self, message):
        self.speak_dialog('prompts.example')


def create_skill():
    return ExamplePrompts()

