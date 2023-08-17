custodian run --output-dir ouput --region us-east-2 running-instances.yaml
custodian report --output-dir ouput --region us-east-2 running-instances.yaml

#  docker build -t kkaaee1990/cloud-custodian-aws:latest .  && docker push  kkaaee1990/cloud-custodian-aws:latest
#  docker run -d -p 8080:80 kkaaee1990/cloud-custodian-aws:latest # cloud-custodian
