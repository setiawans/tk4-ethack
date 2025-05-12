# Use official Node.js image
FROM node:18-alpine

# Set working directory inside container
WORKDIR /app

# Copy package.json and package-lock.json from the correct location
COPY ./src/package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy the rest of the application files
COPY ./src . 

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]