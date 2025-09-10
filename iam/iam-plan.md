# IAM Plan for Secure WebApp Deployment

## Roles
- **CI/CD Role**: Can deploy to S3 or EC2, but cannot modify IAM policies.
- **Audit Role**: Can read logs and CloudTrail events.
- **Developer Role**: Can push code, but cannot deploy.

## Policies
- Use least privilege.
- No wildcard(*) permissions
- Rotate credentials every 90 days
- Cannot reuse used passwords

## Future Enhancements
- Provision roles using Terraform.
- Scan IAM policies with Checkov.

