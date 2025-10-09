 
<?php
$pdo = new PDO("mysql:host=localhost;dbname=cyberdb;charset=utf8", "user", "password");
 
$sql = "SELECT id_incident, type_incident, date_detection, description 
        FROM Incident 
        WHERE niveau_gravite='Critique' AND statut='En cours'";
$stmt = $pdo->query($sql);
 
echo "<table>";
echo "<tr><th>ID</th><th>Type</th><th>Date</th><th>Description</th></tr>";
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    echo "<tr><td>{$row['id_incident']}</td>
              <td>{$row['type_incident']}</td>
              <td>{$row['date_detection']}</td>
              <td>{$row['description']}</td></tr>";
}
echo "</table>";
?>
