locals {
  app = {
    name        = "devrel-chatbot-${var.stage}"
    description = "Devrel Chatbot AI"
    zipname     = "lambda_chatbot.zip"
    handler     = "lambda_handler.lambda_handler"
  }

  lambda_policies = [
    aws_iam_policy.lambda_logging.arn,
    aws_iam_policy.lambda_dynamodb_warehouse_table.arn
  ]
  lambda_policies_map = { for idx, policy_arn in local.lambda_policies : idx => policy_arn }
}