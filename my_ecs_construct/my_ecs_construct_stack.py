from aws_cdk import Stack
from aws_cdk import (aws_ec2 as ec2, aws_ecs as ecs,
                     aws_ecs_patterns as ecs_patterns)
from constructs import Construct
from aws_cdk.aws_ecr_assets import DockerImageAsset
import logging
from pathes import get_iam_docker_path

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='logs/ckd-stack.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class MyEcsConstructStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # image = DockerImageAsset(self, "IAM_docker",
        #     directory=get_iam_docker_path()
        # )
        # logger.info(image.image_uri)
        # logger.info(image.repository.repository_arn)
        # logger.info(image.image_tag)

         # Create VPC and Fargate Cluster
        # NOTE: Limit AZs to avoid reaching resource quotas
        # vpc = ec2.Vpc(
        #     self, "FargateVpc",
        #     max_azs=2
        # )

        # cluster = ecs.Cluster(
        #     self, 'FargateCluster',
        #     vpc=vpc
        # )
        # task_id = "IAM_docker_task_id"
        # container_id = f'{task_id}-Container'
        # service_id = f"{task_id}-Service"

        # task_definition = ecs.FargateTaskDefinition(
        #     self, 'FargateTask',
        #     cpu=256, 
        #     memory_limit_mib=512
        # )
        
        # # Define Nginx Docker image asset
        # nginx_image = ecs.ContainerImage.from_registry("nginx:latest")
        
        # image = ecs.ContainerImage.from_ecr_repository(repository=image.repository, tag=image.image_tag)

        # logger.info(f"Image name: {image.image_name}")

        # container = task_definition.add_container (
        #     "NginxContainer",
        #     image=nginx_image,
        # )
        # container.add_port_mappings(ecs.PortMapping(container_port=80))
        # service = ecs_patterns.ApplicationLoadBalancedFargateService(
        #     self, "FargateService",
        #     cluster=cluster,
        #     task_definition=task_definition,
        #     desired_count=1,  # Adjust as needed
        #     listener_port=80  # Adjust port as needed
        # )

        # vpc = ec2.Vpc(self, "MyVpc", max_azs=3)     # default is all AZs in region

        cluster = ecs.Cluster(self, "MyCluster", enable_fargate_capacity_providers=True,
                              
                              )

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MyFargateService",
            cluster=cluster,            # Required
            cpu=256,                    # Default is 256
            # desired_count=6,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            memory_limit_mib=512,      # Default is 512
            public_load_balancer=True)  # Default is True