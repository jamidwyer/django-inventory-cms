#!/bin/bash

source .env

# Backup destination
BACKUP_FILE="$BACKUP_DIR/backup_$(date +%Y%m%d%H%M%S).sql"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Export password so pg_dump can use it
export PGPASSWORD="$DB_PASSWORD"

# Run the pg_dump command to backup the database
ssh root@$SERVER_IP docker exec -u "$DB_USER" hord_db pg_dump -Fc "$DB_NAME" > "$BACKUP_FILE"

gzip "$BACKUP_FILE"

# Log the backup result
echo "Backup completed: $(date)" >> $BACKUP_DIR/backup_log.txt
