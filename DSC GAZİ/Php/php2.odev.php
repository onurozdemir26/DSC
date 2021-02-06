<!DOCTYPE html>
<html>
<head>
   <title></title>
</head>
<body>
<form action="" method="get">
   Sayı: <input type="text" name="sayi">
   <input type="submit" name="Kontrol Et">
</form>
</body>
</html>

<?php

function MukemmelSayi($sayi) {
   if(!is_numeric($sayi)) {
      echo "<script>alert('Lütfen Bir Sayı Girin')</script>"; 
      return false;
   }
   for($a=1; $a<$sayi; $a++) {
      $sonuc = $sayi%$a;
      if($sonuc==0) {
         $dizi[]=$a;
      }
   }
   if(array_sum($dizi)==$sayi) {
		echo "<script>alert(' Bir Mükemmel Sayı!')</script>";
        
   }
   else {
      echo "<script>alert(' Bir Mükemmel Sayı Değil!')</script>";
   }
}


if(isset($_GET['sayi'])) 
{
$kontrol = $_GET['sayi'];
MukemmelSayi($kontrol);


}
?>