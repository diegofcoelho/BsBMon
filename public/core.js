angular.module('MyApp', ['ngMaterial', 'ngMessages', 'angular-canvas-gauge', 'md.data.table', 'n3-line-chart'])

    .config(['$mdThemingProvider', function ($mdThemingProvider) {
        'use strict';

        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    }])

    .controller('AppCtrl', function ($timeout, $scope) {

        $scope.show = {};
        $scope.show.graph1 = false;
        $scope.show.graph2 = false;
        $scope.show.graph3 = false;
        $scope.show.graph4 = false;

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

        $scope.table = [];
        $scope.tcount = 0;
        $scope.interpolations = null;
        $scope.interpolation = null;

        $scope.gauge = {
            value: 50,
            width: 350,
            height: 350
        };

        $scope.interpolations = [
                        {id: 1, model: 'bundle'},
                        {id: 2, model: 'linear'},
                        {id: 3, model: 'cardinal'},
                        {id: 4, model: 'monotone'},
                        {id: 5, model: 'step'}
                    ];
/*
        $scope.loadInter = function () {

            // Use timeout to simulate a 650ms request.
            return $timeout(function () {

                $scope.interpolations = $scope.interpolations || [
                        {id: 1, model: 'bundle'},
                        {id: 2, model: 'linear'},
                        {id: 3, model: 'cardinal'},
                        {id: 4, model: 'monotone'},
                        {id: 5, model: 'step'}
                    ];

            }, 650);
        };
*/
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
                        mode: "monotone"
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: ["line"],
                    id: "RotSeries"
                },
                {
                    axis: "y2",
                    dataset: "BsBdata",
                    key: "val_5",
                    label: "Nível",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: ["line"],
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
                        mode: "monotone"
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: ["line"],
                    id: "mySeries2"
                },
                {
                    axis: "y2",
                    dataset: "BsBdata",
                    key: "val_4",
                    label: "pH",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: ["line"],
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
                        mode: "monotone"
                    },
                    color: "hsla(0,100%,50%, 0.8)",
                    type: ["line"],
                    id: "mySeries2"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_8",
                    label: "Subs2T",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: ["line"],
                    id: "mySeries1"
                },
                {
                    axis: "y2",
                    dataset: "BsBdata",
                    key: "val_3",
                    label: "Vazão de Ar",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: ["line"],
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
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "subs1"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_10",
                    label: "Substrate 2",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "subs2"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_11",
                    label: "Acid",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "acid"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_12",
                    label: "Base",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "base"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_13",
                    label: "Gas Mixture",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "gasmx"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_14",
                    label: "pO2",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "pO2"
                },
                {
                    axis: "y",
                    dataset: "BsBdata",
                    key: "val_5",
                    label: "AFoam",
                    interpolation: {
                        mode: "monotone"
                    },
                    color: "hsla(240,100%,25%, 0.8)",
                    type: ["line"],
                    id: "aFoam"
                }
            ],
            axes: {x: {key: "x", type: "date"}}
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

    .controller('dataController', ['$http', '$mdEditDialog', '$q', '$timeout', '$scope', function ($http, $mdEditDialog, $q, $timeout, $scope) {
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
        val_14: parseFloat(data.po2)
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