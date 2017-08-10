<script src="js/jquery-ui.min.js"></script>
<script src="js/SVGChart.js?v=1"></script>
<script src="js/RadialChart.js?v=1"></script>
<script src="js/ColumnChart.js?v=1"></script>
<script src="js/ProgressPieChart.js?v=4"></script>
<script>
    $(function() {
        function monkey(index) {
            console.log("started: " + index);
        }
        function shmonkey(index) {
            console.log("ended: " + index);
        }
        (new ProgressPieChart($("[data-monkey]"), [
            {
                "max-value": 90,
                "value": 36,
                "foreground-color": "#3366cc",
                "background-color": "#CCD9F1",
                "active-callback-start": monkey,
                "active-callback-complete": shmonkey
            },
            {
                "max-value": 45,
                "value": 9,
                "foreground-color": "#dc3912",
                "background-color": "#F6CDC4",
                "active-callback-start": monkey,
                "active-callback-complete": shmonkey
            },
            {
                "max-value": 60,
                "value": 60,
                "foreground-color": "#ff9900",
                "background-color": "#FFE5C0",
                "active-callback-start": monkey,
                "active-callback-complete": shmonkey
            },
            {
                "max-value": 30,
                "value": 18,
                "foreground-color": "#109618",
                "background-color": "#C3E5C6",
                "active-callback-start": monkey,
                "active-callback-complete": shmonkey
            },
            {
                "max-value": 135,
                "value": 108,
                "foreground-color": "#990099",
                "background-color": "#E5C0E4",
                "active-callback-start": monkey,
                "active-callback-complete": shmonkey
            }
        ], {
            "duration": 2000,
            "chain-duration": 0,
            "activate-duration": 150,
            "hole-radius": "30%",
            "active-radius": "5%",
            "font-size": 20,
            "font-weight": "bold",
            "font-color": "#fff"
        })).create();
    });
</script>
<div class="row">
    <div class="col-xs-12">
        <div style="border: 1px solid #000; height: 502px; width: 502px; position: relative;" data-monkey></div>
    </div>
</div>
