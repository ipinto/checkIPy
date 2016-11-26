class Messenger:

    def __init__(self):
        self._notifiers = []

    def add_notifier(self, notifier):
        if notifier not in self._notifiers:
            self._notifiers.append(notifier)

    def notify(self, message):
        for notifier in self._notifiers:
            notifier.notify(message)
