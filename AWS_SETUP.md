# AWS Credentials Setup for Quilt3

This guide explains how to configure AWS credentials so you can push data to S3 buckets using quilt3.

## Quick Start

### Option 1: Using AWS Credentials File (Recommended for Development)

1. Install AWS CLI:
```bash
pip install awscli
```

2. Configure your credentials interactively:
```bash
aws configure
```

This will prompt you for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region
- Default output format

Your credentials will be saved to `~/.aws/credentials`.

3. Test the connection:
```python
import boto3
boto3.client('s3').list_buckets()  # Should list your S3 buckets
```

4. Use quilt3 with your credentials:
```python
import quilt3

b = quilt3.Bucket("s3://your-bucket-name")
b.put_file("remote/path.txt", "./local/file.txt")
```

### Option 2: Using Environment Variables

Set your credentials as environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
```

Then quilt3 will automatically use these credentials in your Python code.

## For Quilt-Managed Buckets

If your bucket is managed through a Quilt catalog, you need additional authentication:

```python
import quilt3

# Configure the catalog URL (only need to run once)
quilt3.config('https://your-catalog-url.com/')

# Authenticate (opens browser for token entry)
quilt3.login()

# Now connect to your bucket
b = quilt3.Bucket("s3://your-bucket-name")
b.put_file("remote/path.txt", "./local/file.txt")
```

Check authentication status:
```python
quilt3.logged_in()  # Returns catalog URL if authenticated, None otherwise
```

## Required AWS Permissions

Make sure your AWS credentials have these S3 permissions:
- `s3:GetObject` - Read objects from S3
- `s3:PutObject` - Write/upload objects to S3
- `s3:ListBucket` - List bucket contents
- `s3:DeleteObject` - Delete objects (if needed)

## Security Best Practices

1. **Never hardcode credentials** in your code
2. **Use AWS credentials file** for local development
3. **Use environment variables** for CI/CD pipelines and containers
4. **Use IAM roles** when running on AWS infrastructure (EC2, ECS, Lambda)
5. **Restrict permissions** to only what's needed (principle of least privilege)
6. **Rotate credentials regularly**
7. **Don't commit credentials** to version control

## Verify Your Setup

Test that credentials are working:

```python
import boto3
import quilt3

# Test boto3
boto3.client('s3').list_buckets()

# Test quilt3 bucket access
b = quilt3.Bucket("s3://your-bucket-name")
b.keys()  # List contents
```

## Additional Resources

- [Quilt3 Documentation](https://docs.quilt.bio/)
- [Quilt3 Bucket API Reference](https://docs.quilt.bio/quilt-python-sdk/advanced/working-with-a-bucket)
- [Boto3 Credentials Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
