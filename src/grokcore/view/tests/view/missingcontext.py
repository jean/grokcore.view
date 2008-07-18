"""
Views without a context cannot be grokked:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: No module-level context for
  <class 'grokcore.view.tests.view.missingcontext.Club'>, please use the
  'context' directive.

"""
from grokcore.view.tests import grok


class Club(grok.View):
    pass
