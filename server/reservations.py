from flask import Blueprint, jsonify, request


from ReservationsAclEntriesPostReqBody import ReservationsAclEntriesPostReqBody
from ReservationsPostReqBody import ReservationsPostReqBody
from ReservationsReservationIdKeysGetReqBody import ReservationsReservationIdKeysGetReqBody
from ReservationsReservationIdObjectsBatchDeleteReqBody import ReservationsReservationIdObjectsBatchDeleteReqBody
from ReservationsReservationIdObjectsBatchExistsMarkPostReqBody import ReservationsReservationIdObjectsBatchExistsMarkPostReqBody
from ReservationsReservationIdObjectsBatchExistsPostReqBody import ReservationsReservationIdObjectsBatchExistsPostReqBody
from ReservationsReservationIdObjectsBatchPostReqBody import ReservationsReservationIdObjectsBatchPostReqBody
from ReservationsReservationIdObjectsBatchPutReqBody import ReservationsReservationIdObjectsBatchPutReqBody
from ReservationsReservationIdObjectsPostReqBody import ReservationsReservationIdObjectsPostReqBody

reservations_api = Blueprint('reservations_api', __name__)


@reservations_api.route('/reservations', methods=['POST'])
def MakeareservationforspecificamountofstorageintheNOS():
    '''
    Make a reservation for specific amount of storage in the NOS;
    It is handler for POST /reservations
    '''
    
    inputs = ReservationsPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>', methods=['GET'])
def Getinfromationaboutreservation_AccessiblewithArightsforreservation(reservationId):
    '''
    Get infromation about reservation. Accessible with A rights for reservation.
    It is handler for GET /reservations/<reservationId>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>', methods=['DELETE'])
def Unreservespace(reservationId):
    '''
    Unreserve space. ALL DATA WILL BE DESTROYED.
    It is handler for DELETE /reservations/<reservationId>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects', methods=['POST'])
def Putdataintostorage(reservationId):
    '''
    Put data into storage
    It is handler for POST /reservations/<reservationId>/objects
    '''
    
    inputs = ReservationsReservationIdObjectsPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/<key>', methods=['GET'])
def GetobjectfromNOS(key, reservationId):
    '''
    Get object from NOS
    It is handler for GET /reservations/<reservationId>/objects/<key>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/<key>', methods=['DELETE'])
def DeleteobjectfromNOS(key, reservationId):
    '''
    Delete object from NOS. Requester removed from consumers list. If no consumers left, object is marked for deletion.
    It is handler for DELETE /reservations/<reservationId>/objects/<key>
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objects/<key>/exist', methods=['GET'])
def CheckexistanceoftheobjectinNOS(key, reservationId):
    '''
    Check existance of the object in NOS.
    It is handler for GET /reservations/<reservationId>/objects/<key>/exist
    '''
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objectsBatch', methods=['POST'])
def GetmultipleobjectsfromNOS(reservationId):
    '''
    Get multiple objects from NOS
    It is handler for POST /reservations/<reservationId>/objectsBatch
    '''
    
    inputs = ReservationsReservationIdObjectsBatchPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objectsBatch', methods=['PUT'])
def Putmultipleobjectstostorage(reservationId):
    '''
    Put multiple objects to storage.
    It is handler for PUT /reservations/<reservationId>/objectsBatch
    '''
    
    inputs = ReservationsReservationIdObjectsBatchPutReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objectsBatch', methods=['DELETE'])
def DeletemultipleobjectsfromNOS(reservationId):
    '''
    Delete multiple objects from NOS. Requester removed from consumers list. If no consumers left, objects is marked for deletion.
    It is handler for DELETE /reservations/<reservationId>/objectsBatch
    '''
    
    inputs = ReservationsReservationIdObjectsBatchDeleteReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objectsBatch/exists', methods=['POST'])
def CheckexistanceofmultipleobjectsinNOS(reservationId):
    '''
    Check existance of multiple objects in NOS.
    It is handler for POST /reservations/<reservationId>/objectsBatch/exists
    '''
    
    inputs = ReservationsReservationIdObjectsBatchExistsPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/objectsBatch/exists/mark', methods=['POST'])
def Markkeysasexisting_Usedtocreatebookkeysinadvanceforbulkupload(reservationId):
    '''
    PMark keys as existing. Used to create book keys in advance for bulk upload.
    It is handler for POST /reservations/<reservationId>/objectsBatch/exists/mark
    '''
    
    inputs = ReservationsReservationIdObjectsBatchExistsMarkPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/<reservationId>/keys', methods=['GET'])
def Listkeysinthereservation(reservationId):
    '''
    List keys in the reservation
    It is handler for GET /reservations/<reservationId>/keys
    '''
    
    inputs = ReservationsReservationIdKeysGetReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/aclEntries', methods=['POST'])
def PostnewAccessControlentry():
    '''
    Post new Access Control entry.
    It is handler for POST /reservations/aclEntries
    '''
    
    inputs = ReservationsAclEntriesPostReqBody.from_json(request.get_json())
    if not inputs.validate():
        return jsonify(errors=inputs.errors), 400
    
    return jsonify()


@reservations_api.route('/reservations/aclEntries/<dataSecret>', methods=['DELETE'])
def DeletedatasecretfromACL(dataSecret):
    '''
    Delete data secret from ACL.
    It is handler for DELETE /reservations/aclEntries/<dataSecret>
    '''
    
    return jsonify()
