"""
 This module created to acheive the communication functionality over the
channels.
"""

class Future:
    """
       This is added to acheive the communication functionality(as a channel)
    To avoid the cal back hell, Exceptions needs to be wrapped in some place.
    This Futures acts as communication channel between the suspended and resumed
    action.
    """
    def __init__(self):
        self.callback = None

    def resolve(self):
        self.callback()
