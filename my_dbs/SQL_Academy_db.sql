create database Academy_DB;
 
use Academy_DB;

CREATE TABLE Students(
student_id INT IDENTITY(1,1) PRIMARY KEY,
full_name NVARCHAR(100) not null ,
email varchar(150) unique not null,
phone  varchar(20) ,
city NVARCHAR (100),
enrollment_date DATE DEFAULT GETDATE()
);

insert into Students(
full_name,
email,
phone,
city
)
values(
'Marwan Elsayed',
'marwanelsayed1107@gmail.com',
'01228720651',
'Alexandria'),
('Ahmed Ali', 
'ahmed.ali@email.com', 
'01011111111', 
'Cairo'),
('Sara Ahmed',
'sara.ahmed@email.com', 
'01122222222', 
'Alexandria'),
('Mohamed Sayed', 
'mohamed.sayed@email.com', 
'01233333333', 
'Giza'),
('Noor Hassan', 
'noor.hassan@email.com', 
'01544444444', 
'Mansoura'),
('Tarek Aziz', 
'tarek.aziz@email.com', 
'01055555555', 
'Tanta'),
('Aya Youssef', 
'aya.youssef@email.com', 
'01166666666', 
'Luxor'),
('Omar Farouk', 
'omar.farouk@email.com', 
'01277777777', 
'Aswan'),
('Fatma Ibrahim', 
'fatma.ibrahim@email.com', 
'01588888888', 
'Zagazig'),
('Mostafa Kamal', 
'mostafa.kamal@email.com', 
'01099999999', 
'Asyut');



update Students set city = 'Giza' where student_id = 2 -- 👌🏽

CREATE TABLE Courses(
course_id INT IDENTITY(1,1) PRIMARY KEY,
course_name NVARCHAR(100) NOT NULL,
price DECIMAL(10,2),
duration_hrs INT,
is_active BIT DEFAULT(1) ,
);
INSERT INTO Courses(
course_name,
price,
duration_hrs,
is_active)
values(
'AI and Data Science',
10000,
170,1),
('Python Fundamentals', 1500.00, 40, 1),
('Machine Learning Basics', 3500.00, 80, 1),
('SQL Databases', 2000.00, 30, 1),
('Deep Learning Specialization', 6000.00, 100, 1),
('Data Analysis with Python',7000,130,1),
('Data Visualization with PowerBI', 1800.00, 25, 1),
('Web Development with Node.js', 4000.00, 90, 1),
('FastAPI Backend Development', 2500.00, 35, 1),
('Advanced Data Structures', 3000.00, 50, 0);

CREATE TABLE Enrollments(
enrollment_id INT IDENTITY(1,1) PRIMARY KEY,
student_id INT not null,
CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES Students(student_id),
course_id int not null,
CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES Courses(course_id),
enrolled_at DATE DEFAULT GETDATE(),
activty_status VARCHAR(20) DEFAULT ('Active')
);
INSERT INTO Enrollments (
student_id, 
course_id)
VALUES 
(1,1),
(2, 1),
(3, 10),
(4, 4),
(5, 3),
(6, 5),
(7, 6),
(8, 7),
(9,8),
(10,9);

CREATE TABLE Payments(
payment_id INT IDENTITY(1,1) PRIMARY KEY,
  enrollment_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  payment_date DATE  DEFAULT GETDATE() NOT NULL ,
  method VARCHAR(50) NOT NULL,
  activty_status VARCHAR(20) NOT NULL DEFAULT ('Pending'),
  CONSTRAINT fk_enrollments FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id)
);

INSERT INTO Payments (enrollment_id,
amount,
method,
activty_status)
VALUES (1,
1500.50, 
'Credit Card',
'Completed'),
(1, 5000.00,  'Credit Card', 'Completed'),
(2, 2500.00,  'Vodafone Cash', 'Pending'), -- Partial payment
(3, 1500.00,  'InstaPay', 'Completed'),
(4, 2000.00,  'Cash', 'Completed'),
(5, 3500.00,  'Credit Card', 'Completed'),
(6, 6000.00,  'Bank Transfer', 'Completed'),
(7, 1800.00,  'Vodafone Cash', 'Completed'),
(8, 4000.00,  'InstaPay', 'Completed'),
(9, 9000.00,  'Vodafone Cash', 'Failed'),
(10, 2500.00,  'InstaPay', 'Pending'); -- Partial payment

CREATE TABLE Leads
(
    lead_id INT IDENTITY(1,1) PRIMARY KEY,
    lead_name NVARCHAR(100),
    phone VARCHAR(20),
    source NVARCHAR(50),
    created_at DATETIME2 DEFAULT GETDATE()
);

INSERT INTO Leads (lead_name, phone, source)
VALUES 
('Hassan Mahmoud', '01098765432', 'Facebook Ad'),
('Mariam Ali', '01123456789', 'Website'),
('John Smith', '+15550199283', 'LinkedIn'),
('Fatma Saeed', '01555667788', 'Referral'),
('Kareem Adel', '01000112233', 'Google Search'),
('Yasmine Nour', '01144556677', 'Instagram'),
('Sherif Amr', '01288990011', 'Website'),
('Sarah Connor', '+15550144829', 'LinkedIn'),
('Mostafa Ibrahim', '01012345678', 'TikTok'),
('Lina Refaat', '01122334455', 'Facebook Ad');


