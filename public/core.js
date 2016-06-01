angular.module('MyApp', ['ngMaterial', 'ngMessages', 'angular-canvas-gauge', 'md.data.table', 'n3-line-chart'])

    .config(['$mdThemingProvider', function ($mdThemingProvider) {
        'use strict';

        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    }])

    .controller('AppCtrl', function ($scope) {
        $scope.data = {};
        $scope.data.time = "00:00";
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

        $scope.gauge = {
            value: 50,
            width: 350,
            height: 350
        };

        $scope.options = {
            margin: {
                top: 5
            },
            series: [
                {
                    axis: "y",
                    dataset: "noisy",
                    key: "val_0",
                    label: "Interpolated",
                    interpolation: {
                        mode: "bundle",
                        tension: 0.7
                    },
                    color: "hsla(88, 48%, 48%, 1)",
                    type: [
                        "line"
                    ],
                    id: "mySeries0"
                },
                {
                    axis: "y",
                    dataset: "noisy",
                    key: "val_0",
                    label: "Not interpolated",
                    color: "hsla(88, 48%, 48%, 1)",
                    type: [
                        "line"
                    ],
                    id: "mySeries1"
                }
            ],
            axes: {
                x: {
                    key: "x"
                }
            }
        };

        $scope.gdata = {
            timed: [
                {
                    x: "2016-05-01T23:29:24.390Z",
                    val_0: 0,
                    val_1: 0,
                    val_2: 0,
                    val_3: 0
                },
                {
                    x: "2016-05-02T23:29:24.390Z",
                    val_0: 0.993,
                    val_1: 3.894,
                    val_2: 8.47,
                    val_3: 14.347
                },
                {
                    x: "2016-05-03T23:29:24.390Z",
                    val_0: 1.947,
                    val_1: 7.174,
                    val_2: 13.981,
                    val_3: 19.991
                },
                {
                    x: "2016-05-04T23:29:24.390Z",
                    val_0: 2.823,
                    val_1: 9.32,
                    val_2: 14.608,
                    val_3: 13.509
                },
                {
                    x: "2016-05-05T23:29:24.390Z",
                    val_0: 3.587,
                    val_1: 9.996,
                    val_2: 10.132,
                    val_3: -1.167
                },
                {
                    x: "2016-05-06T23:29:24.390Z",
                    val_0: 4.207,
                    val_1: 9.093,
                    val_2: 2.117,
                    val_3: -15.136
                },
                {
                    x: "2016-05-07T23:29:24.390Z",
                    val_0: 4.66,
                    val_1: 6.755,
                    val_2: -6.638,
                    val_3: -19.923
                },
                {
                    x: "2016-05-08T23:29:24.390Z",
                    val_0: 4.927,
                    val_1: 3.35,
                    val_2: -13.074,
                    val_3: -12.625
                },
                {
                    x: "2016-05-09T23:29:24.390Z",
                    val_0: 4.998,
                    val_1: -0.584,
                    val_2: -14.942,
                    val_3: 2.331
                },
                {
                    x: "2016-05-10T23:29:24.390Z",
                    val_0: 4.869,
                    val_1: -4.425,
                    val_2: -11.591,
                    val_3: 15.873
                }
            ],
            tolerance: [
                {
                    x: 0,
                    average: 22,
                    extrema_min: 19,
                    extrema_max: 25
                },
                {
                    x: 1,
                    average: 24,
                    extrema_min: 21,
                    extrema_max: 28
                },
                {
                    x: 2,
                    average: 22,
                    extrema_min: 18,
                    extrema_max: 26
                },
                {
                    x: 3,
                    average: 20,
                    extrema_min: 17,
                    extrema_max: 25
                },
                {
                    x: 4,
                    average: 23,
                    extrema_min: 20,
                    extrema_max: 26
                },
                {
                    x: 5,
                    average: 22,
                    extrema_min: 20,
                    extrema_max: 24
                },
                {
                    x: 6,
                    average: 22,
                    extrema_min: 18,
                    extrema_max: 25
                },
                {
                    x: 7,
                    average: 24,
                    extrema_min: 22,
                    extrema_max: 28
                },
                {
                    x: 8,
                    average: 25,
                    extrema_min: 22,
                    extrema_max: 27
                },
                {
                    x: 9,
                    average: 23,
                    extrema_min: 21,
                    extrema_max: 26
                }
            ],
            numerical: [
                {
                    x: 0,
                    val_0: 0,
                    val_1: 0,
                    val_2: 0,
                    val_3: 0
                },
                {
                    x: 1,
                    val_0: 0.993,
                    val_1: 3.894,
                    val_2: 8.47,
                    val_3: 14.347
                },
                {
                    x: 2,
                    val_0: 1.947,
                    val_1: 7.174,
                    val_2: 13.981,
                    val_3: 19.991
                },
                {
                    x: 3,
                    val_0: 2.823,
                    val_1: 9.32,
                    val_2: 14.608,
                    val_3: 13.509
                },
                {
                    x: 4,
                    val_0: 3.587,
                    val_1: 9.996,
                    val_2: 10.132,
                    val_3: -1.167
                },
                {
                    x: 5,
                    val_0: 4.207,
                    val_1: 9.093,
                    val_2: 2.117,
                    val_3: -15.136
                },
                {
                    x: 6,
                    val_0: 4.66,
                    val_1: 6.755,
                    val_2: -6.638,
                    val_3: -19.923
                },
                {
                    x: 7,
                    val_0: 4.927,
                    val_1: 3.35,
                    val_2: -13.074,
                    val_3: -12.625
                },
                {
                    x: 8,
                    val_0: 4.998,
                    val_1: -0.584,
                    val_2: -14.942,
                    val_3: 2.331
                },
                {
                    x: 9,
                    val_0: 4.869,
                    val_1: -4.425,
                    val_2: -11.591,
                    val_3: 15.873
                }
            ],
            logarithmic: [
                {
                    x: 0,
                    val_0: 300000,
                    val_1: 400000,
                    val_2: 500000,
                    val_3: 600000
                },
                {
                    x: 1,
                    val_0: 208060,
                    val_1: 308060,
                    val_2: 408060,
                    val_3: 508060
                },
                {
                    x: 2,
                    val_0: 16771,
                    val_1: 116771,
                    val_2: 216771,
                    val_3: 316771
                },
                {
                    x: 3,
                    val_0: 97998,
                    val_1: 2002,
                    val_2: 102002,
                    val_3: 202002
                },
                {
                    x: 4,
                    val_0: 30728,
                    val_1: 69272,
                    val_2: 169272,
                    val_3: 269272
                },
                {
                    x: 5,
                    val_0: 156732,
                    val_1: 256732,
                    val_2: 356732,
                    val_3: 456732
                },
                {
                    x: 6,
                    val_0: 292034,
                    val_1: 392034,
                    val_2: 492034,
                    val_3: 592034
                },
                {
                    x: 7,
                    val_0: 250780,
                    val_1: 350780,
                    val_2: 450780,
                    val_3: 550780
                },
                {
                    x: 8,
                    val_0: 70900,
                    val_1: 170900,
                    val_2: 270900,
                    val_3: 370900
                },
                {
                    x: 9,
                    val_0: 82226,
                    val_1: 17774,
                    val_2: 117774,
                    val_3: 217774
                }
            ],
            noisy: [
                {
                    x: 0,
                    val_0: 82,
                    val_1: 78,
                    val_2: 30,
                    val_3: 3
                },
                {
                    x: 1,
                    val_0: 7,
                    val_1: 75,
                    val_2: 49,
                    val_3: 57
                },
                {
                    x: 2,
                    val_0: 91,
                    val_1: 65,
                    val_2: 78,
                    val_3: 77
                },
                {
                    x: 3,
                    val_0: 96,
                    val_1: 37,
                    val_2: 48,
                    val_3: 95
                },
                {
                    x: 4,
                    val_0: 44,
                    val_1: 82,
                    val_2: 46,
                    val_3: 70
                },
                {
                    x: 5,
                    val_0: 97,
                    val_1: 97,
                    val_2: 1,
                    val_3: 54
                },
                {
                    x: 6,
                    val_0: 14,
                    val_1: 22,
                    val_2: 96,
                    val_3: 27
                },
                {
                    x: 7,
                    val_0: 51,
                    val_1: 26,
                    val_2: 66,
                    val_3: 62
                },
                {
                    x: 8,
                    val_0: 70,
                    val_1: 2,
                    val_2: 5,
                    val_3: 54
                },
                {
                    x: 9,
                    val_0: 14,
                    val_1: 5,
                    val_2: 85,
                    val_3: 31
                }
            ],
            interrupted: [
                {
                    x: 0,
                    val_0: 0,
                    val_1: 0,
                    val_2: 0,
                    val_3: 0
                },
                {
                    x: 1,
                    val_0: 0.993,
                    val_1: 3.894,
                    val_2: 8.47,
                    val_3: 14.347
                },
                {
                    x: 2,
                    val_0: 1.947,
                    val_1: 7.174,
                    val_2: 13.981,
                    val_3: 19.991
                },
                {
                    x: 3,
                    val_0: 2.823,
                    val_1: 9.32,
                    val_2: 14.608,
                    val_3: 13.509
                },
                {
                    x: 4,
                    val_0: 3.587,
                    val_1: 9.996,
                    val_2: 10.132,
                    val_3: 1.167
                },
                {
                    x: 5,
                    val_0: 4.207,
                    val_1: 9.093,
                    val_2: 2.117,
                    val_3: 15.136
                },
                {
                    x: 6,
                    val_0: 4.66,
                    val_1: 6.755,
                    val_2: 6.638,
                    val_3: 19.923
                },
                {
                    x: 7,
                    val_0: 4.927,
                    val_1: 3.35,
                    val_2: 13.074
                },
                {
                    x: 8,
                    val_0: 4.998,
                    val_1: 0.584
                },
                {
                    x: 9,
                    val_0: 4.869
                }
            ],
            parametric: [
                {
                    x: 2,
                    y: 0
                },
                {
                    x: 1.9138806714644176,
                    y: 0.9427934736519953
                },
                {
                    x: 1.6629392246050905,
                    y: 1.6629392246050905
                },
                {
                    x: 1.268786568327291,
                    y: 1.9903694533443936
                },
                {
                    x: 0.7653668647301797,
                    y: 1.8477590650225735
                },
                {
                    x: 0.19603428065912154,
                    y: 1.268786568327291
                },
                {
                    x: -0.3901806440322564,
                    y: 0.3901806440322572
                },
                {
                    x: -0.9427934736519954,
                    y: -0.5805693545089242
                },
                {
                    x: -1.414213562373095,
                    y: -1.414213562373095
                },
                {
                    x: -1.7638425286967099,
                    y: -1.9138806714644176
                },
                {
                    x: -1.9615705608064609,
                    y: -1.9615705608064609
                },
                {
                    x: -1.9903694533443939,
                    y: -1.5460209067254749
                },
                {
                    x: -1.8477590650225737,
                    y: -0.7653668647301808
                },
                {
                    x: -1.5460209067254738,
                    y: 0.19603428065912182
                },
                {
                    x: -1.1111404660392044,
                    y: 1.1111404660392066
                },
                {
                    x: -0.5805693545089231,
                    y: 1.7638425286967114
                },
                {
                    x: 3.185319639056295e-15,
                    y: 2
                },
                {
                    x: 0.5805693545089275,
                    y: 1.763842528696707
                },
                {
                    x: 1.1111404660392066,
                    y: 1.1111404660391988
                },
                {
                    x: 1.5460209067254764,
                    y: 0.19603428065911419
                },
                {
                    x: 1.8477590650225757,
                    y: -0.7653668647301862
                },
                {
                    x: 1.9903694533443943,
                    y: -1.5460209067254786
                },
                {
                    x: 1.96157056080646,
                    y: -1.961570560806463
                },
                {
                    x: 1.7638425286967068,
                    y: -1.9138806714644145
                },
                {
                    x: 1.4142135623730892,
                    y: -1.414213562373087
                },
                {
                    x: 0.9427934736519882,
                    y: -0.5805693545089101
                },
                {
                    x: 0.39018064403224884,
                    y: 0.39018064403227165
                },
                {
                    x: -0.19603428065913053,
                    y: 1.268786568327303
                },
                {
                    x: -0.7653668647301897,
                    y: 1.8477590650225795
                },
                {
                    x: -1.2687865683273005,
                    y: 1.9903694533443923
                },
                {
                    x: -1.6629392246050962,
                    y: 1.6629392246050796
                },
                {
                    x: -1.9138806714644212,
                    y: 0.9427934736519777
                },
                {
                    x: -2,
                    y: -2.009163527365565e-14
                },
                {
                    x: -1.9138806714644143,
                    y: -0.9427934736520163
                },
                {
                    x: -1.6629392246050831,
                    y: -1.6629392246051018
                },
                {
                    x: -1.2687865683272799,
                    y: -1.990369453344396
                },
                {
                    x: -0.7653668647301647,
                    y: -1.8477590650225628
                },
                {
                    x: -0.19603428065910372,
                    y: -1.268786568327272
                },
                {
                    x: 0.3901806440322718,
                    y: -0.3901806440322288
                },
                {
                    x: 0.9427934736520104,
                    y: 0.5805693545089554
                },
                {
                    x: 1.4142135623731082,
                    y: 1.4142135623731154
                },
                {
                    x: 1.7638425286967179,
                    y: 1.9138806714644272
                },
                {
                    x: 1.9615705608064637,
                    y: 1.9615705608064553
                },
                {
                    x: 1.9903694533443925,
                    y: 1.5460209067254576
                },
                {
                    x: 1.8477590650225695,
                    y: 0.7653668647301589
                },
                {
                    x: 1.5460209067254684,
                    y: -0.19603428065914005
                },
                {
                    x: 1.111140466039199,
                    y: -1.1111404660392175
                },
                {
                    x: 0.5805693545089204,
                    y: -1.7638425286967159
                },
                {
                    x: -2.450531559567883e-15,
                    y: -2
                },
                {
                    x: -0.5805693545089251,
                    y: -1.7638425286967074
                },
                {
                    x: -1.111140466039203,
                    y: -1.1111404660392028
                },
                {
                    x: -1.5460209067254715,
                    y: -0.19603428065912248
                },
                {
                    x: -1.8477590650225713,
                    y: 0.7653668647301752
                },
                {
                    x: -1.990369453344393,
                    y: 1.5460209067254689
                },
                {
                    x: -1.9615705608064629,
                    y: 1.9615705608064586
                },
                {
                    x: -1.7638425286967157,
                    y: 1.913880671464422
                },
                {
                    x: -1.4142135623731047,
                    y: 1.4142135623731078
                },
                {
                    x: -0.9427934736520092,
                    y: 0.5805693545089453
                },
                {
                    x: -0.390180644032274,
                    y: -0.3901806440322321
                },
                {
                    x: 0.19603428065910153,
                    y: -1.2687865683272692
                },
                {
                    x: 0.7653668647301594,
                    y: -1.8477590650225615
                },
                {
                    x: 1.2687865683272725,
                    y: -1.9903694533443972
                },
                {
                    x: 1.662939224605076,
                    y: -1.6629392246051118
                },
                {
                    x: 1.9138806714644097,
                    y: -0.942793473652032
                },
                {
                    x: 2,
                    y: -4.508185774390072e-14
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

document.addEventListener('DOMContentLoaded', function () {
    var timeSrc = new EventSource('feed');
    timeSrc.addEventListener('time', function (event) {
        /*document.getElementById("Test").innerHTML += "\n " + event.data;*/
        var $scope = $("#appScope").scope();
        $scope.$apply(function () {
            $scope.data = eval('(' + event.data + ')');
        });
        $('#po2').highcharts().series[0].points[0].update(parseFloat($scope.data.po2));
        $('#base').highcharts().series[0].points[0].update(parseFloat($scope.data.base));
        $('#subs1').highcharts().series[0].points[0].update(parseFloat($scope.data.subs1));
        $('#subs2').highcharts().series[0].points[0].update(parseFloat($scope.data.subs2));
        $('#acid').highcharts().series[0].points[0].update(parseFloat($scope.data.acid));
        $('#gasmx').highcharts().series[0].points[0].update(parseFloat($scope.data.gasmx));
        $scope.table.push($scope.data);
        $scope.tcount = $scope.table.length;
    });
}, false);