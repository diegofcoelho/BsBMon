/**
 * Created by dfcoelho on 21/05/2016.
 */
jQuery(document).ready(function ($) {

    var $scope = $("#appScope").scope()

    var gaugeOptions = {

        chart: {
            type: 'solidgauge'
        },

        title: null,

        pane: {
            center: ['50%', '80%'],
            size: '100%',
            startAngle: -90,
            endAngle: 90,
            background: {
                backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
                innerRadius: '60%',
                outerRadius: '100%',
                shape: 'arc'
            }
        },

        tooltip: {
            enabled: false
        },

        // the value axis
        yAxis: {
            stops: [
                [0.1, '#55BF3B'], // green
                [0.5, '#DDDF0D'], // yellow
                [0.9, '#DF5353'] // red
            ],
            lineWidth: 0,
            minorTickInterval: null,
            tickPixelInterval: 400,
            tickWidth: 0,
            title: {
                y: -70
            },
            labels: {
                y: 16
            }
        },

        plotOptions: {
            solidgauge: {
                dataLabels: {
                    y: 5,
                    borderWidth: 0,
                    useHTML: true
                }
            }
        }
    };

    // The speed gauge
    $('#po2').highcharts(Highcharts.merge(gaugeOptions, {
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'pO2'
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'pO2',
            data: [$scope.data.po2],
            dataLabels: {
                format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
                '<span style="font-size:12px;color:silver">%</span></div>'
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]

    }));
    // substrate gauge
    $('#subs1').highcharts(Highcharts.merge(gaugeOptions, {
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'Substrate 1'
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'Substrate 1',
            data: [$scope.data.subs1],
            dataLabels: {
                format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
                '<span style="font-size:12px;color:silver">%</span></div>'
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]

    }));
    // substrate gauge
    $('#subs2').highcharts(Highcharts.merge(gaugeOptions, {
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'Substrate 2'
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'Substrate 2',
            data: [$scope.data.subs2],
            dataLabels: {
                format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
                '<span style="font-size:12px;color:silver">%</span></div>'
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]

    }));

    $('#gasmx').highcharts(Highcharts.merge(gaugeOptions, {
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'Gas Mixture'
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'Gas Mixture',
            data: [$scope.data.gasmx],
            dataLabels: {
                format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
                '<span style="font-size:12px;color:silver">%</span></div>'
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]

    }));

    $('#acid').highcharts(Highcharts.merge(gaugeOptions, {
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'Acid'
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'Acid',
            data: [$scope.data.acid],
            dataLabels: {
                format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
                '<span style="font-size:12px;color:silver">%</span></div>'
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]

    }));

    $('#base').highcharts(Highcharts.merge(gaugeOptions, {
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'Base'
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'Base',
            data: [$scope.data.base],
            dataLabels: {
                format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
                '<span style="font-size:12px;color:silver">%</span></div>'
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]

    }));


});