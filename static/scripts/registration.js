// Toggle between Login and Register
const authTitle = document.getElementById('auth-title');
const authBtn = document.getElementById('auth-btn');
const toggleAuth = document.getElementById('toggle-auth');
let isLogin = true; // Tracks if it's login or registration

toggleAuth.addEventListener('click', () => {
    isLogin = !isLogin;
    if (isLogin) {
        authTitle.textContent = 'Login';
        authBtn.textContent = 'Login';
        toggleAuth.textContent = "Don't have an account? Register here";
    } else {
        authTitle.textContent = 'Register';
        authBtn.textContent = 'Register';
        toggleAuth.textContent = 'Already have an account? Login here';
    }
});

// Handle form submission
const authForm = document.getElementById('auth-form');
authForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (isLogin) {
        // Handle login
        const storedUsername = localStorage.getItem('username');
        const storedPassword = localStorage.getItem('password');
        if (username === storedUsername && password === storedPassword) {
            alert('Login successful!');
            window.location.href = 'dashboard.html'; // Redirect to the dashboard
        } else {
            alert('Invalid username or password.');
        }
    } else {
        // Handle registration
        localStorage.setItem('username', username);
        localStorage.setItem('password', password);
        alert('Registration successful! You can now login.');
        isLogin = true;
        authTitle.textContent = 'Login';
        authBtn.textContent = 'Login';
        toggleAuth.textContent = "Don't have an account? Register here";
    }
});