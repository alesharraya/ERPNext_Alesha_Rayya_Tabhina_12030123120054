# ERPNext Docker Setup

Repositori ini telah disiapkan untuk menjalankan **ERPNext** menggunakan Docker.

## Struktur Direktori
- `docker-compose.yml`: File konfigurasi Docker Compose untuk menjalankan ERPNext stack (MariaDB, Redis Cache, Redis Queue, Frappe Backend, Webhook/SocketIO, Scheduler, Queue Workers, dan Nginx Frontend).
- `erpnext_src/`: Source code repository resmi ERPNext (`https://github.com/frappe/erpnext`).
- `.frappe_docker/`: Konfigurasi dan template dari Frappe Docker.

## Cara Menjalankan

### 1. Menjalankan ERPNext
```bash
docker compose up -d
```

### 2. Menghentikan ERPNext
```bash
docker compose down
```

### 3. Akses ERPNext di Browser
- **URL**: [http://localhost:8080](http://localhost:8080)
- **Username**: `Administrator`
- **Password**: `admin`

### 4. Melihat Log Kontainer
```bash
docker compose logs -f
```
