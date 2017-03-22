from flask import Blueprint, jsonify, request


from ReservationsAclEntriesPostReqBody import ReservationsAclEntriesPostReqBody
from ReservationsPostReqBody import ReservationsPostReqBody
from ReservationsReservationIdObjectsDeleteReqBody import ReservationsReservationIdObjectsDeleteReqBody
from ReservationsReservationIdObjectsMarkPostReqBody import ReservationsReservationIdObjectsMarkPostReqBody

reservations_api = Blueprint('reservations_api', __name__)


@reservations_api.route('/reservations', methods=['POST'])
def MakeReservation():
    '''
    Make a reservation for specific amount of storage in the NOS.
    It is handler for POST /reservations
    '''
    
    inputs = ReservationsPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>', methods=['GET'])
def GetReservationInfo(reservationId):
    '''
    Get infromation about reservation. Accessible with A (admin) rights for reservation.
    It is handler for GET /reservations/<reservationId>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>', methods=['DELETE'])
def DeleteReservation(reservationId):
    '''
    Unreserve space. ALL DATA WILL BE DESTROYED.
    It is handler for DELETE /reservations/<reservationId>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects', methods=['GET'])
def GetMultipleObjects(reservationId):
    '''
    Get Multiple Objects from NOS or check CRC.
    It is handler for GET /reservations/<reservationId>/objects
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects', methods=['POST'])
def PutObjects(reservationId):
    '''
    Put one or multiple objects into storage.
    It is handler for POST /reservations/<reservationId>/objects
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects', methods=['DELETE'])
def DeleteMultipleObjects(reservationId):
    '''
    Delete multiple objects from NOS. Requester removed from consumers list. If no consumers left, objects is marked for deletion.
    It is handler for DELETE /reservations/<reservationId>/objects
    '''
    
    inputs = ReservationsReservationIdObjectsDeleteReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/exists', methods=['GET'])
def CheckExistanceForMultipleObjects(reservationId):
    '''
    Check existance of multiple objects in NOS.
    It is handler for GET /reservations/<reservationId>/objects/exists
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/mark', methods=['POST'])
def MarkKeysAsExisting(reservationId):
    '''
    PMark keys as existing. Used to create book keys in advance for bulk upload.
    It is handler for POST /reservations/<reservationId>/objects/mark
    '''
    
    inputs = ReservationsReservationIdObjectsMarkPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/<key>', methods=['GET'])
def GetObject(key, reservationId):
    '''
    Get object from NOS
    It is handler for GET /reservations/<reservationId>/objects/<key>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/<key>', methods=['DELETE'])
def DeleteObject(key, reservationId):
    '''
    Delete object from NOS. Requester removed from consumers list. If no consumers left, object is marked for deletion.
    It is handler for DELETE /reservations/<reservationId>/objects/<key>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/<key>/exist', methods=['GET'])
def CheckObjectExistance(key, reservationId):
    '''
    Check existance of the object in NOS.
    It is handler for GET /reservations/<reservationId>/objects/<key>/exist
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/keys', methods=['GET'])
def ListKeys(reservationId):
    '''
    List keys in the reservation
    It is handler for GET /reservations/<reservationId>/keys
    '''
    
    return jsonify()


@reservations_api.route('/reservations/aclEntries', methods=['GET'])
def GetACLList():
    '''
    Get full ACL list for current reservation. Requester should have A (admin) rights.
    It is handler for GET /reservations/aclEntries
    '''
    
    return jsonify()


@reservations_api.route('/reservations/aclEntries', methods=['POST'])
def CreateOrUpdateACL():
    '''
    Post new Access Control entry or edit existing one.
    It is handler for POST /reservations/aclEntries
    '''
    
    inputs = ReservationsAclEntriesPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/aclEntries/<dataSecret>', methods=['DELETE'])
def DeleteACLEntry(dataSecret):
    '''
    Delete data secret from ACL.
    It is handler for DELETE /reservations/aclEntries/<dataSecret>
    '''
    
    return jsonify()
