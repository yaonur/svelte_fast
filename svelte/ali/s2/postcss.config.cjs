const postcssPresetEnv = require("postcss-preset-env");
const autorPrefixer = require("autoprefixer");
const tailwindCss = require("tailwindcss");
const nesting = require("postcss-nesting");
const tailwindcssNesting = require("tailwindcss/nesting");
const preCss = require("precss");
const postcssimport = require("postcss-import");
module.exports = {
  plugins: [
    // postcssPresetEnv({
    //   stage: 3,
    //   features: {
    //     "nesting-rules": true,
    //     "custom-media-queries": true,
    //     "media-query-ranges": true,
    //   },
    // }),
    // preCss,
    tailwindcssNesting(nesting),
    autorPrefixer,
    tailwindCss,
    // postcssimport({prependData: '@import "./variables.scss";'}),
  ],
};

