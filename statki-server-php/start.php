<?php
$forbidden = array(".", "/", "\\");
if(isset($_POST['gameId'])) {
	$gameId = str_replace($forbidden, "_", $_POST['gameId']);

	$file=fopen('data/'.$gameId.".csv", "w");
	fclose($file);
        print("OK");
} else {
        print("FAIL");
}
?>