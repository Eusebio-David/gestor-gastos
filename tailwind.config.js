import { typography } from '@tailwindcss/typography'

export default {
  content: [
    './templates/**/*.html',
    './tu_app/**/*.html',
    './**/*.js', // si usás archivos JS o TS que contienen clases de Tailwind
  ],
  theme: {
    extend: {},
  },
  plugins: [typography],
}
