<?php
	require_once('./connect.inc.php');
	$q = mysqli_query($con,"SELECT `short_name`, `available` FROM `companies`");
?>

<!DOCTYPE html>
<html>
<head>
	<title>Company Slots Availability</title>
	<script type="text/javascript" src="./js/jquery-2.2.0.min.js"></script>
    <link href="./css/bootstrap.min.css"
    rel="stylesheet">
    <script src="./js/bootstrap.min.js">
    </script>
</head>
<body>
	<table id="dataTable" class="table table-hover">
	</table>
	<script type="text/javascript">
		window.setInterval(function(){
			$.ajax('./tableUpdate.php')
				.done(function(data){
					$('#dataTable').html(data);
				});
		}, 1000);
	</script>
</body>
</html>