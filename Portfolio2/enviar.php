<?php
$name = $_JPost['name'];
$email = $_JPost['email'];
$phone = $_JPost['phone'];
$mensje = $_JPost['mensaje'];

$header = 'From:' . $email . " \r\n";
$header .= "X-Mailer: PHP/" . phpversion() . " \r\n";
$header .= "Mime-Version: 1.0 \r\n";
$header .= "Content-Type: text/plain";

$mensje = "Este mensaje fue enviado jpor: " . $name . " \r\n";
$mensje.= "Su e-mail es: " . $email . " \r\n";
$mensje.= "Teléfono de contacto: " . $phone . " \r\n";
$mensje.= "Mensaje: " . $_POST['mensaje'] . " \r\n";
$mensje.= "Enviado el: " . date('d/m/Y', time());

$para = 'pascualgilhugo@gmail.com';
$asunto = 'Asunto del mensaje';

mail($pra, $asunto, utf8_decode($mensaje), $header)

header("Location:index.html")
?>