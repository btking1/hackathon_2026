# import action_engine
# import logger
# import output_builder
# import rule_engine
import scanner

records = scanner.scan_folder()

if records is not None:
    for record in records:
        print(record)
