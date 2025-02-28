document.addEventListener('DOMContentLoaded', function() {
    // Get the dark mode toggle button
    const darkModeToggle = document.getElementById('darkModeToggle');
    
    // Check if user has a preference stored in localStorage
    const isDarkMode = localStorage.getItem('darkMode') === 'enabled';
    
    // Set initial dark mode status based on user preference
    if (isDarkMode) {
        enableDarkMode();
    } else {
        // Ensure light mode button style is set initially
        darkModeToggle.innerHTML = '🌙';
        darkModeToggle.classList.remove('btn-light');
        darkModeToggle.classList.add('btn-outline-dark');
    }
    
    // Toggle dark mode when button is clicked
    darkModeToggle.addEventListener('click', () => {
        // Check if dark mode is currently enabled
        const isDarkModeEnabled = document.body.classList.contains('dark-mode');
        
        if (isDarkModeEnabled) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });
    
    // Function to enable dark mode
    function enableDarkMode() {
        // Add dark mode class to body
        document.body.classList.add('dark-mode');
        
        // Change button text/icon
        darkModeToggle.innerHTML = '☀️';
        darkModeToggle.classList.remove('btn-outline-dark');
        darkModeToggle.classList.add('btn-outline-light');
        
        // Store user preference
        localStorage.setItem('darkMode', 'enabled');
    }
    
    // Function to disable dark mode
    function disableDarkMode() {
        // Remove dark mode class from body
        document.body.classList.remove('dark-mode');
        
        // Change button text/icon
        darkModeToggle.innerHTML = '🌙';
        darkModeToggle.classList.remove('btn-outline-light');
        darkModeToggle.classList.add('btn-outline-dark');
        
        // Store user preference
        localStorage.setItem('darkMode', 'disabled');
    }
});