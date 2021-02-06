<?php 
$zaman=strtotime('now');



if ($zaman>=strtotime("06:00") && $zaman<strtotime("10:00")) {
	echo "Günaydın";
}
elseif ($zaman>=strtotime("10:00") && $zaman<strtotime("17:00")) {
	echo "İyi Günler";
}
elseif ($zaman>=strtotime("17:00") && $zaman<strtotime("20:00")) {
	echo "İyi Akşamlar";
}
elseif ($zaman>=strtotime("20:00") && $zaman<strtotime("00:00")) {
	echo "İyi Geceler";
}
else{
	echo "Esenlikler Dilerim";
}

?>