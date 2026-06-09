Bronze Bucket Name = p1-youtubedatapipeline-b1

Silver Bucket Name = p1-youtubedatapipeline-s1

Gold Bucket Name = p1-youtubedatapipeline-g1

Scripts Bucket Name = p1-youtubedatapipeline-scripts

--bronze_database yt_pipeline_bronze_dev 
--bronze_table raw_statistics 
--silver_bucket p1-youtubedatapipeline-s1 
--silver_database yt_pipeline_silver_dev 
--silver_table clean_statistics