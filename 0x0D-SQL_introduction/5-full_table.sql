-- script that prints the full description of the table first_table
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
  AND table_name = 'first_table';