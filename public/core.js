//http://codepen.io/chaosmail/pen/xZgPmp/
angular.module('MyApp', ['ngMaterial', 'ngMessages', 'angular-canvas-gauge', 'md.data.table', 'n3-line-chart', 'ngRoute'])

    .config(['$mdThemingProvider', function ($mdThemingProvider) {
        'use strict';

        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    }])

    .controller('AppCtrl', function ($timeout, $scope, $mdToast, $mdDialog) {

        $scope.status = '  ';
        var last = {
            bottom: false,
            top: true,
            left: false,
            right: true
        };

        $scope.toastPosition = angular.extend({}, last);

        $scope.getToastPosition = function () {
            sanitizePosition();

            return Object.keys($scope.toastPosition)
                .filter(function (pos) {
                    return $scope.toastPosition[pos];
                })
                .join(' ');
        };

        function sanitizePosition() {
            var current = $scope.toastPosition;

            if (current.bottom && last.top) current.top = false;
            if (current.top && last.bottom) current.bottom = false;
            if (current.right && last.left) current.left = false;
            if (current.left && last.right) current.right = false;

            last = angular.extend({}, current);
        }

        $scope.showToast = function (msg) {
            // https://material.angularjs.org/latest/demo/toast
            // http://www.tutorialspoint.com/angular_material/angular_material_toasts.htm
            var pinTo = $scope.getToastPosition();
            $mdToast.show(
                $mdToast.simple()
                    .textContent(msg)
                    .hideDelay(3000)
                    .position(pinTo)
            );
        };
        $scope.show = {};
        $scope.show.graph1 = false;
        $scope.show.graph2 = false;
        $scope.show.graph3 = false;
        $scope.show.graph4 = false;

        $scope.showAlert = function (ev, titlemsg, textmsg) {
            // Appending dialog to document.body to cover sidenav in docs app
            // Modal dialogs should fully cover application
            // to prevent interaction outside of dialog
            $mdDialog.show(
                $mdDialog.alert()
                    .parent(angular.element(document.querySelector('#popupContainer')))
                    .clickOutsideToClose(true)
                    .title(titlemsg)
                    .textContent(textmsg)
                    .ariaLabel('Task Alert Dialog')
                    .ok('Ok')
                    .targetEvent(ev)
            );
        };

        $scope.showConfirm = function (ev) {
            // Appending dialog to document.body to cover sidenav in docs app
            var confirm = $mdDialog.confirm()
                .title('Deletar dados?')
                .textContent('Ao confirmar, todos os dados na planilha e gráficos serão deletados.')
                .ariaLabel('Lucky day')
                .targetEvent(ev)
                .ok('Deletar')
                .cancel('Cancelar');

            $mdDialog.show(confirm).then(function () {
                $scope.clear();
                $scope.status = 'You decided to get rid of your debt.';
            }, function () {
                $scope.status = 'You decided to keep your debt.';
            });
        };


        $scope.server = {};
        $scope.server.logger = false;
        $scope.server.project = {};
        /*
         $scope.server.project.id = 'Project MicroAlgae';
         $scope.server.project.series = 'Series 1';
         $scope.server.project.user = '';
         */
        $scope.getSeries = function () {
            try {
                var series_length = Object.keys($scope.server.udata['data'][$scope.server.project.id]).length;
                $scope.server.project.series = 'Series ' + (series_length + 1 );
            }
            catch (err) {
                if ($scope.server.project.id == '' || $scope.server.project.id == ' '|| $scope.server.project.id == undefined) {
                    $scope.server.project.series = undefined;
                } else {
                    $scope.server.project.series = 'Series 1';
                }
            }
        };

        $scope.showPrompt = function (ev) {
            // Appending dialog to document.body to cover sidenav in docs app
            var confirm;
            confirm = $mdDialog.prompt()
                .title('Create a new Project')
                .textContent('Choose a name for your new Project:')
                .placeholder('Project\'s name')
                .ariaLabel('Project\'s name')
                .targetEvent(ev)
                .ok('Okay!')
                .cancel('Cancelar');
            if ($scope.projects) {
                confirm.initialValue('Project ' + ($scope.projects.length + 1));
            }
            $mdDialog.show(confirm).then(function (result) {
                $scope.projects.push(result);
                $scope.server.project.id = result;
                $scope.getSeries();
                $scope.status = 'You decided to name your dog ' + result + '.';
            }, function () {
                $scope.status = 'You didn\'t name your dog.';
            });
        };
        // http://stackoverflow.com/questions/21574472/angularjs-cant-access-form-object-in-controller-scope
        $scope.trigger = function () {
            var pckg = $scope.server;

            if ($scope.server.logger) {
                $scope.table = [$scope.data];
                $scope.gdata.BsBdata = [];
                $scope.gdata.BsBdata.push(serialify($scope.data));
                $scope.showToast("BsBMonitor is now recording data from the device.");
                $scope.selectedIndex = 1;
                //$scope.showAlert(null, "re", "BsBMonitor is now recording data from the device.");
            } else {
                $scope.showToast("BsBMonitor is now on Monitor Mode.");
            }

            $.ajax({
                type: "POST",
                url: "/log",
                data: JSON.stringify(pckg),
                contentType: 'application/json',
                dataType: 'json',
                success: function () {
                    console.log(pckg);
                }
            });
        };

        $scope.clear = function () {
            $scope.table = [$scope.data];
            $scope.gdata.BsBdata = [];
            $scope.gdata.BsBdata.push(serialify($scope.data));
        };

        $scope.data = {};
        $scope.data.time = "00:00";
        $scope.data.ftime = new Date();
        $scope.data.stime = "Jun 06 2016 - 00:00";
        $scope.data.temp = 0;
        $scope.data.rotation = 0;
        $scope.data.ph = 0;
        $scope.data.po2 = 0;
        $scope.data.acid = 0;
        $scope.data.base = 0;
        $scope.data.afoam = 0;
        $scope.data.level = 0;
        $scope.data.subs1 = 0;
        $scope.data.subs1t = 0;
        $scope.data.subs2 = 0;
        $scope.data.subs2t = 0;
        $scope.data.gasmx = 0;
        $scope.data.airflow = 0;
        $scope.data.flhoeimv = 0;
        $scope.data.flux = 0;

        $scope.table = [];
        $scope.tcount = 0;
        $scope.interpolations = null;
        $scope.interpolation = null;
        $scope.config = {};
        $scope.config.g1 = {};
        $scope.config.g1.interpolation = 'bundle';
        $scope.config.g1.options = {};
        $scope.config.g1.options.array = [];
        $scope.config.g1.options.line = true;
        $scope.config.g1.options.dot = true;
        $scope.config.g1.options.area = true;
        $scope.config.g2 = {};
        $scope.config.g2.interpolation = 'bundle';
        $scope.config.g2.options = {};
        $scope.config.g2.options.array = [];
        $scope.config.g2.options.line = true;
        $scope.config.g2.options.dot = true;
        $scope.config.g2.options.area = true;
        $scope.config.g3 = {};
        $scope.config.g3.interpolation = 'bundle';
        $scope.config.g3.options = {};
        $scope.config.g3.options.array = [];
        $scope.config.g3.options.line = true;
        $scope.config.g3.options.dot = true;
        $scope.config.g3.options.area = true;
        $scope.config.g4 = {};
        $scope.config.g4.interpolation = 'bundle';
        $scope.config.g4.options = {};
        $scope.config.g4.options.array = [];
        $scope.config.g4.options.line = true;
        $scope.config.g4.options.dot = true;
        $scope.config.g4.options.area = true;

        // to ignore sidenav closed state on page load

        $scope.gauge = {
            value: 50,
            width: 350,
            height: 350
        };


        $scope.plotOptions = function (n) {
            var objs = {1: "g1", 2: "g2", 3: "g3", 4: "g4"};
            var opts = {1: "line", 2: "dot", 3: "area"};
            var graphs = {1: "graph_options_1", 2: "graph_options_2", 3: "graph_options_3", 4: "graph_options_4"};
            $scope.config[objs[n]].options.array = [];
            for (var i = 1; i <= 3; i++) {
                if ($scope.config[objs[n]].options[opts[i]]) {
                    $scope.config[objs[n]].options.array.push(opts[i]);
                }
            }
            if ($scope.config[objs[n]].options.array.length == 0) {
                $scope.config[objs[n]].options.array.push('line');
                $scope.config[objs[n]].options.line = true;

            }
            $scope[graphs[n]].series.forEach(function (element, index, array) {
                element.type = $scope.config[objs[n]].options.array;
            });
        };

        $scope.interpolations = [
            {id: 1, model: 'bundle'},
            {id: 2, model: 'linear'},
            {id: 3, model: 'cardinal'},
            {id: 4, model: 'monotone'},
            {id: 5, model: 'step'}
        ];

        $scope.graph_options_1 = {
            margin: {
                top: 25,
                bottom: 25
            },
            series: [
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_1",
                    label: "Rotação",
                    interpolation: {
                        mode: $scope.config.g1.interpolation
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: $scope.config.g1.options.array,
                    id: "RotSeries"
                },
                {
                    axis: "y2",
                    dataset: "BsBdata",
                    key: "val_5",
                    label: "Nível",
                    interpolation: {
                        mode: $scope.config.g1.interpolation
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: $scope.config.g1.options.array,
                    id: "LevelSeries"
                }
            ],
            axes: {x: {key: "x", type: "date"}}
        };
        $scope.graph_options_2 = {
            margin: {
                top: 25,
                bottom: 25
            },
            /*
             Curve Interpolation
             http://n3-charts.github.io/line-chart/#/docs
             https://github.com/d3/d3/wiki/SVG-Shapes#line_interpolate
             https://en.wikipedia.org/wiki/Cubic_Hermite_spline#Cardinal_spline
             https://en.wikipedia.org/wiki/B-spline
             https://en.wikipedia.org/wiki/Monotone_cubic_interpolation
             http://www.december.com/html/spec/colorhsla.html
             */
            series: [
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_2",
                    label: "Temperatura",
                    interpolation: {
                        mode: $scope.config.g2.interpolation
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: $scope.config.g2.options.array,
                    id: "mySeries2"
                },
                {
                    axis: "y2",
                    dataset: "BsBdata",
                    key: "val_4",
                    label: "pH",
                    interpolation: {
                        mode: $scope.config.g2.interpolation
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: $scope.config.g2.options.array,
                    id: "mySeries1"
                }
            ],
            axes: {x: {key: "x", type: "date"}}
        };
        $scope.graph_options_3 = {
            margin: {
                top: 25,
                bottom: 25
            },
            series: [
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_7",
                    label: "Subs1T",
                    interpolation: {
                        mode: $scope.config.g3.interpolation
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: $scope.config.g3.options.array,
                    id: "mySeries2"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_8",
                    label: "Subs2T",
                    interpolation: {
                        mode: $scope.config.g3.interpolation
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: $scope.config.g3.options.array,
                    id: "mySeries1"
                },
                {
                    axis: "y2",
                    dataset: "BsBdata",
                    key: "val_3",
                    label: "Vazão de Ar",
                    interpolation: {
                        mode: $scope.config.g3.interpolation
                    },
                    color: "hsla(204, 100%, 50%, 1)",
                    type: $scope.config.g3.options.array,
                    id: "airflow"
                }
            ],
            axes: {x: {key: "x", type: "date"}}
        };
        $scope.graph_options_4 = {
            margin: {
                top: 25,
                bottom: 25
            },
            series: [
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_9",
                    label: "Substrate 1",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: $scope.config.g4.options.array,
                    id: "subs1"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_10",
                    label: "Substrate 2",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: $scope.config.g4.options.array,
                    id: "subs2"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_11",
                    label: "Acid",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(204, 100%, 50%, 1)",
                    type: $scope.config.g4.options.array,
                    id: "acid"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_12",
                    label: "Base",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(275, 100%, 50%, 1)",
                    type: $scope.config.g4.options.array,
                    id: "base"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_13",
                    label: "Gas Mixture",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(29, 100%, 50%, 1)",
                    type: $scope.config.g4.options.array,
                    id: "gasmx"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_14",
                    label: "pO2",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(50, 100%, 50%, 1)",
                    type: $scope.config.g4.options.array,
                    id: "pO2"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_5",
                    label: "AFoam",
                    interpolation: {
                        mode: $scope.config.g4.interpolation
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: $scope.config.g4.options.array,
                    id: "aFoam"
                }
            ],
            axes: {x: {key: "x", type: "date"}}
        };


        [1, 2, 3, 4].forEach($scope.plotOptions);

        $scope.changeModel = function () {
            function GraphOptions(element, index, array) {
                element.interpolation.mode = String(this);
                //console.log("a[" + index + "] = " + element + this);
            }

            $scope.graph_options_1.series.forEach(GraphOptions, $scope.config.g1.interpolation);
            $scope.graph_options_2.series.forEach(GraphOptions, $scope.config.g2.interpolation);
            $scope.graph_options_3.series.forEach(GraphOptions, $scope.config.g3.interpolation);
            $scope.graph_options_4.series.forEach(GraphOptions, $scope.config.g4.interpolation);
            $scope.showToast("Interpolation Model updated.")
            setTimeout(function () {
                $scope.selectedIndex = 1;
            }, 1000);
        };

        $scope.gdata = {
            BsBdata: [
                {
                    val_1: 0.00,
                    val_2: 0.00,
                    val_3: 0.00,
                    val_4: 0.00,
                    val_5: 0.00,
                    val_6: 0.00,
                    val_7: 0.00,
                    val_8: 0.00,
                    val_9: 0.00,
                    val_10: 0.00,
                    val_11: 0.00,
                    val_12: 0.00,
                    val_13: 0.00,
                    val_14: 0.00,
                    x: new Date()
                }
            ]
        };
    })

    .controller('dataController', ['$http', '$mdEditDialog', '$mdDialog', '$q', '$timeout', '$scope', function ($http, $mdEditDialog, $q, $timeout, $mdDialog, $scope) {
        'use strict';

        $scope.options = {
            rowSelection: false,
            multiSelect: false,
            autoSelect: false,
            decapitate: false,
            largeEditDialog: false,
            boundaryLinks: false,
            limitSelect: false,
            pageSelect: false
        };

        $scope.selected = [];
        $scope.limitOptions = [5, 10, 15, {
            label: 'All',
            value: function () {
                return $scope.table ? $scope.table.length : 0;
            }
        }];

        $scope.query = {
            order: 'name',
            limit: 12,
            page: 1
        };

        // for testing ngRepeat
        $scope.columns = [{
            name: 'Hora',
            orderBy: 'name',
            unit: '(HH:MM)'
        }, {
            descendFirst: true,
            name: 'Type',
            orderBy: 'type'
        }, {
            name: 'Calories',
            numeric: true,
            orderBy: 'calories.value'
        }, {
            name: 'Fat',
            numeric: true,
            orderBy: 'fat.value',
            unit: 'g'
        }, {
            name: 'Protein',
            numeric: true,
            orderBy: 'protein.value',
            trim: true,
            unit: 'g'
        }, {
            name: 'Iron',
            numeric: true,
            orderBy: 'iron.value',
            unit: '%'
        }, {
            name: 'Comments',
            orderBy: 'comment'
        }];

        $http.get('templates/desserts.json').then(function (desserts) {
            $scope.desserts = desserts.data;

        });

        $scope.editComment = function (event, dessert) {
            event.stopPropagation();

            var dialog = {
                // messages: {
                //   test: 'I don\'t like tests!'
                // },
                modelValue: dessert.comment,
                placeholder: 'Add a comment',
                save: function (input) {
                    dessert.comment = input.$modelValue;
                },
                targetEvent: event,
                title: 'Add a comment',
                validators: {
                    'md-maxlength': 30
                }
            };

            var promise = $scope.options.largeEditDialog ? $mdEditDialog.large(dialog) : $mdEditDialog.small(dialog);

            promise.then(function (ctrl) {
                var input = ctrl.getInput();

                input.$viewChangeListeners.push(function () {
                    input.$setValidity('test', input.$modelValue !== 'test');
                });
            });
        };

        $scope.toggleLimitOptions = function () {
            $scope.limitOptions = $scope.limitOptions ? undefined : [5, 10, 15];
        };

        $scope.getTypes = function () {
            return ['Candy', 'Ice cream', 'Other', 'Pastry'];
        };

        $scope.onPaginate = function (page, limit) {
            console.log('Scope Page: ' + $scope.query.page + ' Scope Limit: ' + $scope.query.limit);
            console.log('Page: ' + page + ' Limit: ' + limit);

            $scope.promise = $timeout(function () {

            }, 2000);
        };

        $scope.deselect = function (item) {
            console.log(item.name, 'was deselected');
        };

        $scope.log = function (item) {
            console.log(item.name, 'was selected');
        };

        $scope.loadStuff = function () {
            $scope.promise = $timeout(function () {

            }, 2000);
        };

        $scope.onReorder = function (order) {

            console.log('Scope Order: ' + $scope.query.order);
            console.log('Order: ' + order);

            $scope.promise = $timeout(function () {

            }, 2000);
        };

    }]);

function serialify(data) {
    return {
        x: new Date(data.ftime),
        val_1: parseFloat(data.rotation),
        val_2: parseFloat(data.temp),
        val_3: parseFloat(data.airflow),
        val_4: parseFloat(data.ph),
        val_5: parseFloat(data.level),
        val_6: parseFloat(data.afoam),
        val_7: parseFloat(data.subs1t),
        val_8: parseFloat(data.subs2t),
        val_9: parseFloat(data.subs1),
        val_10: parseFloat(data.subs2),
        val_11: parseFloat(data.acid),
        val_12: parseFloat(data.base),
        val_13: parseFloat(data.gasmx),
        val_14: parseFloat(data.po2),
        val_15: parseFloat(data.lux)
    };
}

document.addEventListener('DOMContentLoaded', function () {
    var timeSrc = new EventSource('feed');
    timeSrc.addEventListener('time', function (event) {
        /*document.getElementById("Test").innerHTML += "\n " + event.data;*/
        var $scope = $("#appScope").scope();
        $scope.$apply(function () {
            $scope.data = eval('(' + event.data + ')');
            var now = new Date();
            $scope.data.ftime = new Date();
            //$scope.data.ftime = now.getUTCFullYear() + "-" + (now.getUTCMonth() + 1) + "-" + now.getUTCDate() +"T" + $scope.data.time + ":00.000Z";
            //$scope.data.stime =  now.getUTCDate() + "/" + (now.getUTCMonth() + 1) + "/" + now.getUTCFullYear() + " - " + $scope.data.time;
            $scope.data.stime = now.toString().replace(/.*(\D{3}) (\d{2}) (\d{4}).*/, '$2/$1/$3') + ' - ' + $scope.data.time;
        });
        $('#po2').highcharts().series[0].points[0].update(parseFloat($scope.data.po2));
        $('#base').highcharts().series[0].points[0].update(parseFloat($scope.data.base));
        $('#subs1').highcharts().series[0].points[0].update(parseFloat($scope.data.subs1));
        $('#subs2').highcharts().series[0].points[0].update(parseFloat($scope.data.subs2));
        $('#acid').highcharts().series[0].points[0].update(parseFloat($scope.data.acid));
        $('#gasmx').highcharts().series[0].points[0].update(parseFloat($scope.data.gasmx));

        $scope.table.push($scope.data);
        $scope.gdata.BsBdata.push(serialify($scope.data));

        $scope.tcount = $scope.table.length;
    });
}, false);

/*
 angular.forEach($scope.gdata, function (row) {
 row.x = new Date(row.x);
 });
 */