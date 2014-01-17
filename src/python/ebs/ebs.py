#!/usr/bin/env python

import sys


from ebsctx import BCEBSContext
from restagt import ReSTFullAgent
from ebsxml import XMLRequest
from lxml import etree


baseurl = "http://192.168.34.211:8080/EBS_Management_System/rest/"
cv = "volume"
cv_url = baseurl + cv

#class BCEBSDriver(driver.VolumeDriver):
class BCEBSDriver(object):
    """Executes commands relating to BC-EBS Volumes"""
    VERSION = "1.0.0"
    def __init__(self):
        self._context = BCEBSContext()
        self._agent = ReSTFullAgent(self._context)
        self._xmlgen = XMLRequest()
        #self._parser = ResponseParser()
    def check_for_setup_error(self):
        """return an error if prerequisites are not met"""
        pass

    def create_cloned_volume(self, volume, src_vref):
        # raise NotImplementedError()
        pass

    def create_volume(self, volume):
        """create a BC-EBS volume"""
        cv_req = self._xmlgen.create_volume_request(size_num = volume["size"])
        resp, content = self._agent.send_then_recv(cv_url, cv_req, optype = "POST")
        print cv_url
        print cv_req
        print resp

        #root = etree.fromstring(content)
        #for each in root.iter():
        #    if each.tag == "volumeId":

        #        return each.text



    def create_volume_from_snapshot(self, volume, snapshot):
        """create a BC-EBS volume from a snapshot"""
        pass

    def delete_volume(self, volume):
        """delete a BC-EBS volume"""
        pass

    def copy_image_to_volume(self, context, volume, image_service, image_id):
        pass

    def create_snapshot(self, snapshot):
        """create a snapshot of BC-EBS volume"""
        pass

    def delete_snapshot(self, snapshot):
        """delete a BC-EBS snapshot"""
        pass

    def local_path(self, volume):
        pass

    def ensure_export(self, context, volume):
        """safely and synchronously recreate an export for a logical volume"""
        pass

    def create_export(self, context, volume):
        """export the volume"""
        pass

    def remove_export(self, context, volume):
        """remove an export for a logical volume"""
        pass

    def initialize_connection(self, volume, connector):
        pass

    def terminate_connection(self, volume, connector, **kwargs):
        pass

    def get_volume_stats(self, refresh=False):
        pass

    def extend_volume(self, volume, new_size):
        """extend an existing volume"""
        pass

    def backup_volume(self, context, backup, backup_service):
        """create a new backup from an existing volume"""
        raise NotImplementedError()

    def restore_backup(self, context, backup, volume, backup_service):
        """restore an existing backup to a new or existing volume"""
        raise NotImplementedError()
