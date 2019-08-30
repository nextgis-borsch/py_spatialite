#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json

version = '0.0.0'
download_url = ''
norm_version = ''

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

    version = data['info']['version']
    name = data['info']['name']
    for i in data['releases'][version]:
        if i['url'].endswith('tar.gz') or i['url'].endswith('zip'):
            download_url = i['url']
            date = i['upload_time'].replace('T', ' ') 
            norm_version = version.replace('-alpha-', '.')
            norm_version = norm_version.replace('-beta-', '.')
            norm_version = norm_version.replace('-rc-', '.')
            break

    if download_url == '':
        for i in data['releases']['2.6.2-spatialite.2.4.0-4']:
            if i['url'].endswith('tar.gz') or i['url'].endswith('zip'):
                download_url = i['url']
                date = i['upload_time'].replace('T', ' ')
                version = '2.6.2-spatialite.2.4.0-4' 
                norm_version = '2.6.2'
                break


#    download_url = data['info']['download_url']
#    date = data['releases'][version][0]['upload_time'].replace('T', ' ')

    version_file_name = os.path.join(os.path.dirname(sys.argv[1]), 'version.str')
    version_file = open(version_file_name, 'w')

    pack_name = "{}-{}-{}".format(name, norm_version, sys.argv[2])
    version_file.write("{}\n{}\n{}".format(norm_version, date, pack_name))
    version_file.close()

print download_url + ';' + norm_version + ';' + version + ';' + pack_name
