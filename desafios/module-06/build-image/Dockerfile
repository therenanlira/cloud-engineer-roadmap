FROM node:18-bookworm-slim AS build
RUN apt-get update && apt-get install -y --no-install-recommends python3 build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN yarn install --frozen-lockfile
RUN yarn tsc
RUN yarn build:backend --config ../app-config.yaml

# Imagem final reduzida
FROM node:18-bookworm-slim
WORKDIR /app
COPY --from=build /app/packages/backend/dist/bundle.tar.gz .
RUN tar -xzf bundle.tar.gz && rm bundle.tar.gz
CMD ["node", "packages/backend/bin/index.js", "--config", "app-config.yaml"]
