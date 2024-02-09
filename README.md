# README

This README would normally document whatever steps are necessary to get the
application up and running
* ...
Based on your history file, here are the installation commands and steps you followed:

1. Update package repository:
   ```bash
   sudo apt update
   ```

2. Install Ruby:
   ```bash
   sudo apt install ruby -y
   ```

3. Install Ruby on Rails:
   ```bash
   sudo apt install ruby-railties
   ```

4. Create a new Rails application:
   ```bash
   rails new sample_app
   ```

5. Navigate to the sample app directory:
   ```bash
   cd sample_app/
   ```

6. Generate a controller:
   ```bash
   rails generate controller welcome index
   ```

7. Install Bundler:
   ```bash
   sudo apt install ruby-bundler 
   ```

8. Install Ruby development headers:
   ```bash
   sudo apt install ruby-dev
   ```

9. Install essential build tools:
   ```bash
   sudo apt-get install build-essential
   ```

10. Install Node.js:
    ```bash
    sudo apt install nodejs
    ```

11. Install npm:
    ```bash
    sudo apt install npm
    ```

12. Install Yarn:
    ```bash
    npm install -g yarn
    ```

13. Set npm global install directory:
    ```bash
    mkdir ~/.npm-global
    npm config set prefix '~/.npm-global'
    export PATH=~/.npm-global/bin:$PATH
    ```

14. web packager install :
    ```bash
    rails webpacker:install
    ```

Now, you can proceed with running the Rails server:
```bash
rails server -b 0.0.0.0 -p 3000
```

This should start your Rails application server and make it accessible on all network interfaces on port 3000.
