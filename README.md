Business Value: "A fault-tolerant, microservices-based architecture ensuring zero direct database exposure to the public internet."

Build this locally on your machine using Docker Desktop

How to run: docker-compose up -d.

URL: http://localhost

What happens: You hit the Nginx container. Nginx creates a reverse proxy connection to the Flask container, which queries Redis, gets the count, and sends the HTML back to you.

What you should see:

Hello World! I have been seen 1 times. (Refresh the page, and the number should increment: 2, 3, 4...)