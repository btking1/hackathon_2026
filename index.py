import action_engine
import logger
import output_builder
import rule_engine
import scanner


def main():
    records = scanner.scan_folder()

    if records is None:
        print("No valid directory found.")
        return

    for record in records:
        try:
            # Run every rule in the rule engine
            for rule in rule_engine.RULES:
                record = rule(record)

            # Decide actions based on issues found
            record = action_engine.apply_rules(record)

            # Build cleaned output and get new file path
            new_path = output_builder.build_output(record)

            # Log success
            logger.log_change(
                original_path=record["path"],
                new_path=new_path,
                issues=record["issues"],
                actions=record["actions"],
                success=True,
                reason="Processed successfully",
            )

        except Exception as e:
            # Log failure
            logger.log_change(
                original_path=record.get("path", ""),
                new_path="",
                issues=record.get("issues", []),
                actions=record.get("actions", []),
                success=False,
                reason=str(e),
            )

            print(f"Error processing {record.get('name', 'unknown file')}: {e}")


if __name__ == "__main__":
    main()
