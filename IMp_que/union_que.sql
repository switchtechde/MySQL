-- Que 
I have 2 table which contain col as below 
Table 1  -  UPI_Transistion_details
Trans_id Source_act_no  Target_act_no S_IFSC_code T_IFSC_CODE Branch_name Amount Transistion_date 
70 rows 

Table 2  -  NEFT_Transistion_details 
Trans_id Source_act_no  Target_act_no S_IFSC_code T_IFSC_CODE Branch_name Amount Transistion_date
50 rows

We need to insert Data into table 3 as Final_transistion 
Trans_id Source_act_no  Target_act_no S_IFSC_code T_IFSC_CODE Branch_name Amount Transistion_date Transistion_type 
120 rows


Insert Into Final_transistion (Trans_id,Source_act_no,Target_act_no,S_IFSC_code,
T_IFSC_CODE,Branch_name,Amount,Transistion_date,Transistion_type 
) 
Select Trans_id,
    Source_act_no,
    Target_act_no,
    S_IFSC_code,
    T_IFSC_CODE,
    Branch_name,
    Amount,
    Transistion_date,
    'UPI' as Transistion_type  
from UPI_Transistion_details
Union all 
Select Trans_id,
    Source_act_no,
    Target_act_no,
    S_IFSC_code,
    T_IFSC_CODE,
    Branch_name,
    Amount,
    Transistion_date,
    'NEFT' as Transistion_type 
from NEFT_Transistion_details


