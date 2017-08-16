'''
Created on 04.06.2013

@author: kca
'''

# import openmtc.model.test
# from openmtc_etsi.exc import SCLNotFound

# class MapperCollectionTestCase(openmtc.model.test.ModelCollectionTestCase):
#     def setUp(self):
#         from openmtc.model import Application
#         from openmtc.mapper import Mapper
#         self.mapper = Mapper("http://localhost:5000")
#         self.sclBase = self.mapper.get("/m2m")
#         self.app = Application(appId = "MyApp")
#         self.app2 = Application(appId = "MyApp2")
#
#     def tearDown(self):
#         from openmtc_etsi.client.http import XIXClient
#         try:
#             XIXClient("http://localhost:5000").delete("/m2m/applications/MyApp")
#         except SCLNotFound:
#             pass
#
#     #def test_mapper(self):
#     #    self.assertTrue(hasattr(self.sclBase, "_changes"))
#
#     def test_mapper_parent(self):
#         self.assertEqual(self.sclBase, self.sclBase.applications.parent)
#
#     """
#     def test_mapper_append_internals(self):
#         self.sclBase.applications.applicationCollection.append(self.app)
#         self.assertIn(self.app, self.sclBase.applications.applicationCollection._changes.added)
#         self.assertTrue("applicationCollection" in self.sclBase.applications._changes.collection_changes, str(self.sclBase.applications._changes))
#         self.assertTrue("applications" in self.sclBase._changes.subresource_changes, str(self.sclBase._changes))
#
#     def test_mapper_retrieve_append_update(self):
#         self.sclBase.applications.applicationCollection.append(self.app)
#         self.mapper.update(self.sclBase)
#         self.assertIsNotNone(self.app.path)
#         self.assertTrue(self.app.path.startswith(self.sclBase.applications.path), self.app.path)
#
#     def test_mapper_retrieveSclBase_appendApp_updateSclBase_appendContainer_updateApp(self):
#         from openmtc.model import Container
#
#         self.sclBase.applications.applicationCollection.append(self.app)
#         self.mapper.update(self.sclBase)
#
#         container = Container(id = "MyContainer")
#
#         self.app.containers.containerCollection.append(container)
#
#         self.mapper.update(self.app)
#         self.assertIsNotNone(container.path)
#         self.assertTrue(container.path.startswith(self.app.containers.path), self.app.path)
#
#     def test_mapper_retrieveSclBase_appendApp_updateSclBase_appendContainer_internals(self):
#         from openmtc.model import Container
#
#         self.sclBase.applications.applicationCollection.append(self.app)
#         self.mapper.update(self.sclBase)
#
#         container = Container(id = "MyContainer")
#
#         self.app.containers.containerCollection.append(container)
#
#         self.assertIn("containerCollection", self.app.containers._changes.collection_changes, str(self.app.containers._changes))
#         self.assertIn("containers", self.app._changes.subresource_changes, str(self.app._changes))
#
#     def test_mapper_retrieveSclBase_appendApp_updateSclBase_appendContainer_updateSclBase(self):
#         from openmtc.model import Container
#
#         self.sclBase.applications.applicationCollection.append(self.app)
#         self.mapper.update(self.sclBase)
#
#         container = Container(id = "MyContainer")
#
#         self.app.containers.containerCollection.append(container)
#
#         self.mapper.update(self.sclBase)
#         self.assertIsNotNone(container.path)
#         self.assertTrue(container.path.startswith(self.app.containers.path), self.app.path)
#     """
#
#
#
#
# if __name__ == '__main__':
#     import unittest
#     unittest.main()
        