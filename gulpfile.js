var gulp = require('gulp');
var browserify = require('browserify');
var sass = require('gulp-sass');
var eslint = require('gulp-eslint');
var babelify = require("babelify");
var source = require('vinyl-source-stream');

gulp.task('lint', function () {
  return gulp.src(['src/**/*.js'])
    .pipe(eslint())
    .pipe(eslint.format())
    .pipe(eslint.failOnError());
});

gulp.task('scripts', ['lint'], function() {
  var b = browserify({
    entries: 'src/pykin.js',
    debug: true
  }).transform(babelify)
    .bundle()
    .pipe(source('pykin.js'))
    .pipe(gulp.dest('pykin/static'));
});

gulp.task('styles', function() {
  gulp.src('src/**/*.sass')
    .pipe(sass({
      indentedSyntax: true,
      includePaths: ['node_modules/bootstrap-sass/assets/stylesheets']
    }).on('error', sass.logError))
    .pipe(gulp.dest('pykin/static'));
});

gulp.task('compile', ['scripts', 'styles']);

gulp.task('default', function() {
  gulp.watch('src/**/*.sass', ['styles']);
  gulp.watch('src/**/*.js', ['scripts']);
});
