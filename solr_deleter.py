#!/usr/bin/env python

import urllib2
import xml.etree.ElementTree as ET

TEN_MINUTES_IN_SECONDS = 60 * 10

XML_CONTENT_TYPE = 'application/xml'

def create_xml_delete_command(query):
    update = ET.Element('update')
    delete = ET.SubElement(update, 'delete')
    query_element = ET.SubElement(delete, 'query')
    query_element.text = query
    commit = ET.SubElement(update, 'commit')
    return ET.tostring(update)

def delete_by_query_xml(url, query):
    content_type_header = {'Content-Type': XML_CONTENT_TYPE}
    delete_command = create_xml_delete_command(query)
    request = urllib2.Request(url, delete_command, content_type_header)
    try:
        response = urllib2.urlopen(request, None, TEN_MINUTES_IN_SECONDS)
    except urllib2.HTTPError as e:
        print e.read()
        raise
    else:
        try:
            response_string = response.read()
            print response_string
        finally:
            response.close()

if __name__ == "__main__":
    from sys import argv
    delete_by_query_xml(argv[1], argv[2])
