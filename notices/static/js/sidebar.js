document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.querySelector(".sidebar");
    const toggle = sidebar ? sidebar.querySelector(".toggle") : null;
    const searchBtn = sidebar ? sidebar.querySelector(".search-box") : null;
    const modeSwitch = sidebar ? sidebar.querySelector(".toggle-switch") : null;
    const modeText = sidebar ? sidebar.querySelector(".mode-text") : null;

    if (toggle) {
        toggle.addEventListener("click", () => {
            sidebar.classList.toggle("close");
        });
    }

    if (searchBtn) {
        searchBtn.addEventListener("click", () => {
            sidebar.classList.remove("close");
        });
    }

    if (modeSwitch && modeText) {
        modeSwitch.addEventListener("click", () => {
            document.body.classList.toggle("dark");

            if (document.body.classList.contains("dark")) {
                modeText.innerText = "Light mode";
            } else {
                modeText.innerText = "Dark mode";
            }
        });
    }
});