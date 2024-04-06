let menuIcon = document.getElementById('menu-icon');

menuIcon.addEventListener('click', () => {
	const sidebar = document.getElementById('menu');
	sidebar.classList.toggle('active');

	if (sidebar.classList.contains('active')) {
		menuIcon.classList.replace('bx-menu', 'bx-x');
	} else {
		menuIcon.classList.replace('bx-x', 'bx-menu');
	}
});
