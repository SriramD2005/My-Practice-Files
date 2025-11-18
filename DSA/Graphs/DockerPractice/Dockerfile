# Use OpenJDK 19 base image
FROM openjdk:19-slim

# Install Kotlin compiler
RUN apt-get update && \
    apt-get install -y curl unzip zip gnupg && \
    curl -s https://get.sdkman.io | bash && \
    bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install kotlin"

# Set working directory
WORKDIR /app

# Copy Kotlin file
COPY main.kt .

# Compile Kotlin file
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && kotlinc main.kt -include-runtime -d hello.jar"

# Run the Kotlin app
CMD ["java", "-jar", "hello.jar"]
