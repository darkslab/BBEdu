<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>bbTest.kz &mdash; Самая простая и удобная платформа онлайн тестирования</title>

    <meta name="description" content="bbTest.kz &mdash; Самая простая и удобная платформа онлайн тестирования. Уже скоро...">

    <link href="bootstrap.min.css" rel="stylesheet">
    <link href="style.css?v=3" rel="stylesheet">
    <link href="font-awesome.min.css" rel="stylesheet">

    <script src="jquery-3.2.1.min.js"></script>
    <script src="bootstrap.min.js"></script>
    <?php if (file_exists(dirname(__FILE__).'/../.bbtest_production')): ?>
        <script>
          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

          ga('create', 'UA-105806399-1', 'auto');
          ga('send', 'pageview');

        </script>
    <?php endif ?>
    <script>
        $(function() {
            var $xhr = null;
            $("[data-subscribe-button]").click(function() {
                var $button = $(this);
                var email = $("[data-subscribe-input]").val();

                $button.attr("disabled", true);
                if ($xhr) {
                    $xhr.abort();
                }

                $xhr = $.post("/subscribe.php", {
                    email: email
                }, function(response) {
                    if (response.success) {
                        $("#subscribe").modal("hide");
                        $button.attr("disabled", false);
                        return;
                    }
                    $("[data-subscribe-container]").addClass("has-error");
                    $("[data-subscribe-error]").removeClass("hidden");
                }, "json");
            });
            $("[data-subscribe-input]").keypress(function() {
                $("[data-subscribe-container]").removeClass("has-error");
                $("[data-subscribe-error]").addClass("hidden");
                $("[data-subscribe-button]").attr("disabled", false);
            });
        });
    </script>
</head>
<body class="splash-body">
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                <img src="logo.png" class="img-responsive center-block splash-title-first">
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                <h4 class="text-center splash-title mt-0 mb-30">&quot;Самая простая и удобная платформа онлайн тестирования.&quot;</h4>
                <h4 class="text-center splash-title mt-0 mb-30">&quot;Качественные тесты, расширенные результаты, индивидуальный подход к каждому.&quot;</h4>
                <h4 class="text-right splash-title mt-0 mb-30">уже скоро...</h4>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                <h5 class="text-center mt-0 mb-30">
                    <a href="#subscribe" class="btn btn-default btn-lg" data-toggle="modal">Когда заработает сайт?</a>
                </h5>
                <div class="modal fade" id="subscribe">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                            </div>
                            <div class="modal-body">
                                <h4 class="modal-title text-center mb-30" style="line-height: 1;">Оставьте нам свой емайл и Вы первым узнаете когда сайт будет запущен.</h4>
                                <div class="form-group" data-subscribe-container>
                                    <label class="control-label hidden" data-subscribe-error>Проверьте правильность емайла</label>
                                    <div class="input-group">
                                        <input type="text" class="form-control input-lg" placeholder="Емайл" data-subscribe-input>
                                        <span class="input-group-btn">
                                            <button class="btn btn-primary" type="button" data-subscribe-button>Отправить</button>
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">Закрыть</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mb-30">
            <div class="col-xs-12 col-sm-6 col-sm-offset-3 col-md-4 col-md-offset-4">
                <div class="row mb-30">
                    <div class="col-xs-4">
                        <h3 class="text-center">
                            <a target="_blank" href="https://www.facebook.com/bbtest.kz" class="splash-title splash-social splash-social-facebook"><i class="fa fa-fw fa-facebook"></i></a>
                        </h3>
                    </div>
                    <div class="col-xs-4">
                        <h3 class="text-center">
                            <a target="_blank" href="https://www.instagram.com/bbtest.kz/" class="splash-title splash-social splash-social-instagram"><i class="fa fa-fw fa-instagram"></i></a>
                        </h3>
                    </div>
                    <div class="col-xs-4">
                        <h3 class="text-center">
                            <a target="_blank" href="https://twitter.com/bbtest_kz" class="splash-title splash-social splash-social-twitter"><i class="fa fa-fw fa-twitter"></i></a>
                        </h3>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
