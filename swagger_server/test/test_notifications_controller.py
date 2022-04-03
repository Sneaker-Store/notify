# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.notification_status import NotificationStatus  # noqa: E501
from swagger_server.models.response_id import ResponseID  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNotificationsController(BaseTestCase):
    """NotificationsController integration test stubs"""

    def test_delete_notif(self):
        """Test case for delete_notif

        Delete scheduled notification
        """
        response = self.client.open(
            '/v1/notify/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_notif_id(self):
        """Test case for get_notif_id

        Get the status of a notification
        """
        response = self.client.open(
            '/v1/notify/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_notif(self):
        """Test case for send_notif

        Notify one or multiple e-mail adresses and/or cellphone numbers
        """
        data = Notification()
        response = self.client.open(
            '/v1/notify',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
