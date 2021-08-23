	<?php
		$sender_name = $_POST['InputName'];
		$sender_email = $_POST['InputEmail'];
		$phone = $_POST['InputPhone'];
		$input_zip_code = $_POST['InputZipCode'];
		$mail_body = $_POST['InputMessage'];
		
		$body = $sender_name." sent a new message for you<br><br> Name: ".$sender_name."<br>Email: ".$sender_email."<br>Phone: ".$phone."<br>Zip Code: ".$input_zip_code."<br>Message: ".$mail_body;
		
		sendMail($sender_name , $sender_email, $body);
		
		function sendMail($sender, $sender_mail, $body) {
			$to = 'eliskafilat10@gmail.com'; // Receiver
			$myemail = 'eliskafilat10@gmail.com'; // Sender
			$subject = "New borrow4me Client";
			$headers = "MIME-Version: 1.0\r\n";
			$headers .= "Content-type: text/html; charset=iso-8859-1\r\n";            
			$headers .= "From:  <info@onushorit.com>\r\n";
			
			$message = $body;
			
			$sentmail = mail($to,$subject,$message,$headers);
			if($sentmail) { echo "Request submitted successfully. We will contact with you very soon."; }
			else { echo "Mail not sent"; }
		}

	?>