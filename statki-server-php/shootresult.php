<?php
$forbidden = array(".", "/", "\\");
if(isset($_POST['gameId']) && isset($_POST['player']) && isset($_POST['result']) && isset($_POST['coordinates'])) {
	$gameId = str_replace($forbidden, "_", $_POST['gameId']);
	$currentTime = (int) (microtime(true)*1000);
	$result = str_replace(" ","",$_POST['result']);
	$player = str_replace(" ","",$_POST['player']);
	$coordinates = str_replace(" ","",$_POST['coordinates']);

	$file=fopen('data/'.$gameId.".csv", "a");
	fwrite($file, $currentTime.",".$result.",".$player.",".$coordinates."\n");
	fclose($file);
        print("OK");
} else {
        print("FAIL");
}
?>