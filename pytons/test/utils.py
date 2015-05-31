from setuptools.command import test

# prepare for monkey patching test command
# to make nose work with `setup.py test`
# see: http://goo.gl/kq9CBs
test._test = test.test


# Based on example at
# https://github.com/0compute/makeenv/blob/master/setup.py
class NoseTestCommand(test._test):

    user_options = test._test.user_options + [
        ("args=", "a", "Arguments to pass to nose"),
        ]

    def initialize_options(self):
        test._test.initialize_options(self)
        self.args = None

    def finalize_options(self):
        test._test.finalize_options(self)
        self.args = self.args and self.args.strip().split() or []
        self.test_suite = True

    def run_tests(self):
        try:
            import nose
        except ImportError:
            raise Exception("You've tried to run command without nose installed")
        nose.run_exit(argv=["nosetests"] + self.args)


def monkeypatch_setup_test():
    """Explicitely monkeypatches setup.py test command"""
    test.test = NoseTestCommand
