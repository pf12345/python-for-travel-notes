var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var loaders = [
    {
        "test": /\.js?$/,
        "exclude": /node_modules/,
        "loader": "babel-loader",
        "query": {
            "presets": [
                "es2015",
                "stage-0"
            ],
            "plugins": []
        }
    },
    {
        "test": /\.vue?$/,
        "loader": "vue"
    },
    {
        "test": /\.less$/,
        "loader": "style!css!less"
    }
];

module.exports = {
    entry: path.resolve('static/js', 'main.js'),
    output: {
        path: path.resolve('static/js'),
        filename: 'build.js',
        publicPath: '/'
    },
    module: {
        loaders: loaders
    },
    /*vue: {
        loaders: {
            css: ExtractTextPlugin.extract("css"),
            // you can also include <style lang="less"> or other langauges
            less: ExtractTextPlugin.extract("css!less")
        }
    },*/
    plugins: [
        // new webpack.optimize.UglifyJsPlugin({
        //     minimize: true,
        //     compress:{
        //         warnings: false,
        //         drop_debugger: true,
        //         drop_console: true
        //     }
        // }),
        // new ExtractTextPlugin("vue_style.css")
    ],
    watch: true
};
