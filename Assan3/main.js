document.addEventListener("DOMContentLoaded", () => {
    let header = document.querySelector('header .blocked');
    let header_height = header.clientHeight;

    window.addEventListener('scroll', event => {
        if (this.scrollY > header_height) {
            header.classList.replace('blocked', 'fixed');
        } else {
            header.classList.replace('fixed', 'blocked');
        };
    });
});