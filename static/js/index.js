//Toggle sidebar
const menuIcon = document.getElementById('menu-icon');
const menu = document.getElementById('menu');

menuIcon.addEventListener('click', () => {
	if (menu.classList.contains('open')) {
		menu.classList.remove('open');
		menuIcon.classList.replace('bx-x', 'bx-menu');
	} else {
		menu.classList.add('open');
		menuIcon.classList.replace('bx-menu', 'bx-x');
	}
});
