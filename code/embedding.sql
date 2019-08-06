SELECT userid,
       luid,
       view_time,
       unix_timestamp(view_time) as timesec
FROM xzdw.dw_log_user_lu_view
WHERE datediff(date_sub(current_date ,1) ,to_date(view_time))<365
  AND userid IS NOT NULL
  AND userid <> ""
  AND userid>10000000
 ORDER BY userid,view_time;
