/**
 * Created by dfcoelho on 21/05/2016.
 */
jQuery(document).ready(function ($) {
    //you can now use $ as your jQuery object.
    var body = $('body');
    $('#container').highcharts({

            chart: {
                type: 'gauge',
                plotBackgroundColor: null,
                plotBackgroundImage: null,
                plotBorderWidth: 0,
                plotShadow: false
            },

            title: {
                text: 'Speedometer'
            },

            pane: {
                startAngle: -150,
                endAngle: 150,
                background: [{
                    backgroundColor: {
                        linearGradient: {x1: 0, y1: 0, x2: 0, y2: 1},
                        stops: [
                            [0, '#FFF'],
                            [1, '#333']
                        ]
                    },
                    borderWidth: 0,
                    outerRadius: '109%'
                }, {
                    backgroundColor: {
                        linearGradient: {x1: 0, y1: 0, x2: 0, y2: 1},
                        stops: [
                            [0, '#333'],
                            [1, '#FFF']
                        ]
                    },
                    borderWidth: 1,
                    outerRadius: '107%'
                }, {
                    // default background
                }, {
                    backgroundColor: '#DDD',
                    borderWidth: 0,
                    outerRadius: '105%',
                    innerRadius: '103%'
                }]
            },

            // the value axis
            yAxis: {
                min: 10,
                max: 1100,

                minorTickInterval: 'auto',
                minorTickWidth: 1,
                minorTickLength: 10,
                minorTickPosition: 'inside',
                minorTickColor: '#666',

                tickPixelInterval: 30,
                tickWidth: 2,
                tickPosition: 'inside',
                tickLength: 10,
                tickColor: '#666',
                labels: {
                    step: 2,
                    rotation: 'auto'
                },
                title: {
                    text: 'rpm'
                },
                plotBands: [{
                    from: 0,
                    to: 660,
                    color: '#55BF3B' // green
                }, {
                    from: 660,
                    to: 880,
                    color: '#DDDF0D' // yellow
                }, {
                    from: 880,
                    to: 1100,
                    color: '#DF5353' // red
                }]
            },

            series: [{
                name: 'Speed',
                data: [800],
                tooltip: {
                    valueSuffix: ' rpm'
                }
            }]

        },
        // Add some life
        function (chart) {
            if (!chart.renderer.forExport) {
                setInterval(function () {
                    var point = chart.series[0].points[0],
                        newVal,
                        inc = Math.round((Math.random() - 0.5) * 200);

                    newVal = point.y + inc;
                    if (newVal < 0 || newVal > 1100) {
                        newVal = point.y - inc;
                    }

                    point.update(newVal);

                }, 3000);
            }
        });
});