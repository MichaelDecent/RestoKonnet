/** @type {import('tailwindcss').Config} */

const preline = require('preline/plugin.js');

module.exports = {
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    theme: {
      extend: {
        colors: {
            ryellow: '#FFAA29',
            rgreen: {
                100: '#489B53',
                200: '#306737',
            }
        },
      },
    },
    variants: {
      extend: {},
    },
    plugins: [
        require('preline/plugin'),
    ],
  }