import os
import django
from django.db import connection

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shield_sql.settings')
django.setup()

sql_script = """
CREATE TABLE crime_scene (
    id INT PRIMARY KEY,
    date DATE,
    city VARCHAR(50),
    location VARCHAR(150),
    description TEXT
);
CREATE TABLE people (
    person_id INT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(200),
    occupation VARCHAR(100)
);

CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    owner_id INT,
    plate_number VARCHAR(20),
    vehicle_type VARCHAR(50),
    color VARCHAR(20),
    FOREIGN KEY (owner_id) REFERENCES people(person_id)
);
CREATE TABLE phone_calls (
    call_id INT PRIMARY KEY,
    caller_id INT,
    receiver_id INT,
    call_time DATETIME,
    duration INT,
    FOREIGN KEY (caller_id) REFERENCES people(person_id),
    FOREIGN KEY (receiver_id) REFERENCES people(person_id)
);
CREATE TABLE cafe_checkins (
    checkin_id INT PRIMARY KEY,
    person_id INT,
    cafe_name VARCHAR(100),
    checkin_time DATETIME,
    FOREIGN KEY (person_id) REFERENCES people(person_id)
);

CREATE TABLE bank_transactions (
    transaction_id INT PRIMARY KEY,
    sender_id INT,
    receiver_id INT,
    amount INT,
    transaction_time DATETIME,
    FOREIGN KEY (sender_id) REFERENCES people(person_id),
    FOREIGN KEY (receiver_id) REFERENCES people(person_id)
);

CREATE TABLE interviews (
    interview_id INT PRIMARY KEY,
    person_id INT,
    transcript TEXT,
    FOREIGN KEY (person_id) REFERENCES people(person_id)
);

INSERT INTO people VALUES
(1,'Arun Kumar','Thillai Nagar, Trichy','Teacher'),
(2,'Ramesh Babu','Srirangam, Trichy','Shop Owner'),
(3,'Karthik Raj','Woraiyur, Trichy','Engineer'),
(4,'Sathish Kumar','KK Nagar, Trichy','Driver'),
(5,'Pradeep','Tennur, Trichy','Student'),
(6,'Vignesh','Cantonment, Trichy','Salesman'),
(7,'Saravanan','Ponmalai, Trichy','Mechanic'),
(8,'Manoj','BHEL Township, Trichy','Engineer'),
(9,'Deepak','Thillai Nagar, Trichy','Bank Clerk'),
(10,'Suresh','Srirangam, Trichy','Teacher'),
(11,'Harish','Woraiyur, Trichy','Electrician'),
(12,'Vimal','KK Nagar, Trichy','Driver'),
(13,'Rajesh','Tennur, Trichy','Chef'),
(14,'Anand','Cantonment, Trichy','Business'),
(15,'Ajith','Ponmalai, Trichy','Technician'),
(16,'Dinesh','BHEL Township, Trichy','Operator'),
(17,'Murali','Thillai Nagar, Trichy','Doctor'),
(18,'Siva','Srirangam, Trichy','Lawyer'),
(19,'Ganesh','Woraiyur, Trichy','Driver'),
(20,'Balaji','KK Nagar, Trichy','Salesman'),
(21,'Naveen','Tennur, Trichy','Student'),
(22,'Ravi','Cantonment, Trichy','Manager'),
(23,'Kumaravel','Ponmalai, Trichy','Worker'),
(24,'Ashok','BHEL Township, Trichy','Engineer'),
(25,'Santhosh','Thillai Nagar, Trichy','Teacher'),
(26,'Vasu','Srirangam, Trichy','Clerk'),
(27,'Prakash','Woraiyur, Trichy','Auto Driver'),
(28,'Rohit','KK Nagar, Trichy','Student'),
(29,'Sanjay','Tennur, Trichy','Programmer'),
(30,'Aravind','Cantonment, Trichy','Designer'),
(31,'Hari','Ponmalai, Trichy','Driver'),
(32,'Bala','BHEL Township, Trichy','Technician'),
(33,'Rahul','Thillai Nagar, Trichy','Sales'),
(34,'Vicky','Srirangam, Trichy','Mechanic'),
(35,'Joseph','Woraiyur, Trichy','Pastor'),
(36,'Martin','KK Nagar, Trichy','Teacher'),
(37,'Albert','Tennur, Trichy','Accountant'),
(38,'Daniel','Cantonment, Trichy','Driver'),
(39,'Peter','Ponmalai, Trichy','Security'),
(40,'Victor','BHEL Township, Trichy','Engineer'),
(41,'Antony','Thillai Nagar, Trichy','Manager'),
(42,'Sebastian','Srirangam, Trichy','Cook'),
(43,'Pravin','Woraiyur, Trichy','Student'),
(44,'Kishore','KK Nagar, Trichy','Engineer'),
(45,'Arjun','Tennur, Trichy','Designer'),
(46,'Gokul','Cantonment, Trichy','Clerk'),
(47,'Yogesh','Ponmalai, Trichy','Driver'),
(48,'Vinoth','BHEL Township, Trichy','Worker'),
(49,'Nithin','Thillai Nagar, Trichy','Engineer'),
(50,'Surya','Srirangam, Trichy','Student'),
(51,'David','Woraiyur, Trichy','Driver'),
(52,'Benjamin','KK Nagar, Trichy','Mechanic'),
(53,'Leo Das','Tennur, Trichy','Business'),
(54,'Arul','Cantonment, Trichy','Driver'),
(55,'Bharath','Ponmalai, Trichy','Engineer'),
(56,'Kannan','BHEL Township, Trichy','Teacher'),
(57,'Prabhu','Thillai Nagar, Trichy','Sales'),
(58,'Madhan','Srirangam, Trichy','Clerk'),
(59,'Sudhakar','Woraiyur, Trichy','Driver'),
(60,'Manikandan','KK Nagar, Trichy','Technician'),
(61,'Dharani','Tennur, Trichy','Student'),
(62,'Sakthivel','Cantonment, Trichy','Engineer'),
(63,'Karthi','Ponmalai, Trichy','Driver'),
(64,'Selva','BHEL Township, Trichy','Mechanic'),
(65,'Imran','Thillai Nagar, Trichy','Trader'),
(66,'Nizam','Srirangam, Trichy','Driver'),
(67,'Rafiq','Woraiyur, Trichy','Sales'),
(68,'Shahid','KK Nagar, Trichy','Student'),
(69,'Ameer','Tennur, Trichy','Chef'),
(70,'Faizal','Cantonment, Trichy','Driver'),
(71,'Lokesh','Ponmalai, Trichy','Engineer'),
(72,'Sathya','BHEL Township, Trichy','Teacher'),
(73,'Raghu','Thillai Nagar, Trichy','Driver'),
(74,'Arvind','Srirangam, Trichy','Business'),
(75,'Mani','Woraiyur, Trichy','Mechanic'),
(76,'Senthil','KK Nagar, Trichy','Driver'),
(77,'Rajkumar','Tennur, Trichy','Engineer'),
(78,'Deva','Cantonment, Trichy','Sales'),
(79,'Sankar','Ponmalai, Trichy','Clerk'),
(80,'Thiru','BHEL Township, Trichy','Teacher'),
(81,'Baskar','Thillai Nagar, Trichy','Driver'),
(82,'Kasi','Srirangam, Trichy','Trader'),
(83,'Velu','Woraiyur, Trichy','Worker'),
(84,'Murugan','KK Nagar, Trichy','Driver'),
(85,'Perumal','Tennur, Trichy','Mechanic'),
(86,'Raja','Cantonment, Trichy','Electrician'),
(87,'Pandi','Ponmalai, Trichy','Driver'),
(88,'Muthu','BHEL Township, Trichy','Worker'),
(89,'Jagan','Thillai Nagar, Trichy','Engineer'),
(90,'Rithik','Srirangam, Trichy','Student'),
(91,'Naveed','Woraiyur, Trichy','Sales'),
(92,'Sadiq','KK Nagar, Trichy','Driver'),
(93,'Ajmal','Tennur, Trichy','Trader'),
(94,'Farhan','Cantonment, Trichy','Student'),
(95,'Hameed','Ponmalai, Trichy','Driver'),
(96,'Irfan','BHEL Township, Trichy','Mechanic'),
(97,'Khalid','Thillai Nagar, Trichy','Driver'),
(98,'Yaseen','Srirangam, Trichy','Worker'),
(99,'Zakir','Woraiyur, Trichy','Trader'),
(100,'Naren','KK Nagar, Trichy','Engineer');

INSERT INTO vehicles VALUES
(1,1,'TN45AB1234','Bike','Black'),
(2,2,'TN45AB2234','Car','White'),
(3,3,'TN45AB3234','Bike','Red'),
(4,4,'TN45AB4234','Bike','Blue'),
(5,5,'TN45AB5234','Scooter','Black'),
(6,6,'TN45AB6234','Bike','Red'),
(7,7,'TN45AB7234','Bike','Red'),
(8,8,'TN45AB8234','Car','Silver'),
(9,9,'TN45AB9234','Bike','Black'),
(10,10,'TN45AC1234','Bike','Red'),
(11,11,'TN45AC2234','Bike','White'),
(12,12,'TN45AC3234','Bike','Red'),
(13,13,'TN45AC4234','Car','White'),
(14,14,'TN45AC5234','Bike','Red'),
(15,15,'TN45AC6234','Bike','Blue'),
(16,16,'TN45AC7234','Bike','Red'),
(17,17,'TN45AC8234','Car','Black'),
(18,18,'TN45AC9234','Bike','Red'),
(19,19,'TN45AD1234','Bike','Green'),
(20,20,'TN45AD2234','Bike','Red'),
(21,21,'TN45AD3234','Bike','Black'),
(22,22,'TN45AD4234','Car','White'),
(23,23,'TN45AD5234','Bike','Red'),
(24,24,'TN45AD6234','Bike','Black'),
(25,25,'TN45AD7234','Bike','Red'),
(26,26,'TN45AD8234','Car','Silver'),
(27,27,'TN45AD9234','Bike','Red'),
(28,28,'TN45AE1234','Bike','Blue'),
(29,29,'TN45AE2234','Bike','Red'),
(30,30,'TN45AE3234','Car','White'),
(31,31,'TN45AE4234','Bike','Red'),
(32,32,'TN45AE5234','Bike','Black'),
(33,33,'TN45AE6234','Bike','Red'),
(34,34,'TN45AE7234','Car','White'),
(35,35,'TN45AE8234','Bike','Red'),
(36,36,'TN45AE9234','Bike','Blue'),
(37,37,'TN45AF1234','Bike','Red'),
(38,38,'TN45AF2234','Bike','Black'),
(39,39,'TN45AF3234','Bike','Red'),
(40,40,'TN45AF4234','Car','White'),
(41,41,'TN45AF5234','Bike','Black'),
(42,42,'TN45AF6234','Bike','Red'),
(43,43,'TN45AF7234','Bike','Blue'),
(44,44,'TN45AF8234','Bike','Red'),
(45,45,'TN45AF9234','Car','White'),
(46,46,'TN45AG1234','Bike','Red'),
(47,47,'TN45AG2234','Bike','Black'),
(48,48,'TN45AG3234','Bike','Red'),
(49,49,'TN45AG4234','Car','White'),
(50,50,'TN45AG5234','Bike','Blue'),
(51,51,'TN45AG6234','Bike','Black'),
(52,52,'TN45AG7234','Bike','Red'),
(53,53,'TN45AG8234','Car','Black'),
(54,54,'TN45AG9234','Bike','White'),
(55,55,'TN45AH1234','Bike','Black'),
(56,56,'TN45AH2234','Car','White'),
(57,57,'TN45AH3234','Bike','Blue'),
(58,58,'TN45AH4234','Bike','Black'),
(59,59,'TN45AH5234','Car','Silver'),
(60,60,'TN45AH6234','Bike','Black'),
(61,61,'TN45AH7234','Bike','White'),
(62,62,'TN45AH8234','Car','Black'),
(63,63,'TN45AH9234','Bike','Blue'),
(64,64,'TN45AJ1234','Bike','Black'),
(65,65,'TN45AJ2234','Car','White'),
(66,66,'TN45AJ3234','Bike','Blue'),
(67,67,'TN45AJ4234','Bike','Black'),
(68,68,'TN45AJ5234','Car','Silver'),
(69,69,'TN45AJ6234','Bike','Black'),
(70,70,'TN45AJ7234','Bike','White'),
(71,71,'TN45AJ8234','Car','Black'),
(72,72,'TN45AJ9234','Bike','Blue'),
(73,73,'TN45AK1234','Bike','Black'),
(74,74,'TN45AK2234','Car','White'),
(75,75,'TN45AK3234','Bike','Blue'),
(76,76,'TN45AK4234','Bike','Black'),
(77,77,'TN45AK5234','Car','Silver'),
(78,78,'TN45AK6234','Bike','Black'),
(79,79,'TN45AK7234','Bike','White'),
(80,80,'TN45AK8234','Car','Black'),
(81,81,'TN45AK9234','Bike','Blue'),
(82,82,'TN45AL1234','Bike','Black'),
(83,83,'TN45AL2234','Car','White'),
(84,84,'TN45AL3234','Bike','Blue'),
(85,85,'TN45AL4234','Bike','Black'),
(86,86,'TN45AL5234','Car','Silver'),
(87,87,'TN45AL6234','Bike','Black'),
(88,88,'TN45AL7234','Bike','White'),
(89,89,'TN45AL8234','Car','Black'),
(90,90,'TN45AL9234','Bike','Blue'),
(91,91,'TN45AM1234','Bike','Black'),
(92,92,'TN45AM2234','Car','White'),
(93,93,'TN45AM3234','Bike','Blue'),
(94,94,'TN45AM4234','Bike','Black'),
(95,95,'TN45AM5234','Car','Silver'),
(96,96,'TN45AM6234','Bike','Black'),
(97,97,'TN45AM7234','Bike','White'),
(98,98,'TN45AM8234','Car','Black'),
(99,99,'TN45AM9234','Bike','Blue'),
(100,100,'TN45AN1234','Bike','Black');

INSERT INTO crime_scene VALUES
(1,'2025-08-15','Trichy','Rockfort Temple Parking','A body was discovered near parked vehicles around 9:30 PM'),
(2,'2025-07-12','Trichy','Srirangam Bus Stand','Minor theft reported near parking area'),
(3,'2025-06-02','Trichy','Thillai Nagar Main Road','Chain snatching reported in the evening'),
(4,'2025-07-21','Trichy','Woraiyur Market','Mobile phone stolen near vegetable market'),
(5,'2025-05-19','Trichy','Cantonment Railway Station','Suspicious activity reported by commuters'),
(6,'2025-04-11','Trichy','KK Nagar Park','Wallet theft reported by jogger'),
(7,'2025-03-10','Trichy','Ponmalai Workshop Gate','Bike missing from parking'),
(8,'2025-02-08','Trichy','BHEL Township Gate','Unauthorized entry reported'),
(9,'2025-01-28','Trichy','Tennur Signal','Traffic altercation reported'),
(10,'2024-12-20','Trichy','Chatram Bus Stand','Pickpocket complaint filed');

INSERT INTO cafe_checkins VALUES
(1,12,'Sangeetha Cafe','2025-08-15 18:10:00'),
(2,21,'A2B','2025-08-15 19:00:00'),
(3,35,'Jeff Cafe','2025-08-14 20:10:00'),
(4,45,'Sangeetha Cafe','2025-08-15 20:05:00'),
(5,52,'Jeff Cafe','2025-08-15 20:45:00'),
(6,53,'Jeff Cafe','2025-08-15 20:47:00'),
(7,61,'A2B','2025-08-15 21:30:00'),
(8,70,'Jeff Cafe','2025-08-13 19:20:00'),
(9,77,'Sangeetha Cafe','2025-08-15 18:40:00'),
(10,82,'A2B','2025-08-15 19:15:00'),
(11,15,'Jeff Cafe','2025-08-15 19:20:00'),
(12,16,'Jeff Cafe','2025-08-15 19:45:00'),
(13,17,'A2B','2025-08-15 18:55:00'),
(14,18,'Sangeetha Cafe','2025-08-15 19:10:00'),
(15,19,'Jeff Cafe','2025-08-15 20:10:00'),
(16,20,'Jeff Cafe','2025-08-15 21:15:00'),
(17,22,'A2B','2025-08-15 20:20:00'),
(18,23,'Sangeetha Cafe','2025-08-15 19:30:00'),
(19,24,'Jeff Cafe','2025-08-14 20:50:00'),
(20,25,'A2B','2025-08-15 18:25:00'),
(21,26,'Jeff Cafe','2025-08-15 19:55:00'),
(22,27,'Jeff Cafe','2025-08-15 20:35:00'),
(23,28,'Jeff Cafe','2025-08-15 21:05:00'),
(24,29,'Sangeetha Cafe','2025-08-15 18:45:00'),
(25,30,'A2B','2025-08-15 19:50:00'),
(26,31,'Jeff Cafe','2025-08-14 21:10:00'),
(27,32,'Sangeetha Cafe','2025-08-15 20:15:00'),
(28,33,'Jeff Cafe','2025-08-15 19:40:00'),
(29,34,'A2B','2025-08-15 20:25:00'),
(30,36,'Jeff Cafe','2025-08-15 18:40:00');

INSERT INTO phone_calls VALUES
(1,10,11,'2025-08-15 20:00:00',120),
(2,18,19,'2025-08-15 20:10:00',60),
(3,25,30,'2025-08-15 20:40:00',180),
(4,53,52,'2025-08-15 21:10:00',95),
(5,61,45,'2025-08-15 22:00:00',140),
(6,72,73,'2025-08-14 18:20:00',70),
(7,81,90,'2025-08-15 19:50:00',30),
(8,44,55,'2025-08-15 20:30:00',50),
(9,14,22,'2025-08-15 19:10:00',40),
(10,21,35,'2025-08-15 20:20:00',120),
(11,32,18,'2025-08-15 20:45:00',75),
(12,11,70,'2025-08-15 21:00:00',50),
(13,29,15,'2025-08-15 21:12:00',100),
(14,31,41,'2025-08-15 18:55:00',90),
(15,44,22,'2025-08-15 20:10:00',30),
(16,50,51,'2025-08-15 19:35:00',60),
(17,63,64,'2025-08-15 20:25:00',110),
(18,75,76,'2025-08-15 20:05:00',20),
(19,81,44,'2025-08-15 18:40:00',45),
(20,90,91,'2025-08-15 19:15:00',80);

INSERT INTO bank_transactions VALUES
(1,11,12,500,'2025-08-10 10:00:00'),
(2,22,23,1200,'2025-08-11 12:20:00'),
(3,30,31,2000,'2025-08-12 09:10:00'),
(4,53,52,50000,'2025-08-14 16:30:00'),
(5,61,45,800,'2025-08-14 10:20:00'),
(6,70,71,1500,'2025-08-15 11:40:00'),
(7,82,83,950,'2025-08-13 13:10:00'),
(8,12,14,600,'2025-08-10 09:10:00'),
(9,15,18,850,'2025-08-11 11:20:00'),
(10,20,21,900,'2025-08-12 15:10:00'),
(11,24,26,1500,'2025-08-13 13:50:00'),
(12,28,30,1100,'2025-08-14 09:40:00'),
(13,33,35,500,'2025-08-14 12:00:00'),
(14,40,41,700,'2025-08-14 14:20:00'),
(15,45,46,950,'2025-08-14 18:10:00'),
(16,48,50,2000,'2025-08-15 10:05:00'),
(17,52,55,1200,'2025-08-15 11:15:00'),
(18,60,61,800,'2025-08-15 12:45:00'),
(19,70,72,1500,'2025-08-15 13:30:00'),
(20,80,81,1750,'2025-08-15 14:00:00');	

INSERT INTO interviews VALUES
(1,21,'I was walking near Rockfort around 9 PM and noticed a red bike parked nearby.'),
(2,35,'I visited Jeff Cafe earlier that evening but left before night.'),
(3,61,'I heard some noise near the parking lot but did not see anyone clearly.'),
(4,72,'The area was crowded because of temple visitors.'),
(5,82,'Many bikes were parked there, hard to remember details.'),
(6,10,'I passed near Rockfort around 8:45 PM and saw many bikes parked there.'),
(7,18,'I noticed a red colored bike near the temple parking earlier that night.'),
(8,33,'Jeff Cafe was crowded on August 15 evening.'),
(9,44,'Some people were leaving the cafe quickly before 9 PM.'),
(10,55,'I heard someone arguing near the Rockfort parking area.'),
(11,63,'A man was standing near a red bike and talking on phone.'),
(12,70,'Temple area had heavy crowd that night.'),
(13,81,'I only saw bikes and cars parked, nothing suspicious.'),
(14,92,'Someone mentioned a bike leaving quickly around 9:15 PM.'),
(15,100,'I remember seeing two men talking near the parking area before the police arrived.');
"""

def reset_db():
    with connection.cursor() as cursor:
        # Drop tables in reverse order of dependencies
        tables = [
            'interviews', 'bank_transactions', 'cafe_checkins', 
            'phone_calls', 'vehicles', 'people', 'crime_scene'
        ]
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
        print("Dropped existing tables.")

def populate():
    with connection.cursor() as cursor:
        # Split script into individual statements and execute
        statements = [s.strip() for s in sql_script.split(';') if s.strip()]
        for statement in statements:
            try:
                cursor.execute(statement)
            except Exception as e:
                print(f"Error executing statement: {statement[:50]}...")
                print(f"Error: {e}")
        print("Database populated successfully.")

if __name__ == "__main__":
    reset_db()
    populate()
