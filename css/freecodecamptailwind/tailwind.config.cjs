/** @type {import("tailwindcss").Config} */
module.exports = {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {

    extend: {

      colors: {
        vuejs: {
          100: "#67d7a6",
          200: "#41b883",
        }
      }
    }
  },
  plugins: [

  ]
};
