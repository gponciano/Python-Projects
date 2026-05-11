from localstack_setup import get_client

def test_connection():
    ec2 = get_client("ec2")
    response = ec2.describe_vpcs()
    vpcs = response.get("Vpcs", [])
    print(f"Connection successful. VPCs found: {len(vpcs)}")
    for vpc in vpcs:
        print(f"  - VPC ID: {vpc['VpcId']}  CIDR: {vpc['CidrBlock']}")

if __name__ == "__main__":
    test_connection()