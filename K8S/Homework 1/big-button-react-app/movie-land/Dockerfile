# Create a new build stage from a base image
FROM node:16.20.2-alpine3.18

# Change working directory
WORKDIR /app

# Copy files and directories
COPY package*.json ./
# Execute build commands
RUN npm i

# Copy files and directories
COPY public public
COPY src src

# Describe which ports your application is listening on
EXPOSE 3000

# Specify default commands
CMD ["npm", "start"]