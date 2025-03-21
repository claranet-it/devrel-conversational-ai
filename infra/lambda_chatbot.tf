resource "aws_iam_policy" "lambda_dynamodb_warehouse_table" {
  name        = "${local.app.name}-lambda_dynamodb_warehouse_table"
  path        = "/"
  description = "IAM policy for access DynamoDB warehouse table from a lambda"
  policy      = data.aws_iam_policy_document.dynamodb_warehouse_table_full_access.json
}

resource "aws_iam_role" "lambda_exec" {
  name               = "${local.app.name}-lambda-exec"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role_policy.json
}

resource "aws_cloudwatch_log_group" "log_group" {
  name              = "/aws/lambda/${local.app.name}"
  retention_in_days = 14
}

resource "aws_iam_policy" "lambda_logging" {
  name        = "${local.app.name}-lambda_logging"
  path        = "/"
  description = "IAM policy for logging from a lambda"
  policy      = data.aws_iam_policy_document.lambda_logging.json
}

resource "aws_iam_role_policy_attachment" "lambda_policies" {
  role = aws_iam_role.lambda_exec.name

  for_each   = local.lambda_policies_map
  policy_arn = each.value
}

resource "aws_lambda_function" "chatbot_lambda_function" {
  function_name    = local.app.name
  filename         = local.app.zipname
  source_code_hash = data.archive_file.chatbot_lambda_package.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
  runtime          = "python3.12"
  handler          = local.app.handler
  timeout          = 30
}