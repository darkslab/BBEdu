<?php

$response = array(
    'success' => false
);

$post_email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
if ($post_email) {
    $response['success'] = true;

    $mysql = new mysqli('localhost', 'root', 'monkey', 'bbtest');
    if (!$mysql->connect_errono) {
        $mysql->set_charset('utf8');
        $mysql->query("
            INSERT INTO `bbtest`.`subscriptions` (
                `email`,
                `created_at`
            )
            VALUES (
                '".$mysql->escape_string($post_email)."',
                NOW()
            );
        ");
    }
}

echo json_encode($response);
