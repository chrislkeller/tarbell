var jqueryNoConflict = jQuery;

// begin main function
jqueryNoConflict(document).ready(function() {
    var charts = [new Highcharts.Chart(createChart())];
});

    function createChart() {

        var config = {};

        config.chart = {
            renderTo: optionsConfig.renderToContainer,
            type: 'bar',
        };

        config.title = {
            text: optionsConfig.title,
        };

        config.subtitle = {
            text: optionsConfig.subtitle,
        };

        config.xAxis = {
            categories: optionsConfig.categories,
            title: {
                text: null
            }
        };

        config.yAxis = {
            title: {
                text: null
            }
        };

        config.stackLabels = {
            enabled: false,
            align: 'left',
            x: 25,
            style: {
                fontSize: '14px',
                lineHeight: '16px',
                fontWeight: 'bold',
                color: (Highcharts.theme && Highcharts.theme.textColor) || '#ffffff'
            },
            formatter: function() {
                return 'Overall total: ' + Highcharts.numberFormat(this.total, 0, ',');
            }
        };

        config.tooltip = {
            formatter: function() {
                return Highcharts.numberFormat(this.y, 0, ',');
            }
        };

        config.legend = {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            x: 10,
            y: 0,
            floating: false,
            borderWidth: 1,
            backgroundColor: '#FFFFFF',
            shadow: true,
            reversed: true,
            margin: 30
        };

        config.credits = {
            enabled: true,
            text: optionsConfig.credits
        };

        //config.plotOptions = {
            //series: {
                //stacking: 'normal',
            //}
        //};

        config.series = optionsConfig.dataSeries;

        return config;
    }