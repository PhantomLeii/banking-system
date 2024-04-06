const menuIcon = document.getElementById('menu-icon');

menuIcon.addEventListener('click', () => {
	const sidebar = document.getElementById('menu');
	sidebar.classList.toggle('active');

	if (sidebar.classList.contains('active')) {
		menuIcon.classList.replace('bx-menu', 'bx-x');
	} else {
		menuIcon.classList.replace('bx-x', 'bx-menu');
	}
});

window.addEventListener('scroll', () => {
	const navbar = document.getElementById('navbar');
	const position = navbar.offsetTop;

	if (window.scrollY > position) {
		navbar.classList.add('sticky');
	} else {
		navbar.classList.remove('sticky');
	}
});
