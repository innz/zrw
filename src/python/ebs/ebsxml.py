__author__ = 'cmri'

import lxml
from lxml import etree


odict = {"cvr":"CreateVolumeRequest",
          "dvr":"DeleteVolumeRequest",
          "qvr":"QueryVolumeRequest",
          "csr":"CreateSnapshotRequest",
          "dsr":"DeleteSnapshotRequest",
          "qsr":"QuerySnapshotRequest",
          "ccr":"CloneVolumeRequest",
          "ctr":"TransferVolumeRequest",
          "ctdr":"TransferDetachVolumeRequest",
          "cer":"ExpandVolumeRequest",
          "atvr":"AttachVolumeRequest",
          "dtvr":"DetachVolumeRequest"
        }

class XMLRequest(object):
    """XMLRequest"""
    xmlheader = """<?xml version="1.0" encoding="UTF-8"?>"""
    def __init__(self):
        pass

    def create_volume_request(self, size_num, user_id="admin"):
        root = etree.Element("CreateVolumeRequest")
        etree.SubElement(root, "sizeNum").text = str(size_num)
        etree.SubElement(root, "userID").text = user_id
        return self.xmlheader + etree.tostring(root)

    def delete_volume_request(self, volume_id, user_id="admin"):
        root = etree.Element("DeleteVolumeRequest")
        etree.SubElement(root, "volumeId").text = volume_id
        etree.SubElement(root, "userID").text = user_id
        return self.xmlheader + etree.tostring(root)

    def query_volume_request(self, volume_id=None, user_id=None, status=None):
        root = etree.Element("QueryVolumeRequest")
        if volume_id:
            etree.SubElement(root, "volumeId").text = volume_id
        if user_id:
            etree.SubElement(root, "userID").text = user_id
        if status:
            etree.SubElement(root, "status").text = str(status)

        return  self.xmlheader + etree.tostring(root)

    def create_snapshot_request(self, volume_id, user_id="admin"):
        root = etree.Element("CreateSnapshotRequest")
        etree.SubElement(root, "volumeId").text = volume_id
        etree.SubElement(root, "userID").text = user_id
        return self.xmlheader + etree.tostring(root)

    def delete_snapshot_request(self, snapshot_id, user_id="admin"):
        root = etree.Element("DeleteSnapshotRequest")
        etree.SubElement(root, "snapshotId").text = snapshot_id
        etree.SubElement(root, "userID").text = user_id
        return self.xmlheader + etree.tostring(root)

    def query_snapshot_request(self, volume_id, snapshot_id, user_id="admin"):
        root = etree.Element("QuerySnapshotRequest")
        etree.SubElement(root, "volumeId").text = volume_id
        etree.SubElement(root, "snapshotId").text = snapshot_id
        etree.SubElement(root, "userID").text = user_id
        return self.xmlheader + etree.tostring(root)

    def create_clone_request(self, volume_id, user_id="admin"):
        root = etree.Element("CloneVolumeRequest")
        etree.SubElement(root, "volumeId").text = volume_id
        etree.SubElement(root, "userID").text = user_id
        return self.xmlheader + etree.tostring(root)

    def attach_volume_request(self, volume_id, user_id,
                              app_node_addr, app_node_user, app_node_passwd):
        pass

    def detach_volume_request(self, volume_id, user_id,
                              app_node_addr, app_node_user, app_node_passwd,
                              force="false"):
        pass

    def extend_volume_request(self):
        pass
