from django.test import TestCase
from .models import Subject
from .models import Course
from .models import Module
from .models import ItemBase

""" Tests for courses/models.py """

class SubjectModelTest(TestCase):
	""" Tests the Subject model. """
	
	def test_subject_title_is_returned(self):
		sbjtitle = Subject(title="ExampleTitle")
		self.assertEqual(sbjtitle.title, str(sbjtitle))

class CourseModelTest(TestCase):
	""" Tests the Course model. """
	
	def test_course_title_is_returned(self):
		crstitle = Course(title="ExampleTitle")
		self.assertEqual(crstitle.title, str(crstitle))

class ModuleModelTest(TestCase):
	""" Tests the Module model. """
	def test_module_title_and_order_is_returned(self):
		modtitle = Module(order=0,title="ExampleTitle")
		self.assertEqual(f'{modtitle.order}. {modtitle.title}', str(modtitle))

class ItembaseModelTest(TestCase):
	""" Tests the ItemBase model. """
	def test_itembase_title_is_returned(self):
		itbtitle = ItemBase(title="ExampleTitle")
		self.assertEqual(itbtitle.title, str(itbtitle))
