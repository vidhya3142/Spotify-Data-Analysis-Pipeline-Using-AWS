import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Albums
Albums_node1730218580412 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-bucket12/staging/albums.csv"], "recurse": True}, transformation_ctx="Albums_node1730218580412")

# Script generated for node Artists
Artists_node1730218581156 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-bucket12/staging/artists.csv"], "recurse": True}, transformation_ctx="Artists_node1730218581156")

# Script generated for node Tracks
Tracks_node1730218581898 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-bucket12/staging/track.csv"], "recurse": True}, transformation_ctx="Tracks_node1730218581898")

# Script generated for node Join 
Join_node1730218593121 = Join.apply(frame1=Albums_node1730218580412, frame2=Artists_node1730218581156, keys1=["artist_id"], keys2=["id"], transformation_ctx="Join_node1730218593121")

# Script generated for node Join
Join_node1730218593768 = Join.apply(frame1=Tracks_node1730218581898, frame2=Join_node1730218593121, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Join_node1730218593768")

# Script generated for node Drop Fields
DropFields_node1730218603098 = DropFields.apply(frame=Join_node1730218593768, paths=["id", "`.track_id`"], transformation_ctx="DropFields_node1730218603098")

# Script generated for node Amazon S3
AmazonS3_node1730218612164 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1730218603098, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotify-bucket12/warehousing1/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1730218612164")

job.commit()
