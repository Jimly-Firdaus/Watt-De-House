# Watt-De-House

# General Information
This program was created to complete the IF2250 Software Engineering Implementation Task. This program has two main features: Estimator and Simulator. The Estimator feature is used to calculate the estimated cost of electricity consumption. This feature requests input data for electrical devices and an estimated duration of use for these devices. The Simulator feature is used to simulate the electrical devices in a house. This feature requests input data for electrical devices, circuit breakers, and rooms. After that, the program will simulate whether an electrical overload occurs or not if the electrical devices are turned on simultaneously.

# How To Run Program
1. Clone repository
```bash
git clone "https://gitlab.informatika.org/Jimly-Firdaus/watt-de-house.git"
```
2. Go into the directory in which the repo is cloned

3. Enter src
```bash
cd src
```
4. Run the program
```bash
python main.py
```

# List of Modules
1. Data Input Module\
![DataInput.png](images/DataInput.png)
    <p>Figure 1. Data Input Display</p>

2. Simulator Module\
![Simulator.png](images/Simulator.png)
    <p>Figure 2. Simulator Display</p>

3. Estimator Module\
![Estimator.png](images/Estimator.png)
    <p>Figure 3. Estimator Display</p>

4. Room Module \
![Ruangan.png](images/Ruangan.png)
    <p>Figure 4. Room Display</p>

5. Electrical Device Module

# Database
## 1. perangkat_listrik
This table is used to store information regarding any electrical devices that are used in the program.
Attribute | Constraint
----- | -----
id | Integer, Primary Key
status | Integer
nama | Text
daya | Real
arus | Real
tegangan | Real
nama_ruangan | Text
durasi | Integer

## 2. ruangan
This table is used to store the rooms in the house frame.
Attribute | Constraint
----- | -----
id | Integer, Primary Key
nama_ruangan | Text
circuit_breaker | Integer
circuit_breaker_name | Text
threshold | Real

## 3. ruangan_perangkat_listrik
This table is used to show the relation between the room id and the device id.
Attribute | Constraint
----- | -----
id_ruangan | Integer
id_perangkat_listrik | Integer

# Task Distribution

Name (NIM) | Task
----- | -----
Wilson Tansil (13521054) | Simulator, GUI
Bill Clinton (13521064) | Electrical Device, GUI
Jimly Firdaus (13521102) | Data Input, GUI
Ulung Adi Putra (13521122) | Estimator, GUI
Muhammad Zaki Amanullah (13521146) | Room, GUI
