const webpack = require('webpack')

const config = {
    entry: __dirname + "/frontend/src/index.jsx",
    output: {
        path: __dirname + "/frontend/static",
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                exclude: /node_modules/,
                use: 'babel-loader',
            }
        ]
    }
}



module.exports = config;