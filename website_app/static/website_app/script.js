document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("darkModeToggle");
    const body = document.body;

    // Kullanıcının tercihini localStorage'dan al
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Açık Mod";
    }

    toggleButton.addEventListener("click", function() {
        body.classList.toggle("dark-mode");

        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            toggleButton.textContent = "☀️ Açık Mod";
        } else {
            localStorage.setItem("darkMode", "disabled");
            toggleButton.textContent = "🌙 Karanlık Mod";
        }
    });
});
