module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        less: {
            development: {
                options: {
                    compress: true
                },
                files: {
                    'static/css/common/base.css': 'static/less/common/base.less',
                }
            }
        },

        watch: {
            less: {
                files: 'static/less/**/*.less',
                tasks: ['less']
            },
        }
    });

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('less', ['less']);

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
}
