<?php
	require_once('./connect.inc.php');
	$q = mysqli_query($con,"SELECT `short_name`, `available` FROM `companies`");
?>
		<tr>
			<th>
				Company
			</th>
			<th>
				Slots
			</th>
		</tr>
<?php
	while ($row = mysqli_fetch_array($q,MYSQLI_NUM)) {
		$cn = $row[0];
		$cnt = $row[1];
		if($cnt <= 0)
			echo "		<tr class=\"danger\">";
		else if($cnt <= 10)
			echo "		<tr class=\"warning\">";
		else
			echo "		<tr>";

		$outval = <<<END
			<td>
				$cn
			</td>
			<td>
				$cnt
			</td>
		</tr>\n
END;
		print($outval);
	}
?>