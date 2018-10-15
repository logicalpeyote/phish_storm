<?php
$to = $_POST['to'];
$message = $_POST['message'];
$api = $_POST['api'];

$subject = $_POST['subject'];
$from = $_POST['from'];

$header = "From: " .  $from . "\r\n";
$header .= "MIME-Version: 1.0\r\n";
$header .= "Content-Type: text/html; charset=ISO-8859-1\r\n";

if($api == "YOUR_API_KEY"){

if(mail($to, $subject, $message, $header)){
    echo 'Your mail has been sent successfully.';
} else{
    echo 'Unable to send email. Please try again.';
}

}
else{

echo "NON autorizzato a utilizzare il servizio";

}
?>