select * 
from Students

select *
from  Courses 

select *
from Enrollments

select *
from Payments

select *
from Leads

DELETE FROM Courses 
WHERE course_id = 2;

TRUNCATE TABLE Enrollments;

ALTER TABLE Students
ADD nationality VARCHAR(100);

SELECT TOP(10) *
FROM Students 
ORDER BY enrollment_date desc; 

select distinct city from Students

UPDATE Students 
SET nationality = 'Egyptian';

ALTER TABLE Leads
ALTER COLUMN created_at DATETIME2;

select * from Leads where created_at between '2026-07-15' and '2026-07-16'

SELECT dc.name AS ConstraintName
FROM sys.default_constraints dc
JOIN sys.columns c
    ON dc.parent_object_id = c.object_id
   AND dc.parent_column_id = c.column_id
WHERE OBJECT_NAME(dc.parent_object_id) = 'Leads'
AND c.name = 'created_at';

ALTER TABLE Leads
DROP CONSTRAINT DF__Leads__created_a__6E01572D;

select * from Students where enrollment_date between '2026-07-15' and '2026-07-16'

SELECT * FROM Leads
WHERE source NOT IN ('Referral', 'WalkIn');

SELECT * FROM Payments
WHERE payment_date IS NOT NULL;

SELECT * FROM Students
WHERE full_name LIKE '%M%';

select source ,COUNT(*) as total_leads
from Leads
group by source -- 3dd el leads mn kol source

select sum(amount) as total_revenue
from Payments -- kol elflos elly d5lt from selling courses

select avg(amount) as avg_payment_by_course
from Payments -- average elflos elly d5lt from selling courses

SELECT source, COUNT(*) AS lead_count
FROM Leads
WHERE created_at >= '2026-06-01' -- 3dd el leads mn kol source b3d the selected date 
GROUP BY source
HAVING COUNT(*) >= 2; -- condition by7dd 3dd leads mo3yn f kol source

SELECT s.full_name, s.city, e.course_id, e.enrolled_at
FROM Students s
INNER JOIN Enrollments e ON s.student_id = e.student_id -- the students names & city with there course ID that they enrolled at

SELECT s.full_name, s.city, e.course_id, e.enrolled_at ,c.course_name
FROM Students s
INNER JOIN Enrollments e ON s.student_id = e.student_id
INNER JOIN Courses c ON e.course_id = c.course_id -- the students names & city with there course ID that they enrolled at with the course name

SELECT s.full_name, s.city, p.amount, e.enrolled_at , e.enrollment_id
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Payments p ON p.enrollment_id = e.enrollment_id -- students names with there payment amount 

SELECT c.course_name,
COUNT(e.enrollment_id) AS enrollment_count
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY enrollment_count DESC; -- Count how many students enrolled in each course

SELECT
s.full_name,
c.course_name,
e.enrolled_at,
SUM(p.amount) AS total_paid,
CASE WHEN SUM(p.amount) IS NULL THEN 'Unpaid' ELSE 'Paid' END AS payment_status
FROM Students s
INNER JOIN Enrollments e ON s.student_id = e.student_id
INNER JOIN Courses c ON e.course_id = c.course_id
LEFT JOIN Payments p ON e.enrollment_id = p.enrollment_id 
GROUP BY s.full_name, c.course_name, e.enrolled_at
ORDER BY s.full_name, c.course_name; -- Full student report: name, course, enrollment date, total paid

SELECT lead_name,
ISNULL(source, 'Unknown') AS clean_source
FROM Leads;

SELECT lead_name,
COALESCE(phone_mobile, phone_home, 'No phone')
AS best_phone
FROM Leads;

SELECT
TRIM(phone) AS clean_phone,
UPPER(TRIM(lead_name)) AS clean_name,
LOWER(source) AS clean_source
FROM Leads;

SELECT lead_name,
CASE
WHEN LOWER(TRIM(source)) IN ('facebook','facebook ads','fb') THEN 'Facebook'
WHEN LOWER(TRIM(source)) IN ('google','google ads') THEN 'Google'
WHEN source IS NULL THEN 'Unknown'
ELSE TRIM(source) END AS clean_source
FROM Leads;

SELECT student_id,
TRY_CAST(REPLACE(amount_text,',',' ') AS DECIMAL(10,2)) AS
clean_amount,
TRY_CONVERT(DATE, registration_text, 105) AS clean_date
FROM Students;

SELECT
lead_name, source, phone, created_at,
CASE
WHEN created_at >= DATEADD(DAY, -7, GETDATE()) THEN 'Hot Lead'
WHEN created_at >= DATEADD(DAY, -30, GETDATE()) THEN 'Warm Lead'
ELSE 'Cold Lead'
END AS lead_temperature
FROM Leads
ORDER BY created_at DESC;  -- Classify leads by how recently they were created

SELECT phone,
COUNT(*) AS occurrences
FROM Leads
GROUP BY phone
HAVING COUNT(*) > 1
ORDER BY occurrences DESC; -- finding duplicate