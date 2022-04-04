<?php
$forbidden = array(".", "/", "\\");
if(isset($_POST['gameId']) && isset($_POST['player']) && isset($_POST['target'])) {
	$gameId = str_replace($forbidden, "_", $_POST['gameId']);
	$currentTime = (int) (microtime(true)*1000);
	$player = str_replace(" ","",$_POST['player']);
	$target = str_replace(" ","",$_POST['target']);

	$file=fopen('data/'.$gameId.".csv", "a");
	fwrite($file, $currentTime.",SHOT,".$player.",".$target."\n");
	fclose($file);
        print("OK");
} else {
        print("FAIL");
}
?>