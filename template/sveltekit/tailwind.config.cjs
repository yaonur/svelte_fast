/** @type {import("tailwindcss").Config} */
module.exports = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors:{
        primary: "#FF6363",
        secondary: {
          100: "#e2e2d5",
          200: "#888883",
        },
      }
    }
  },
  plugins: []
};
