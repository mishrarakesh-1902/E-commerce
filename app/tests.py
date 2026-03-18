from django.test import TestCase

# Create your tests here.

# Test guidelines
# Use TestCase for database-backed tests
# Use SimpleTestCase for tests that don't need DB

# Use setUp() for common test setup
# Use tearDown() for cleanup after tests

# Use assertRedirects() to test redirects
# Use assertContains() to check response content

# Run tests: python manage.py test
# Run specific: python manage.py test app.tests.TestClass

# Coverage: pip install coverage && coverage run manage.py test

# Use factory_boy for test data generation
# Use faker for generating fake data in tests

# Test views with Client: self.client.get('/') or self.client.post('/', data={})

# Test models: create instances and check field values
# Example: product = Product.objects.create(name='Test', price=100)
