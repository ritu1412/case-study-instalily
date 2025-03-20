import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        # Open a JSON file when the spider starts
        self.file = open("output.json", "w", encoding="utf-8")
        self.file.write("[\n")
        self.first_item = True

    def close_spider(self, spider):
        # Close the JSON array and file when the spider finishes
        self.file.write("\n]")
        self.file.close()

    def process_item(self, item, spider):
        # Convert the item to a JSON string
        line = json.dumps(dict(item), ensure_ascii=False, indent=2)
        
        # Add a comma before every item except the first
        if not self.first_item:
            self.file.write(",\n")
        else:
            self.first_item = False
        
        self.file.write(line)
        return item