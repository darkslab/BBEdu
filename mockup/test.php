<script src="js/jquery-ui.min.js"></script>
<script src="js/SVGChart.js"></script>
<script src="js/RadialChart.js"></script>
<script src="js/ColumnChart.js"></script>
<script src="js/ProgressPieChart.js"></script>
<script>
    $(function() {
        (new ProgressPieChart($("[data-monkey]"), [
            {
                "max-value": 200,
                "value": 150,
                "foreground-color": "#f00",
                "background-color": "#888"
            },
            {
                "max-value": 200,
                "value": 50,
                "foreground-color": "#0f0",
                "background-color": "#888"
            },
            {
                "max-value": 200,
                "value": 100,
                "foreground-color": "#00f",
                "background-color": "#888"
            }
        ], {
            // "font-size": 20,
            // "font-weight": "bold",
            // "font-color": "#000"
        })).create();
    });
</script>
<div class="row">
    <div class="col-xs-12">
        <div style="border: 1px solid #000; height: 502px; width: 502px; position: relative;" data-monkey></div>
        <div style="border: 1px solid #000; height: 502px; width: 502px; position: relative;">
            <svg width="100%" height="100%">
                <g transform="translate(250,250) rotate(-90)">
                    <g transform="translate(0,0)">
                    <!-- <g transform="translate(35.355339059327376,35.355339059327376)"> -->
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 0 200
                                 L0 0
                                 Z" fill="#ccc"></path>
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 141.421356237309505 141.421356237309505
                                 L0 0
                                 Z" fill="#3366cc"></path>
                        <g transform="rotate(90 106.066017177982129 106.066017177982129)">
                            <text x="106.066017177982129" y="106.066017177982129" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                        </g>
                    </g>
                </g>
                <g transform="translate(250,250) rotate(0)">
                    <!-- <g transform="translate(0,0)"> -->
                    <g transform="translate(46.193976625564338,19.134171618254489)">
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 141.421356237309505 141.421356237309505
                                 L0 0
                                 Z" fill="#ccc"></path>
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 184.775906502257351 76.536686473017954
                                 L0 0
                                 Z" fill="#dc3912"></path>
                        <g transform="rotate(0 138.581929876693013 57.402514854763466)">
                            <text x="138.581929876693013" y="57.402514854763466" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                        </g>
                    </g>
                </g>
                <g transform="translate(250,250) rotate(45)">
                    <g transform="translate(0,0)">
                    <!-- <g transform="translate(43.301270189221932,25)"> -->
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 100 173.205080756887729
                                 L0 0
                                 Z" fill="#ccc"></path>
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 173.205080756887729 100
                                 L0 0
                                 Z" fill="#ff9900"></path>
                        <g transform="rotate(-45 129.903810567665797 75)">
                            <text x="129.903810567665797" y="75" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                        </g>
                    </g>
                </g>
                <g transform="translate(250,250) rotate(105)">
                    <g transform="translate(0,0)">
                    <!-- <g transform="translate(48.296291314453414,12.940952255126038)"> -->
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 173.205080756887729 100
                                 L0 0
                                 Z" fill="#ccc"></path>
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 193.185165257813657 51.763809020504152
                                 L0 0
                                 Z" fill="#109618"></path>
                        <g transform="rotate(-105 144.888873943360243 38.822856765378114)">
                            <text x="144.888873943360243" y="38.822856765378114" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                        </g>
                    </g>
                </g>
                <g transform="translate(250,250) rotate(135)">
                    <g transform="translate(0,0)">
                    <!-- <g transform="translate(19.134171618254489,46.193976625564338)"> -->
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 -141.421356237309505 141.421356237309505
                                 L0 0
                                 Z" fill="#ccc"></path>
                        <path d="M0 0
                                 L200 0
                                 A200 200 0 0 1 76.536686473017954 184.775906502257351
                                 L0 0
                                 Z" fill="#990099"></path>
                        <g transform="rotate(-135 57.402514854763466 138.581929876693013)">
                            <text x="57.402514854763466" y="138.581929876693013" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                        </g>
                    </g>
                </g>
                <!-- <g transform="translate(250,250)">
                    <circle cx="0" cy="0" r="250" stroke="#000" stroke-width="1" fill="none"></circle>
                </g> -->
            </svg>
        </div>
        <div style="border: 1px solid #000; height: 502px; width: 502px; position: relative;">
            <svg width="100%" height="100%">
                <g transform="translate(250,250)">
                    <g transform="rotate(-90)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(35.355339059327376,35.355339059327376)"> -->
                            <path d="M0 0
                                     L200 0
                                     A200 200 0 0 1 0 200
                                     L0 0
                                     Z" fill="#c8c8c8"></path>
                        </g>
                    </g>
                    <g transform="rotate(0)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(46.193976625564338,19.134171618254489)"> -->
                            <path d="M0 0
                                     L200 0
                                     A200 200 0 0 1 141.421356237309505 141.421356237309505
                                     L0 0
                                     Z" fill="#bebebe"></path>
                        </g>
                    </g>
                    <g transform="rotate(45)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(43.301270189221932,25)"> -->
                            <path d="M0 0
                                     L200 0
                                     A200 200 0 0 1 100 173.205080756887729
                                     L0 0
                                     Z" fill="#b4b4b4"></path>
                        </g>
                    </g>
                    <g transform="rotate(105)">
                        <!-- <g transform="translate(0,0)"> -->
                        <g transform="translate(48.296291314453414,12.940952255126038)">
                            <path d="M0 0
                                     L200 0
                                     A200 200 0 0 1 173.205080756887729 100
                                     L0 0
                                     Z" fill="#c8c8c8"></path>
                        </g>
                    </g>
                    <g transform="rotate(135)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(19.134171618254489,46.193976625564338)"> -->
                            <path d="M0 0
                                     L200 0
                                     A200 200 0 0 1 -141.421356237309505 141.421356237309505
                                     L0 0
                                     Z" fill="#bebebe"></path>
                        </g>
                    </g>
                </g>

                <g transform="translate(250,250)">
                    <g transform="rotate(-90)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(35.355339059327376,35.355339059327376)"> -->
                            <path d="M0 0
                                     L80 0
                                     A80 80 0 0 1 0 80
                                     L0 0
                                     Z" fill="#3366cc"></path>
                            <g transform="rotate(90 106.066017177982129 106.066017177982129)">
                                <text x="106.066017177982129" y="106.066017177982129" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                            </g>
                        </g>
                    </g>
                    <g transform="rotate(0)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(46.193976625564338,19.134171618254489)"> -->
                            <path d="M0 0
                                     L40 0
                                     A40 40 0 0 1 28.284271247461901 28.284271247461901
                                     L0 0
                                     Z" fill="#dc3912"></path>
                            <g transform="rotate(0 138.581929876693013 57.402514854763466)">
                                <text x="138.581929876693013" y="57.402514854763466" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                            </g>
                        </g>
                    </g>
                    <g transform="rotate(45)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(43.301270189221932,25)"> -->
                            <path d="M0 0
                                     L200 0
                                     A200 200 0 0 1 100 173.205080756887729
                                     L0 0
                                     Z" fill="#ff9900"></path>
                            <g transform="rotate(-45 129.903810567665797 75)">
                                <text x="129.903810567665797" y="75" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                            </g>
                        </g>
                    </g>
                    <g transform="rotate(105)">
                        <!-- <g transform="translate(0,0)"> -->
                        <g transform="translate(48.296291314453414,12.940952255126038)">
                            <path d="M0 0
                                     L120 0
                                     A120 120 0 0 1 103.923048454132638 60
                                     L0 0
                                     Z" fill="#109618"></path>
                            <g transform="rotate(-105 144.888873943360243 38.822856765378114)">
                                <text x="144.888873943360243" y="38.822856765378114" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                            </g>
                        </g>
                    </g>
                    <g transform="rotate(135)">
                        <g transform="translate(0,0)">
                        <!-- <g transform="translate(19.134171618254489,46.193976625564338)"> -->
                            <path d="M0 0
                                     L160 0
                                     A160 160 0 0 1 -113.137084989847604 113.137084989847604
                                     L0 0
                                     Z" fill="#990099"></path>
                            <g transform="rotate(-135 57.402514854763466 138.581929876693013)">
                                <text x="57.402514854763466" y="138.581929876693013" text-anchor="middle" dominant-baseline="central" font-size="24" font-weight="bold" fill="#fff">400</text>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- <g transform="translate(250,250)">
                    <circle cx="0" cy="0" r="250" stroke="#000" stroke-width="1" fill="none"></circle>
                </g> -->
            </svg>
        </div>
    </div>
</div>
