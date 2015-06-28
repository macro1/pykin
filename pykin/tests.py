import unittest
import transaction

from pyramid import testing

from . import models


# class TestMyViewSuccessCondition(unittest.TestCase):
#
#     def setUp(self):
#         self.config = testing.setUp()
#         from sqlalchemy import create_engine
#         engine = create_engine('sqlite://')
#         models.DBSession.configure(bind=engine)
#         models.Base.metadata.create_all(engine)
#         with transaction.manager:
#             model = models.MyModel(name='one', value=55)
#             models.DBSession.add(model)
#
#     def tearDown(self):
#         models.DBSession.remove()
#         testing.tearDown()
#
#     def test_passing_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['one'].name, 'one')
#         self.assertEqual(info['project'], 'pykin')
#
#
# class TestMyViewFailureCondition(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#         from sqlalchemy import create_engine
#         engine = create_engine('sqlite://')
#         models.DBSession.configure(bind=engine)
#
#     def tearDown(self):
#         models.DBSession.remove()
#         testing.tearDown()
#
#     def test_failing_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info.status_int, 500)
