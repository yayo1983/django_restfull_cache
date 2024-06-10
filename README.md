## Crear super usuario por comando

python manage.py createsuperuser

## Subir proyecto a Github

git init
git add .
git commit -m "Primer commit"
git remote add origin https://github.com/yayo1983/django_restfull_cache.git
git push -u origin main


## Ejecutar las pruebas
python manage.py test


## Registrar usuario

curl -X POST http://localhost:8000/api/auth/registration/ \
-H "Content-Type: application/json" \
-d '{"username": "nuevo_usuario", "password1": "password123", "password2": "password123", "email": "usuario@example.com"}'

## Iniciar usuario
curl -X POST http://localhost:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"username": "nuevo_usuario", "password": "password123"}'

## Acceso al endpoint protegido de artículos:
curl -X GET http://localhost:8000/api/articulos/ \
-H "Authorization: Token <tu_token_aqui>"

## Crear un nuevo artículo:
curl -X POST http://localhost:8000/api/articulos/ \
-H "Authorization: Token <tu_token_aqui>" \
-H "Content-Type: application/json" \
-d '{"titulo": "Nuevo Artículo", "descripcion": "Descripción del nuevo artículo"}'
