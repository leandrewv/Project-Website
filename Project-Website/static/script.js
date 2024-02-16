let register_btn = document.querySelector(".register-btn");  // Corrected class name
let login_btn = document.querySelector(".Login-btn");
let form = document.querySelector(".Form-box");

register_btn.addEventListener("click", () => {
    form.classList.add("change-form");
});

login_btn.addEventListener("click", () => {
    form.classList.remove("change-form");
});
const password = "{{ password }}";
const username = "{{ username }}";