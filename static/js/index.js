window.addEventListener('scroll', () => {
	const navbar = document.getElementById('navbar');
	const offset = navbar.offsetTop;

	if (window.scrollY > offset) {
		navbar.classList.add('sticky');
	} else {
		navbar.classList.remove('sticky');
	}
});

const menuIcon = document.getElementById('menu-icon');

menuIcon.addEventListener('click', () => {
	const menu = document.getElementById('menu');
	let menuState = false;

	if (menuState) {
		menu.classList.add('open');
	} else {
		menu.classList.remove('open');
	}
});
