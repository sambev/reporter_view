module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        less: {
            development: {
                options: {
                    compress: true
                },
                files: {
                    'reporter_view/static/css/common/base.css': 'reporter_view/static/less/common/base.less',
                }
            }
        },

        watch: {
            less: {
                files: 'reporter_view/static/less/**/*.less',
                tasks: ['less']
            },
        }
    });

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('less', ['less']);

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
}
