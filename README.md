# Product Management Service

This is a Django backend for a simple e-commerce platform. It provides APIs for product management and product reviews, allowing users to manage products and submit reviews for products.

## Features

- Product Management:

  - Product creation: Add new products to the platform with details such as title, description, and price.
  - Product listing: Retrieve a list of all products available in the platform.
  - Product details: Retrieve detailed information about a specific product.
  - Product update: Update the details of a product, including its title, description, and price.
  - Product deletion: Remove a product from the platform.

- Product Reviews:
  - Create product review: Allow users to submit reviews for a specific product.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/struckchure/yourstep.product-ms.git
   ```

2. Navigate to the project directory:

   ```shell
   cd yourstep.product-ms
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```shell
     source env/bin/activate
     ```

   - On Windows:

     ```shell
     .\env\Scripts\activate
     ```

5. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Run the database migrations:

   ```shell
   python manage.py migrate
   ```

7. Start the development server:

   ```shell
   python manage.py runserver
   ```

   The API server will start running at `http://localhost:8000/`.

## API Endpoints

### Product Management

#### Product List

- **URL:** `/product/`
- **Method:** GET
- **Description:** Retrieve a list of all products available in the platform.
- **Response:** JSON array containing details of all products.
  - `id` (integer): The unique identifier of the product.
  - `title` (string): The title of the product.
  - `description` (string): The description of the product.
  - `price` (float): The price of the product.

#### Product Details

- **URL:** `/product/{product_id}/`
- **Method:** GET
- **Description:** Retrieve detailed information about a specific product.
- **Response:** JSON object containing the details of the product.
  - `id` (integer): The unique identifier of the product.
  - `title` (string): The title of the product.
  - `description` (string): The description of the product.
  - `price` (float): The price of the product.

#### Create Product

- **URL:** `/product/`
- **Method:** POST
- **Description:** Create a new product in the platform.
- **Request Body:** JSON object containing the product details.
  - `title` (string): The title of the product.
  - `description` (string): The description of the product.
  - `price` (float): The price of the product.
- **Response:** JSON object containing the details of the created product.
  - `id` (integer): The unique identifier of the product.
  - `title` (string):

The title of the product.

- `description` (string): The description of the product.
- `price` (float): The price of the product.

#### Update Product

- **URL:** `/product/{product_id}/`
- **Method:** PUT
- **Description:** Update the details of a specific product.
- **Request Body:** JSON object containing the updated product details.
  - `title` (string): The updated title of the product.
  - `description` (string): The updated description of the product.
  - `price` (float): The updated price of the product.
- **Response:** JSON object containing the updated details of the product.
  - `id` (integer): The unique identifier of the product.
  - `title` (string): The updated title of the product.
  - `description` (string): The updated description of the product.
  - `price` (float): The updated price of the product.

#### Delete Product

- **URL:** `/product/{product_id}/`
- **Method:** DELETE
- **Description:** Delete a specific product from the platform.
- **Response:** HTTP 204 No Content on successful deletion.

### Product Reviews

#### Product Review List

- **URL:** `/product/{product_id}/review/`
- **Method:** GET
- **Description:** Retrieve a list of reviews for a specific product.
- **Response:** JSON array containing details of all reviews for the product.
  - `id` (integer): The unique identifier of the review.
  - `description` (string): The description of the review.
  - `grade` (integer): The rating of the review (between 0 and 5).

#### Create Product Review

- **URL:** `/product/{product_id}/review/`
- **Method:** POST
- **Description:** Create a new review for a specific product.
- **Request Body:** JSON object containing the review details.
  - `description` (string): The description of the review.
  - `grade` (integer): The rating of the review (between 0 and 5).
- **Response:** JSON object containing the details of the created review.
  - `id` (integer): The unique identifier of the review.
  - `description` (string): The description of the review.
  - `grade` (integer): The rating of the review (between 0 and 5).
