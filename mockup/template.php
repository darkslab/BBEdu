<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title></title>

    <meta name="description" content="">

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/style.css?v=8" rel="stylesheet">

    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script>
        $(function() {
            var min_height = 600;
            var $main = $("[data-bb-main]");
            $main.css({
                "min-height": ($(window).height() > min_height ? $(window).height() : min_height) + "px"
            });
            $(window).resize(function() {
                if ($(this).height() > min_height) {
                    $main.css({
                        "min-height": $(this).height() + "px"
                    });
                }
            });
            $("[data-bb-bar-button]").click(function() {
                if ($(window).width() < 1200) {
                    var $button = $(this);
                    if ($button.hasClass("bb-pushed")) {
                        $button.removeClass("bb-pushed");
                        $main.removeClass("bb-pushed");
                    } else {
                        $button.addClass("bb-pushed");
                        $main.addClass("bb-pushed");
                    }
                }
            });
        });
    </script>
</head>
<body>
    <div class="bb-container bb-container-student">
        <div class="bb-menu text-bright text-shadowed">
            <div class="container-fluid">
                <div class="row bb-menu-section bb-menu-section-first pt-15 pb-15">
                    <a href="<?php echo $base; ?>" class="col-xs-12">
                        <img class="img-responsive bb-menu-logo" src="img/logo.png" alt="bbTest.kz Logo" title="bbTest.kz">
                    </a>
                </div>
                <div class="row bb-menu-section pt-15 pb-15">
                    <div class="col-xs-8 col-xs-offset-2">
                        <img class="img-responsive img-circle bb-menu-gravatar" src="img/gravatar2.jpg" alt="Мейрбекова Анара" title="Мейрбекова Анара">
                    </div>
                    <h5 class="col-xs-12 text-center text-bright mt-5 mb-0">Мейрбекова Анара</h5>
                    <!-- <h5 class="col-xs-12 text-center text-bright mt-5 mb-5"><span class="label label-danger">Администратор</span></h5> -->
                    <div class="col-xs-12 text-center mt-5 mb-5">
                        <a href="<?php echo $base; ?>payment.html" class="btn btn-success btn-xs">Счёт: 0 ₸</a>
                    </div>
                </div>
                <div class="row bb-menu-section bb-menu-section-last pt-15 pb-15">
                    <ul class="nav nav-pills nav-stacked col-xs-12 pr-0">
                        <li class="<?php echo $nav == 'dashboard' ? 'active' : ''; ?>"><a href="<?php echo $base; ?>dashboard.html"><i class="fa fa-fw fa-tachometer"></i> Личный кабинет</a></li>
                        <li class="<?php echo $nav == 'test' ? 'active' : ''; ?>"><a href="<?php echo $base; ?>test.html"><i class="fa fa-fw fa-pencil-square-o"></i> Онлайн тестирование</a></li>
                        <li class="<?php echo $nav == 'payment' ? 'active' : ''; ?>"><a href="<?php echo $base; ?>payment.html"><i class="fa fa-fw fa-credit-card"></i> Пополнить счёт</a></li>
                    </ul>
                </div>
                <div class="row bb-menu-section bb-menu-section-final pt-15 pb-15 visible-xs-block">
                    <ul class="nav nav-pills nav-stacked col-xs-12 pr-0">
                        <li class="<?php echo $nav == 'settings' ? 'active' : ''; ?>"><a href="<?php echo $base; ?>settings.html"><i class="fa fa-fw fa-sliders"></i> Настройки</a></li>
                        <li class="<?php echo $nav == 'logout' ? 'active' : ''; ?>"><a href="<?php echo $base; ?>logout.html"><i class="fa fa-fw fa-sign-out"></i> Выход</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="bb-main" data-bb-main>
            <div class="container-fluid">
                <div class="row bb-bar">
                    <nav class="navbar navbar-inverse">
                        <div class="container-fluid">
                            <div class="navbar-header">
                                <button type="button" class="navbar-toggle mr-0" data-bb-bar-button>
                                    <span class="icon-bar bb-bar-button-first"></span>
                                    <span class="icon-bar bb-bar-button-second"></span>
                                    <span class="icon-bar bb-bar-button-third"></span>
                                </button>
                                <a class="navbar-brand ml-0 pt-10 pb-10 pl-5" href="<?php echo $base; ?>">
                                    <img class="bb-bar-logo" src="img/logo.png" alt="bbTest.kz Logo" title="bbTest.kz">
                                </a>
                            </div>
                            <div class="navbar-collapse collapse" style="height: 1px;">
                                <ul class="nav navbar-nav navbar-right">
                                    <li class="bb-bar-gravatar-container"><img class="img-responsive img-circle bb-bar-gravatar mt-10 mb-10 mr-5 ml-5" src="img/gravatar2.jpg" alt="Мейрбекова Анара" title="Мейрбекова Анара"></li>
                                    <li class="dropdown">
                                        <a href="javascript: void(0);" class="dropdown-toggle" data-toggle="dropdown">Мейрбекова Анара <span class="caret"></span></a>
                                        <ul class="dropdown-menu dropdown-menu-right">
                                            <li><a href="<?php echo $base; ?>dashboard.html"><i class="fa fa-fw fa-tachometer"></i> Личный кабинет</a></li>
                                            <li><a href="<?php echo $base; ?>settings.html"><i class="fa fa-fw fa-sliders"></i> Настройки</a></li>
                                            <li class="divider"></li>
                                            <li><a href="<?php echo $base; ?>logout.html"><i class="fa fa-fw fa-sign-out"></i> Выход</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </nav>
                </div>
                <div class="row">
                    <div class="container bb-content">

                        <!-- Main content start -->
                        <?php echo $content; ?>
                        <!-- Main content end -->

                    </div>
                </div>
            </div>
            <div class="bb-copyright text-center">Сделано с <i class="fa fa-heart-o"></i> в Казахстане. &copy; bbTest.kz</div>
        </div>
    </div>
</body>
</html>
