<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);

//Inside myfirstprogram.php

echo "<table border='1'>

<tr>

<th> </th>";

for ($x = 1; $x <= 100; $x++) {
  echo "<th>".$x."</th>";
}
echo "</tr>";
for ($x = 1; $x <= 100; $x++) {
  echo "<tr>";
  echo "<th>". $x ."</th>";
  for ($y = 1; $y <= 100; $y++) {
  echo "<th>".  $x*$y."</th>";
  }
  echo "</tr>";
}

?>
