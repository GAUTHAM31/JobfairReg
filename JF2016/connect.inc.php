<?php
	$dbhost = "localhost";
	$dbuser = "reg";
	$dbpass = "gautham3131";
	$dbname = "jobFair_DB";

	$conn_error = "Could Not Connect!";
	$con=mysqli_connect($dbhost, $dbuser, $dbpass);

	if(!mysqli_select_db($con,$dbname))
	{
		die($conn_error);
	}
?>