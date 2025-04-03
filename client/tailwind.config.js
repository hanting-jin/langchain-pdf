/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}', 'node_modules/preline/dist/*.js'],
	theme: {
		extend: {}
	},
	darkMode: false, // 禁用dark模式
	plugins: [require('preline/plugin')]
};
