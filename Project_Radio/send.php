<?php
$message = $_POST[msg];
$name = $_POST[name];
$file = fopen("chat.txt", "a+");
fputs($file, "<strong>$name<strong> </br> $message");
fclose($file);
?>