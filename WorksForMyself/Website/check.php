<?php
  //print_r($_POST);
  $email = $_POST['text'];
  $tel = $_POST['phone'];

  $error = ''; 

  $subject = "=?utf-8?B?".base64_encode("Заказ в 1 клик")."?=";
  $headers = "From: $email\r\nReply-to: $email\r\nContent-type: text/html;charset=utf-8\r\n";
  mail('info@dveri-optom.com', $subject, $tel, $headers);

  header('Location: index.html')
?>