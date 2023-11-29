
    pip install -r requirements/development.txt

    python manage.py migrate
    python manage.py runserver

Credenciales recomendadas `admin / changeme`.

# Tabla de usuarios

| Username    | Password   | Superuser | Groups     | Preferred language | Timezone      | Active |
| ----------- | ---------- | --------- | ---------- | ------------------ | ------------- | ------ |
| `admin`     | `changeme` | Yes       | None       | undefined          | undefined     | Yes    |
| `editor`    | `changeme` | No        | Editors    | undefined          | undefined     | Yes    |
| `moderator` | `changeme` | No        | Moderators | undefined          | undefined     | Yes    |
| `inactive`  | `changeme` | yes       | None       | undefined          | undefined     | No     |
| `german`    | `changeme` | yes       | None       | German             | Europe/Berlin | Yes    |
| `arabic`    | `changeme` | yes       | None       | Arabic             | Asia/Beirut   | Yes    |
