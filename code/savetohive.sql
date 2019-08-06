load data local inpath
	 "/data1/embedding/result/item_vec${vDate}.txt"
into table algorithm.mds_lu_embedding_da partition(dt= (date_sub(current_date ,1));

