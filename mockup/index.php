<?php

$content = '';

$base = dirname($_SERVER['SCRIPT_NAME']);
if ($base != '/') {
    $base .= '/';
}

$nav = str_replace('.html', '', basename($_SERVER['QUERY_STRING']));

if (!$nav) {
    $nav = 'home';
}
if ($nav != 'template') {
    $inc_file = __DIR__.'/'.$nav.'.php';
    if (@file_exists($inc_file)) {
        ob_start();
        include($inc_file);
        $content = ob_get_contents();
        ob_end_clean();
    }
}

include(__DIR__.'/template.php');
