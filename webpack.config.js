const path = require('path');
const rootAssetPath = path.resolve(__dirname, 'app/assets');

module.exports = {
	entry: rootAssetPath + '/scripts/index.js',
	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname, 'app/static')
	},
	module: {
		rules: [
			{
				test: /\.(scss)$/,
				use: [{
					loader: 'style-loader', // inject CSS to page
				}, {
					loader: 'css-loader', // translates CSS into CommonJS modules
				}, {
					loader: 'postcss-loader', // Run post css actions
					options: {
						plugins: function () { // post css plugins, can be exported to postcss.config.js
							return [
								require('precss'),
								require('autoprefixer')
							];
						}
					}
				}, {
					loader: 'sass-loader' // compiles Sass to CSS
				}]
			},
			{
				test: /\.(png|jpg|gif)$/,
				use: [{
					loader: 'file-loader',
					options: {
						outputPath: path.resolve(__dirname, 'app/static/img')
					}
				}, {
					loader: 'image-webpack-loader',
					options: {
						disable: true
					}
				}]
			}
		]
	},
	externals: {
		jquery: 'jQuery',
	}
};
