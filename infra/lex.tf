resource "aws_lex_bot" "warehouse_bot" {
  name                        = "WarehouseBot"
  description                 = "Chatbot for warehouse movements queries"
  process_behavior            = "BUILD"
  idle_session_ttl_in_seconds = 300 # 5 minutes
  enable_model_improvements   = true
  locale                      = "en-US"
  child_directed              = false

  abort_statement {
    message {
      content      = "Sorry, I couldn't process your request. Please try again."
      content_type = "PlainText"
    }
  }

  clarification_prompt {
    max_attempts = 2
    message {
      content      = "I didn't understand you. Could you please rephrase your request?"
      content_type = "PlainText"
    }
  }

  intent {
    intent_name    = aws_lex_intent.warehouse_movements.name
    intent_version = aws_lex_intent.warehouse_movements.version
  }
}

resource "aws_lex_intent" "warehouse_movements" {
  name        = "GetWarehouseMovements"
  description = "Intent to get warehouse movements for a specific date"

  sample_utterances = [
    "Get all movements for warehouse {warehouse} on {date}",
    "Show me movements for warehouse {warehouse} on {date}",
    "List all warehouse {warehouse} movements for {date}",
    "Give me all movements from warehouse {warehouse} on {date}"
  ]

  fulfillment_activity {
    type = "CodeHook"
    code_hook {
      message_version = "1.0"
      uri             = aws_lambda_function.chatbot_lambda_function.arn
    }
  }

  slot {
    name           = "warehouse"
    description    = "The warehouse identifier"
    slot_constraint = "Required"
    slot_type      = "AMAZON.AlphaNumeric"
    value_elicitation_prompt {
      max_attempts = 2
      message {
        content      = "Which warehouse are you interested in?"
        content_type = "PlainText"
      }
    }
  }

  slot {
    name           = "date"
    description    = "The date of movements"
    slot_constraint = "Required"
    slot_type      = "AMAZON.AlphaNumeric"
    value_elicitation_prompt {
      max_attempts = 2
      message {
        content      = "For which date would you like to see movements?"
        content_type = "PlainText"
      }
    }
  }
}

resource "aws_lambda_permission" "lex_invoke_permission_generic" {
  statement_id  = "AllowExecutionFromLexGeneric"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.chatbot_lambda_function.function_name
  principal     = "lex.amazonaws.com"
}