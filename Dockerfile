FROM node:18

WORKDIR /app

COPY backend/package*.json ./backend/
RUN cd backend && npm install

# Salin semua file source (frontend dan backend)
COPY . .

CMD ["node", "backend/server.js"]

