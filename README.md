# **BBT Car Dealership Management System** 🚗  

## **Overview**  
BBT Car Dealership Management System is a **Python-based car dealership management system** that helps manage **car details, customer details, and vehicle registrations**. The system uses **CSV files** to store data and provides menu-based navigation for easy interaction.  

## **Features**  
✅ **Car Management:** Add, delete, update, and view cars in inventory.  
✅ **Customer Management:** Maintain buyer records with contact details.  
✅ **Vehicle Registration:** Register cars for customers and generate bills.  
✅ **CSV Data Storage:** All records are saved in CSV files for simplicity.  

## **Technologies Used**  
- **Python** 🐍  
- **Pandas** (for data handling)  
- **NumPy**  
- **Datetime** (for billing dates)  
- **CSV Files** (for storing data)  

## **Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/BBT-Car-Dealership.git
   cd BBT-Car-Dealership
   ```
2. Install dependencies:  
   ```bash
   pip install pandas numpy
   ```
3. Run the program:  
   ```bash
   python main.py
   ```

## **Usage**  
Once you run `main.py`, the system displays a **menu** where you can:  
- **Manage cars** (add, update, delete, view).  
- **Manage buyers** (add, update, delete, view).  
- **Register a vehicle** (assign a car to a customer).  

### **Menu Options:**  
```
1 - Car Details
2 - Buyer Details
3 - Vehicle Registration
4 - Exit
```

## **Data Storage Format**  
The system stores records in three CSV files:  
📂 **car.csv** - Stores car details (car type, brand, color, price, etc.)  
📂 **Buyers_Details.csv** - Stores customer records (name, contact, email, etc.)  
📂 **Vehicle_Registration.csv** - Stores registered vehicle sales (customer name, car details, price, etc.)  

## **Example Output**  
```
Welcome to BBT CAR DEALERSHIP
-------------------------------
1 - Car Details
2 - Buyer Details
3 - Vehicle Registration
4 - Exit
Enter your choice (1-4):
```

## **License**  
This project is licensed under the **MIT License** – you are free to use, modify, and distribute it with attribution.  

## **Contributing**  
1. Fork the repository  
2. Create a new branch: `git checkout -b feature-branch`  
3. Commit your changes: `git commit -m "Added new feature"`  
4. Push to the branch: `git push origin feature-branch`  
5. Open a **Pull Request**  

## **Author**  
👤 **Pratik Borle**  
📧 Email: pratikborle64@gmail.com  
🔗 GitHub: pratikborle74 (https://github.com/pratikborle74)  
