## NOS 1.0:

- NOS = Network Object Stor
- services objects over network from a chosen data structure e.g. SophiaDB...
- is backend object stor which can be used by high level client for storing files, directories, ...

### format of object

```
- binary bytestr
- $byte1= nr of references stored, 0 means is deleted, 255 means permanent
- $bytes2 (max 160): array of 16bytes (16 bytes per consumer, = someone using data=reference)
- $bytes3 (4): CRC of payload behind
- $bytes4 (max 1MB): payload = the data
```

- consumer is IYO UID
- special $byte1's
	- 0: no consumers, marked for deletion but is still there
	- 255: permanent = cannot be deleted

### principles

- rest based network server (using go-raml to generate)
- backend sophia db & rocksdb (rocksdb for ssd, sophiadb for HD, will start with rocksdb)
- when HD then there is maximum one NOS per HD, on SSD preferably as well but can change

### 3 types of secrets

- adminSecret
	- administrator of the NOS, is set during install 
	- can be changed by the administrator itself
- reservationAdminSecret
	- is admin of a reservation
- dataSecret
	- gives RWD rights to a data in a reservation

### methods

see raml specs #TODO

```
- reserve($IYO_UID,$reservationId, $adminSecret,$nrMB,$expirationEpoch=0)
	- makes a reservation for amount of storage in this NOS
	- $reservationId is unique id (upto 16 chars) which identifies the reservation

- unreserve($IYO_UID,$id,$reservationAdminSecret)
	- BE CAREFULL DATA WILL BE REMOVED

- put($IYO_UID,$dataSecret,$reservationId,$key,$data,$consumers=[])
	- $dataSecret required to be able to write into the reservation
	- will store data with max size 1MB
	- data is stored using format defined above
	- crc will be calculated
	- if $consumers not in consumers bytes then add
	- if more than 10 consumers then $byte1=255 $bytes2="" \
		- this means object is permanent, cannot be deleted
	- if object marked as permanent then don't add consumers
	- if object marked for deletion $byte1=254, add consumer and active obj again
	- if key=="" then calculate md5 or blake32 hash (TODO:)
	- return [$state & $key]
		- state: existed, new, deleted
		
- puts($IYO_UID,$dataSecret,$reservationId,[$keys],[$data],$consumers=[])
	- same logic as put but for more objects at once
	- return [[$state,$key]]
	
- get($IYO_UID,$dataSecret,$reservationId,$key,verify=True)
	- check CRC if verify == True, if wrong return
	- check if object is in deletion mode, if yes return ""
	- if it doesn't exist return "" & state NOTEXIST
	- return $data
	- if not exist return ???
		
- gets($IYO_UID,$dataSecret,$reservationId,[$key],verify=True)
	- return as list
	- if one does not exist return ???
	
- list(($IYO_UID,$dataSecret,$reservationId)
	- list of keys in the reservation 
	
- delete($IYO_UID,$dataSecret,$reservationId,$key)
	- if not exist do nothing
	- if exists remove the consumer from the $consumers field
	- if exists & its the only consumer then mark object for deletion (do not remove!)
`	- return [$state,$key]
	
- deletes($IYO_UID,$dataSecret,$reservationId,[$key])

- exist($IYO_UID,$dataSecret,$reservationId,$key)

- exists($IYO_UID,$dataSecret,$reservationId,[$key,...])

- existsMark($IYO_UID,$dataSecret,$reservationId,[$key,...],$consumers=[])
	- return [$keyOfNonExistingObj, ...] return the ones which did not exist yet
	- this is to be used if someone wants to upload a bulk of objects

- info($IYO_UID,$dataSecret,$reservationId)
	- returns json of amount of storage used / expirationc/acl
	- only for admin of a reservation

- aclSet($IYO_UID,$adminSecret,$reservationId,$dataSecret,$right)
	- only an reservation admin itself can call this method
	- updates the acl
	- $right is RWDA . (Read Write Delete Admin)	

- actDelete($IYO_UID,$adminSecret,$reservationId,$dataSecret)
	- removes the acl info for that $dataSecret

- stats($IYO_UID,$adminSecret,$reservationId)
	- returns json with
		- nr of requests per hour
		- nr of objects stored
		- size of the data
	- only reservation admin can call this

```

#### acl

- acl:
	- is dict to $dataSecrets & rights
	- 1 $dataSecret is a unique secret key, for getting/setting/deleting data in the reserved space
	- is done per reservation

```json
{
	$secret: "RWD",
	$secret: "R",
	$secret: "A",
}
```

- rights: ```Read Write Delete Admin```


### tracking of usage

- per reservation track
-- nr of requests per hour
-- nr of objects stored
-- size of the data

### config

- yaml

```yaml
dbengine: sophiadb
maxsizemb: 1024
dbpath: /storage/db/1/
```

### implementation ideas

- rocksdb backend to start with
- api in goraml, generate the server/client
- asyncio/sanic implementation
- create tests in ays
- deployment only on top of G8OS, per disk


