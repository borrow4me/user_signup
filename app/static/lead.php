<?php
	$sender_name = $_POST['name'];
	$sender_email = $_POST['email'];
	$phone = $_POST['phone'];
	$city = $_POST['city'];
	$input_zip_code = $_POST['zip_code'];
	$input_loan_type = $_POST['loan_type'];
	$amount = $_POST['amount'];
	
	$body = $sender_name." sent a new message for you<br><br> Name: ".$sender_name."<br>Email: ".$sender_email."<br>Phone: ".$phone."<br>City: ".$city."<br>Zip Code: ".$input_zip_code."<br>Loan Type: ".$input_loan_type."<br>Amount: ".$amount;
	
	sendMail($sender_name , $sender_email, $body);
	
	function sendMail($sender, $sender_mail, $body) {
		$to = 'receiver@domain.com'; // Set Receiver Email Here
		$myemail = 'sender@domain.com'; // Set Sender Email Here
		$subject = "New EasyLoan Client"; // Set Subject Here
		$headers = "MIME-Version: 1.0\r\n";
		$headers .= "Content-type: text/html; charset=iso-8859-1\r\n";            
		$headers .= "From: EasyLoan <sender@domain.com>\r\n"; // Set Header Here
		
		$message = $body;
		
		$sentmail = mail($to,$subject,$message,$headers);
		if($sentmail) { echo "Request submitted successfully. We will contact with you very soon."; }
		else { echo "Mail not sent"; }
	}

?>