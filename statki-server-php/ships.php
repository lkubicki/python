<?php
$forbidden = array(".", "/", "\\");
if(isset($_GET['gameId'])) {
	$gameId = str_replace($forbidden, "_", $_GET['gameId']);
	$line = '';

	error_reporting(0);
	$file = fopen('data/'.$gameId.'.csv', 'r');
	error_reporting(E_ALL);
	if($file) {
		$cursor = -1;

		do {
			fseek($file, $cursor--, SEEK_END);
			$char = fgetc($file);
		} while ($char === "\n" || $char === "\r");

		while ($char !== false && $char !== "\n" && $char !== "\r") {
			$line = $char . $line;
			fseek($file, $cursor--, SEEK_END);
			$char = fgetc($file);
		}

		fclose($file);
	} else {
                $line = 'FAIL';
        }

	print $line;
}
?>