# # Use a Maven image to build the application
# FROM maven:3.9.0-openjdk-17-slim AS build

# # Set the working directory in the container
# WORKDIR /app

# # Copy the pom.xml and source code into the container
# COPY pom.xml .
# COPY src ./src

# # Build the application (this will create the JAR file in the target directory)
# RUN mvn clean package -DskipTests

# # Use a lightweight JDK image to run the application
# FROM openjdk:21-jdk-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the JAR file from the previous build stage
# COPY --from=build /app/target/hello-0.0.1-SNAPSHOT.jar /app/hello-0.0.1-SNAPSHOT.jar

# # Expose the port on which the Spring Boot application will run
# EXPOSE 8080

# # Set the entry point to run the Spring Boot application
# ENTRYPOINT ["java", "-jar", "/app/hello-0.0.1-SNAPSHOT.jar"]


# Use Maven image with Java 21 installed
FROM jelastic/maven:3.9.5-openjdk-21

# Set the working directory inside the container
WORKDIR /app

# Copy the pom.xml file and download dependencies
COPY pom.xml .
# RUN mvn dependency:go-offline

# Copy the entire project source code into the container
COPY src ./src

# Build the application
RUN mvn clean install

# Expose the port that the application will run on
EXPOSE 8080

# Run the application
CMD ["java", "-jar", "target/hello-0.0.1-SNAPSHOT.jar"]
