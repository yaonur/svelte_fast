/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        primary:'#202225',
        secondary:'#5865f2',
        gray:{
          900:'#202225',
          800:'#2f3136',
          700:'#36393f',
          600:'#4f545c',
          500:'#72767d',
          400:'#8e9297',
          300:'#b9bbbe',
          200:'#d7d8da',
          100:'#ebebeb',

        }
      }
    }
  },
  plugins: []
};
