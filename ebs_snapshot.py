import boto3

def create_ebs_snapshots(region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    volumes = ec2.describe_volumes()['Volumes']
    for vol in volumes:
        vol_id = vol['VolumeId']
        desc = f'Snapshot of {vol_id}'
        response = ec2.create_snapshot(VolumeId=vol_id, Description=desc)
        print(f"Snapshot created: {response['SnapshotId']} for volume {vol_id}")

# create_ebs_snapshots()
