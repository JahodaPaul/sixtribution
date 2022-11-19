/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,ts}'],
  theme: {
    extend: {
      colors: {
        'sixt-orange': '#ff2c00',
      },
    },
  },
  plugins: [],
}
