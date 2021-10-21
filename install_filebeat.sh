wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.15.1-linux-x86_64.tar.gz -O filebeat.tar.gz
tar -vzxf filebeat.tar.gz
rm filebeat.tar.gz
mkdir filebeat
cp -r filebeat-7.15.1-linux-x86_64/* filebeat/
cp filebeat.yml filebeat/
rm -rf filebeat-7.15.1-linux-x86_64/