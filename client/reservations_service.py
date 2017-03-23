class ReservationsService:
    def __init__(self, client):
        self.client = client



    def MakeReservation(self, data, headers=None, query_params=None):
        """
        Make a reservation for specific amount of storage in the NOS.
        It is method for POST /reservations
        """
        uri = self.client.base_url + "/reservations"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def GetReservationInfo(self, reservationId, headers=None, query_params=None):
        """
        Get infromation about reservation. Accessible with A (admin) rights for reservation.
        It is method for GET /reservations/{reservationId}
        """
        uri = self.client.base_url + "/reservations/"+reservationId
        return self.client.get(uri, headers=headers, params=query_params)


    def DeleteReservation(self, reservationId, headers=None, query_params=None):
        """
        Unreserve space. ALL DATA WILL BE DESTROYED.
        It is method for DELETE /reservations/{reservationId}
        """
        uri = self.client.base_url + "/reservations/"+reservationId
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def CreateOrUpdateACL(self, data, reservationId, headers=None, query_params=None):
        """
        Post new Access Control entry or edit existing one.
        It is method for POST /reservations/{reservationId}/aclEntries
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/aclEntries"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def GetACLList(self, reservationId, headers=None, query_params=None):
        """
        Get full ACL list for current reservation. Requester should have A (admin) rights.
        It is method for GET /reservations/{reservationId}/aclEntries
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/aclEntries"
        return self.client.get(uri, headers=headers, params=query_params)


    def DeleteACLEntry(self, dataSecret, reservationId, headers=None, query_params=None):
        """
        Delete data secret from ACL.
        It is method for DELETE /reservations/{reservationId}/aclEntries/{dataSecret}
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/aclEntries/"+dataSecret
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def ListKeys(self, reservationId, headers=None, query_params=None):
        """
        List keys in the reservation
        It is method for GET /reservations/{reservationId}/keys
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/keys"
        return self.client.get(uri, headers=headers, params=query_params)


    def DeleteMultipleObjects(self, reservationId, headers=None, query_params=None):
        """
        Delete multiple objects from NOS. Requester removed from consumers list. If no consumers left, objects is marked for deletion.
        It is method for DELETE /reservations/{reservationId}/objects
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/objects"
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def PutObjects(self, data, reservationId, headers=None, query_params=None):
        """
        Put one or multiple objects into storage.
        It is method for POST /reservations/{reservationId}/objects
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/objects"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def GetMultipleObjects(self, reservationId, headers=None, query_params=None):
        """
        Get Multiple Objects from NOS or check CRC.
        It is method for GET /reservations/{reservationId}/objects
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/objects"
        return self.client.get(uri, headers=headers, params=query_params)


    def MarkKeysAsExisting(self, data, reservationId, headers=None, query_params=None):
        """
        PMark keys as existing. Used to create book keys in advance for bulk upload.
        It is method for POST /reservations/{reservationId}/objects/mark
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/objects/mark"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def GetObject(self, key, reservationId, headers=None, query_params=None):
        """
        Get object from NOS
        It is method for GET /reservations/{reservationId}/objects/{key}
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/objects/"+key
        return self.client.get(uri, headers=headers, params=query_params)


    def DeleteObject(self, key, reservationId, headers=None, query_params=None):
        """
        Delete object from NOS. Requester removed from consumers list. If no consumers left, object is marked for deletion.
        It is method for DELETE /reservations/{reservationId}/objects/{key}
        """
        uri = self.client.base_url + "/reservations/"+reservationId+"/objects/"+key
        return self.client.session.delete(uri, headers=headers, params=query_params)
