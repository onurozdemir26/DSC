<!DOCTYPE html>
<html>
<head>
	<title>Asal Sayı Bulma</title>
</head>
<body>
<form action="" method="POST">
	Sayı: <input type="text" name="sayi">   
	<input type="submit" name="Kontrol ET">
</form>
</body>
</html>



<?php
$sayi=$_POST['sayi'];
$asal=0; $i=2;
do
{ 
	if ($sayi % $i == 0)
	{
		
		$asal = 1;
	}
	$i++;
}
while($i<$sayi);
if ($sayi==2) {
	echo "Sayı Asaldır";
}
elseif ($asal != 1)
{
	echo "Sayı Asaldır";
}
else
{
	echo "Sayı Asal Değildir";
}
 
?>

