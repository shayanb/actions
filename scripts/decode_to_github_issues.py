# combined_script.py
import json
import sys

def decode_and_convert_to_markdown(json_payload):
    try:
        # Decode the JSON payload
        transactions_data = json.loads(json_payload)
        # transactions = transactions_data.get('result', [])
        markdown_lines = ["# Onchain Transaction Report\n"]

        # # Generate Markdown from the transactions
        # for tx in transactions:
        #     markdown_lines.append(f"## Transaction Hash: {tx['hash']}")
        #     markdown_lines.append(f"- **Block Number**: {tx['blockNumber']}")
        #     markdown_lines.append(f"- **From**: {tx['from']}")
        #     markdown_lines.append(f"- **To**: {tx['to']}")
        #     markdown_lines.append(f"- **Value**: {tx['value']} wei")
        #     markdown_lines.append(f"- **Confirmations**: {tx['confirmations']}\n")

        # Append raw data as an appendix
        markdown_lines.append("Appendix: Raw Data\n")
        markdown_lines.append("```json")
        markdown_lines.append(json.dumps(transactions_data, indent=4))
        markdown_lines.append("```")

        # Output the Markdown content
        return "\n".join(markdown_lines)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (f"An error occurred: {str(e)}")


JSON_PAYLOAD = sys.argv[1]
markdown_content = decode_and_convert_to_markdown(JSON_PAYLOAD)
print(markdown_content)  # This could be logged, saved, or used to create a GitHub issue etc.
