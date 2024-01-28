<!DOCTYPE html>
<html>
<head>
<title>METANIT.COM</title>
<meta charset="utf-8" />
</head>
<body>
<h2>Список пользователей</h2>
<?php
$conn = mysqli_connect("localhost", "root", "mypassword", "testdb3");
if (!$conn) {
die("Ошибка: " . mysqli_connect_error());
}
$sql = "SELECT * FROM Users";
if($result = mysqli_query($conn, $sql)){
$rowsCount = mysqli_num_rows($result); // количество полученных строк
echo "<p>Получено объектов: $rowsCount</p>";
echo "<table><tr><th>Id</th><th>Имя</th><th>Возраст</th></tr>";
foreach($result as $row){
echo "<tr>";
echo "<td>" . $row["id"] . "</td>";
echo "<td>" . $row["name"] . "</td>";
echo "<td>" . $row["age"] . "</td>";
echo "</tr>";
}
echo "</table>";
mysqli_free_result($result);
} else{
echo "Ошибка: " . mysqli_error($conn);
}
mysqli_close($conn);
?>
</body>
</html>