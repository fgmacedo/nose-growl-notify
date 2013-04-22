#coding: utf-8

from nose.plugins import Plugin
import gntp.notifier
import os


def notify(icon, summary, body=""):
    image_name = os.path.join(os.path.dirname(__file__), '{0}.png'.format(icon))
    image = open(image_name, 'rb').read()
    gntp.notifier.mini(
        description=body,
        applicationName='nose-growl',
        title=summary,
        notificationIcon=image
    )


class NoseGrowlNotify (Plugin):

    NOTIFICATION_LIMIT = 5

    def __init__(self):
        super(NoseGrowlNotify, self).__init__()
        self.failed_tests = []

    def addError(self, test, err):
        self.record_failed_test(test, err)

    def addFailure(self, test, err):
        self.record_failed_test(test, err)

    def record_failed_test(self, test, err):
        self.failed_tests.append((test, err,))

    def finalize(self, result):
        if len(self.failed_tests) == 0:
            notify("dialog-ok", "All tests passed")
        else:
            for idx, info in enumerate(self.failed_tests):
                test, err = info
                message = err[1].message if hasattr(err[1], 'message') else err[1]
                notify("dialog-error", test.id(), message)
                if idx == self.NOTIFICATION_LIMIT:
                    notify("dialog-error", "Multiple tests failed")
                    break
