<?php
error_reporting(0);
include 'config.php';

# Database Connection
$conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) or die('Database connection error.');


# Create Tables if they don't exist (Setup)
mysqli_query($conn, "CREATE TABLE IF NOT EXISTS countries (
    country VARCHAR(100) NOT NULL,
    capital VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;");

mysqli_query($conn, "CREATE TABLE IF NOT EXISTS flag (
    flag VARCHAR(25500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;");

# Insert Initial Data
mysqli_query($conn, "INSERT IGNORE INTO countries (country, capital) VALUES
    ('France', 'Paris'),
    ('Spain', 'Madrid'),
    ('Germany', 'Berlin');");
mysqli_query($conn, "TRUNCATE TABLE flag;");

mysqli_query($conn, "INSERT IGNORE INTO flag (flag) VALUES ('NDH{nadi_nta?_nchofk_f_l7o9na}');");

# Vulnerable SQL Query
$vuln = isset($_GET['vuln']) ? $_GET['vuln'] : '';

$result = mysqli_fetch_assoc(mysqli_query($conn, "SELECT capital FROM countries WHERE country='{$vuln}'"));

if ($result) {
    echo "<div class='result-box'>Capital: <strong>" . htmlspecialchars($result['capital']) . "</strong></div>";
} else {
    echo "<div class='error-box'>Not found!</div>";
}

# View Source Option
if (isset($_GET['view-source'])) {
    highlight_file(__FILE__) and die();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>warmup</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            color: #333;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            box-shadow: 0 4px 2px -2px gray;
        }

        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 30px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            font-size: 28px;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
            font-size: 16px;
        }

        input[type="submit"] {
            width: 100%;
            padding: 12px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        input[type="submit"]:hover {
            background-color: #2980b9;
        }

        .result-box, .error-box {
            text-align: center;
            font-size: 18px;
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }

        .result-box {
            background-color: #2ecc71;
            color: white;
        }

        .error-box {
            background-color: #e74c3c;
            color: white;
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: #34495e;
            color: white;
            position: fixed;
            width: 100%;
            bottom: 0;
        }

        a {
            color: #3498db;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<header>
    Bayanat :)
</header>

<div class="container">
    <h2>Find the Capital</h2>
    <form>
        <input type="text" name="vuln" placeholder="Enter country name" required>
        <input type="submit" value="Search">
    </form>
    <a href='?view-source'>View Source Code</a>
</div>

<footer>
    <p>&copy; 2025 Bayanat. All Rights Reserved.</p>
</footer>

</body>
</html>
