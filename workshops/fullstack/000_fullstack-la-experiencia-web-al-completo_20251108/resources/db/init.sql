USE app_db;

-- Usuarios
CREATE TABLE users (
    id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    email         VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Publicaciones (posts)
CREATE TABLE posts (
    id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id       INT UNSIGNED NOT NULL,
    title         VARCHAR(150) NOT NULL,
    body          TEXT NOT NULL,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Comentarios
CREATE TABLE comments (
    id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    post_id       INT UNSIGNED NOT NULL,
    user_id       INT UNSIGNED NOT NULL,
    content       TEXT NOT NULL,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Datos iniciales para pruebas

INSERT INTO users (name, email, password_hash) VALUES
('Alice', 'alice@gmail.com', 'hash_alice'),
('Bob',   'bob@gmail.com',   'hash_bob'),
('Carol', 'carol@gmail.com', 'hash_carol');

INSERT INTO posts (user_id, title, body) VALUES
(1, 'Primer post del taller', 'Este es un ejemplo de post para probar la API.'),
(2, 'Hola desde el backend',  'Otra entrada de prueba para las rutas de listado.'),
(1, 'Ideas de proyecto',      'Pensando en hacer una mini SPA con Vue.');

INSERT INTO comments (post_id, user_id, content) VALUES
(1, 2, 'Buen ejemplo, ya veo cómo funciona el GET.'),
(1, 3, '¿Podemos añadir paginación luego?'),
(2, 1, 'Confirmo que esto se ve bien desde el frontend.');
