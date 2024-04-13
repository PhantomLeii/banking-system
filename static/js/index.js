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

// Add box-shadow on scroll
const navbar = document.getElementById('navbar');
const postion = navbar.offsetTop;

window.addEventListener('scroll', () => {
	if (window.scrollY > postion) {
		navbar.classList.add('sticky');
	} else {
		navbar.classList.remove('sticky');
	}
});

// Swap currency '.' with ','
const balances = document.querySelectorAll('.balance span');

balances.forEach((balance) => {
	balance.textContent = balance.textContent.replace('.', ',');
});

// Display transaction colum only when transactions are available
// for rendering
const transactionsColumn = document.querySelector('.transactions');

window.addEventListener('DOMContentLoaded', () => {
	const transactionItemCount = transactionsColumn.children.length;
	if (transactionItemCount < 2) {
		transactionsColumn.classList.add('hidden');
	} else {
		transactionsColumn.classList.remove('hidden');
	}
});
