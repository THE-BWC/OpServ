import defaultTheme from 'tailwindcss/defaultTheme'

/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./app/templates/**/*.html",
        "./app/static/src/**/*.js",
        "./app/static/node_modules/flowbite/**/*.js",
    ],
    darkMode: 'class',
    theme: {
        fontFamily: {
            'sans': ['Roboto','Helvetica Neue','Helvetica','Oxygen','Ubuntu','Cantarell','Fira Sans','Droid Sans','sans-serif']
        },
        screens: {
            'xs': '416px',
            ...defaultTheme.screens,
        },
        colors: {
            'primary': '#901919',
            'secondary': '#3a3a3a',
            'success': '#4caf50',
            'info': '#2196f3',
            'warning': '#ff9800',
            'danger': '#f44336',
            'light': '#dadada',
            'dark': '#212121',
            'link': '#41b6ff',
            'gradient-dark': '#681000',
            'gradient-light': '#8c0902',
            'gradient-border': '#ab0900',
            ...defaultTheme.colors,
        },
        extend: {
            backgroundImage: {
                'honeycomb': "url('/static/honeycomb.png')",
                'forum-header': "url('/static/Forum_Header_Background.png')",
            },
            colors: {
                'gray-100': '#bababa',
                'gray-200': '#999',
                'gray-300': '#7F7F7F',
                'gray-400': '#666',
                'gray-500': '#323232FF',
                'gray-600': '#2d2d2d',
                'gray-700': '#292929',
                'gray-800': '#252525',
                'gray-900': '#212529',
            },
        },
    },
    fontFamily: {
        'body': [
            'Inter',
            'ui-sans-serif',
            'system-ui',
            '-apple-system',
            'system-ui',
            'Segoe UI',
            'Roboto',
            'Helvetica Neue',
            'Arial',
            'Noto Sans',
            'sans-serif',
            'Apple Color Emoji',
            'Segoe UI Emoji',
            'Segoe UI Symbol',
            'Noto Color Emoji'
        ],
        'sans': [
            'Inter',
            'ui-sans-serif',
            'system-ui',
            '-apple-system',
            'system-ui',
            'Segoe UI',
            'Roboto',
            'Helvetica Neue',
            'Arial',
            'Noto Sans',
            'sans-serif',
            'Apple Color Emoji',
            'Segoe UI Emoji',
            'Segoe UI Symbol',
            'Noto Color Emoji'
        ]
    },
    plugins: [
        require('flowbite/plugin')
    ],
}

