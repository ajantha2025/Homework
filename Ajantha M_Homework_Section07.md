
## 7.1 HW Questions

### Question 1. 
```SQL
SELECT ModelYear,Make,Model
FROM EVRegistry
```


### Question 2.
```SQL

SELECT DISTINCT ElectricVehicleType
FROM EVRegistry
```

### Question 3.
```SQL

SELECT *
FROM EVRegistry
WHERE ElectricVehicleType = "Battery Electric Vehicle (BEV)"
```

### Question 4.
```SQL
SELECT Make,Model
FROM EVRegistry
WHERE BaseMSRP BETWEEN 20000 AND 35000
```

## 7.2 HW Questions
### Question 1.
```SQL
SELECT * 
FROM EVRegistry
WHERE City is NULL
```

### Question 2.
```SQL
SELECT Make,Model,ElectricVehicleType
FROM EVRegistry
WHERE VIN like '%3E1EA1J'
```
### Question 3.
```SQL
SELECT ModelYear,Make,Model,ElectricVehicleType,ElectricRange
FROM EVRegistry
WHERE Make = 'TESLA' OR Make = 'CHEVROLET'
ORDER BY Make,ModelYear DESC
```
### Question 4.
```SQL
SELECT stationId,count(*) as ct
FROM EVCharging
GROUP BY stationId
ORDER BY ct DESC
LIMIT 5
```

### Question 5.
```SQL
SELECT userId,Min(chargeTimeHrs) as minTime,Max(chargeTimeHrs) as maxTime
FROM EVCharging
WHERE chargeTimeHrs > 0.5
GROUP by userId
ORDER by minTime,maxTime
```

## 7.3 HW Questions
### Question 1.
```SQL
SELECT weekday,round(avg(chargeTimeHrs),2)
FROM EVCharging
GROUP by weekday
ORDER by 2 desc
```
### Question 2.
```SQL
SELECT userId,round(sum(kwhTotal),2) as totalpower
FROM EVCharging
GROUP by userId
ORDER by 2 DESC
LIMIT 15
```

### Question 3.
```SQL 
SELECT df.typeFacility,count(*) as numStation
FROM dimFacility df
JOIN factCharge fc
on df.FacilityKey = fc.facilityID
GROUP by df.typeFacility
ORDER by 2 DESC
```

### Question 4.
--- 
##### PRIMARY KEY:

* The primary key uniquely identifies each record that exists in our tables.

* The values are always unique and they are never NULL values.
##### FOREIGN KEY:

* The foreign key in one table refers to the primary key in a "connected" table.
* The foreign key designation also helps prevent any action that could destroy the link between the two tables.
### Question 5.
```SQL
SELECT userid,min(chargeTimeHrs)as minTime,Max(chargeTimeHrs) as maxime
FROM evCharging
group by userid
having min(chargeTimehrs)>1 AND max(chargeTimeHrs)>1
order by 2 asc,3 asc 
```








