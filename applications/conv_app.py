"""
Copyright (c) 2019 Uber Technologies, Inc.

Licensed under the Uber Non-Commercial License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at the root directory of this project.

See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Alexandros Papangelis"

from plato.agent.component.nlu import nlu
from plato.agent.component.nlg import nlg
from plato.agent.component.user_simulator.user_simulator \
    import UserSimulator
from plato.controller import basic_controller

import sys

# Create your first conversational AI application with Plato.
# 1. Create the necessary custom classes
# 2. Write a new configuration file using these classes
# 3. Call the Basic controller!


class TempNLU(nlu):
    def __int__(self):
        super(TempNLU, self).__init__()

    def process_input(self, utterance, dialogue_state=None):
        pass


class TempNLG(nlg):
    def __int__(self):
        super(TempNLG, self).__init__()

    def generate_output(self, args=None):
        pass


class TempUS(UserSimulator):
    def __int__(self):
        super(TempUS, self).__init__()

    def receive_input(self, inpt):
        pass

    def respond(self):
        pass


if __name__ == '__main__':
    basic_controller.run(sys.argv[2])
