const { addDynamicIconSelectors } = require('@iconify/tailwind');
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: ['./src/**/*.{html,js,svelte,ts}'],
      theme: {
        extend: {
          colors: {
            primary:{
              100: "hsl(220 10% 60%)",
              DEFAULT: "hsl(220 10% 98%)"
            },
            bg:{
              DEFAULT: "hsl(220 10% 10%)"
            }
          },
          width: {
            main: '60ch',
          },
          spacing:{
            main:'1rem'
          }
        }
      },

      plugins: [addDynamicIconSelectors(),]
    };
