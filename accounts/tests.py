from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from .forms import SignUp

class ProfileModelTest(TestCase):
    
    def setUp(self):
        # Create a User instance for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_profile_creation(self):
        """Test that the Profile is created correctly."""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.rank, 0)  # Default value
        self.assertEqual(self.profile.quiz_count, 0)  # Default value
        self.assertEqual(self.profile.badge, 0)  # Default value

    def test_profile_str(self):
        """Test the string representation of the Profile."""
        self.assertEqual(str(self.profile), "testuser's Profile")

    def test_profile_fields(self):
        """Test that Profile fields can be updated."""
        self.profile.rank = 1
        self.profile.quiz_count = 5
        self.profile.badge = 2
        self.profile.save()

        self.profile.refresh_from_db()  # Refresh from the database
        self.assertEqual(self.profile.rank, 1)
        self.assertEqual(self.profile.quiz_count, 5)
        self.assertEqual(self.profile.badge, 2)

    def test_user_profile_relationship(self):
        """Test that a user can have only one profile."""
        with self.assertRaises(Exception):
            Profile.objects.create(user=self.user)  # Should raise an error



class SignUpFormTest(TestCase):
    
    def test_form_valid_with_matching_passwords(self):
        """Test the form is valid with matching passwords."""
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'password123',
            'confirm_password': 'password123',
        }
        form = SignUp(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_with_non_matching_passwords(self):
        """Test the form is invalid with non-matching passwords."""
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'password123',
            'confirm_password': 'differentpassword',
        }
        form = SignUp(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('confirm_password', form.errors)  # Check for specific error field
        self.assertEqual(form.errors['confirm_password'], ["Passwords do not match"])

    def test_form_invalid_without_required_fields(self):
        """Test the form is invalid without required fields."""
        form_data = {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'password': '',
            'confirm_password': '',
        }
        form = SignUp(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

    def test_form_creates_user(self):
        """Test that the form creates a User instance when valid."""
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'password123',
            'confirm_password': 'password123',
        }
        form = SignUp(data=form_data)
        if form.is_valid():
            user = form.save(commit=False)  # Do not save yet, just create a user instance
            user.set_password(form.cleaned_data['password'])  # Set password correctly
            user.save()
        
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(username='newuser').email, 'new@example.com')