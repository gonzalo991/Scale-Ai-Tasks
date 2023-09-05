-- Create a dataset for the logistics company
CREATE OR REPLACE DATASET logistics;

-- Create a table to store information about deliveries
CREATE OR REPLACE TABLE logistics.deliveries (
    delivery_id STRING,
    client_id INT64,
    delivery_date DATE,
    delivery_time TIME,
    pickup_location STRING,
    delivery_location STRING,
    status STRING,
    estimated_delivery_time TIME,
    delivery_notes STRING,
) PRIMARY KEY (delivery_id DEFAULT (GENERATED_UUID()));

-- Create a table to store information about clients
CREATE OR REPLACE TABLE logistics.clients (
    client_id STRING,
    client_name STRING,
    contact_person STRING,
    email STRING,
    phone_number STRING,
    address STRING,
    PRIMARY KEY (client_id DEFAULT (GENERATED_UUID()))
);

-- Create a table to store information about delivery drivers
CREATE OR REPLACE TABLE logistics.drivers (
    driver_id STRING,
    driver_name STRING,
    license_number STRING,
    vehicle_plate_number STRING,
    contact_number STRING,
    hire_date DATE,
    status STRING,
    PRIMARY KEY (driver_id DEFAULT (GENERATED_UUID()))
);

-- Create a table to store information about delivery routes
CREATE OR REPLACE TABLE logistics.routes (
    route_id STRING,
    route_name STRING,
    start_location STRING,
    end_location STRING,
    distance_km NUMERIC,
    estimated_duration INT64, -- In minutes
    notes STRING,
    PRIMARY KEY (route_id DEFAULT (GENERATED_UUID()))
);

-- Create a table to track delivery history and status updates
CREATE OR REPLACE TABLE logistics.delivery_history (
    history_id STRING,
    delivery_id STRING,
    status STRING,
    update_time DATETIME,
    notes STRING,
    PRIMARY KEY (history_id DEFAULT (GENERATED_UUID()))
);
