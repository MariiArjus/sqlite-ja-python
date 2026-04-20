<?php include 'config.php'; ?>
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Autode müügiportaal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .car-card img { height: 200px; object-fit: cover; }
        body { background-color: #f8f9fa; }
    </style>
</head>
<body>

<nav class="navbar navbar-dark bg-dark mb-4">
    <div class="container">
        <span class="navbar-brand mb-0 h1">Autode nimekiri</span>
    </div>
</nav>

<div class="container">
    <div class="row">
        <?php
        $stmt = $pdo->query("SELECT * FROM autod");
        while ($row = $stmt->fetch()) {
            echo '
            <div class="col-md-4 mb-4">
                <div class="card car-card shadow-sm">
                    <img src="img/' . $row['image'] . '" class="card-img-top" alt="' . $row['brand'] . '">
                    <div class="card-body">
                        <h5 class="card-title">' . $row['brand'] . ' ' . $row['model'] . '</h5>
                        <p class="card-text text-muted">Aasta: ' . $row['aasta'] . '</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="badge bg-success fs-5">' . $row['price'] . ' €</span>
                            <div class="btn-group">
                                <button type="button" class="btn btn-sm btn-outline-secondary">Vaata</button>
                                <button type="button" class="btn btn-sm btn-outline-primary">Osta</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>';
        }
        ?>
    </div>
</div>

</body>
</html>