from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        kwargs['include_headers_line'] = False
        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
            kwargs['fields_to_export'] = fields_to_export

        super(CustomCsvItemExporter, self).__init__(*args, **kwargs)