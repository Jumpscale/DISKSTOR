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

### methods

see raml specs #TODO

```
- reserve($IYO_UID,$id,$adminSecret,$nrMB,$expirationEpoch=0, acl = ...)
	- makes a reservation for amount of storage in this NOS
	- $id is unique id (upto 16 chars) which identifies the reservation
	- $adminSecret is a unique secret given by the administrator, which allows to get the info as well as do an unreserve

- unreserve($IYO_UID,$id,$adminSecret)
	- secret needs to be the admin one
	- BE CAREFULL DATA WILL BE REMOVED

- put($IYO_UID,$secret,$reservationId,$key,$data,$consumers=[])
	- will store data with max size 1MB
	- data is stored using format defined above
	- crc will be calculated using ISA lib
	- if $consumers not in consumers bytes then add
	- if more than 10 consumers then $byte1=255 $bytes2="" \
		- this means object is permanent, cannot be deleted
	- if object marked as permanent then don't add consumers
	- if object marked for deletion $byte1=254, add consumer and active obj again
	- if key=="" then calculate md5 or blake32 hash (TODO:)
	- return capnp holding $state & $key
		- state: existed, new, deleted
- puts($IYO_UID,$secret,$reservationId,[$keys],[$data],$consumers=[])
	- same logic as put but for more objects at once
	- return capnp holding $state & $key per obj
- get($IYO_UID,$secret,$reservationId,$key,verify=True)
	- check CRC if verify == True, if wrong return
	- check if object is in deletion mode, if yes return ""
	- if it doesn't exist return "" & state NOTEXIST
	- return capnp holding $state & $data
		- state: "OK","NOTEXIST"
- gets($IYO_UID,$secret,$reservationId,[$key],verify=True)
	- return as list
- delete($IYO_UID,$secret,$reservationId,$key)
	- if not exist do nothing
	- if exists remove the consumer from the $consumers field
	- if exists & its the only consumer then mark object for deletion (do not remove!)
	- return capnp holding $state & $key
		- state: existed, new, deleted
- deletes($IYO_UID,$secret,$reservationId,[$key])
- exist($IYO_UID,$secret,$reservationId,$key)
- exists($IYO_UID,$secret,$reservationId,[$key,...])
- existsMark($IYO_UID,$secret,$reservationId,[$key,...],$consumers=[])
	- return [$keyOfNonExistingObj, ...] return the ones which did not exist yet
	- this is to be used if someone wants to upload a bulk of objects

- info($IYO_UID,$secret,$reservationId)
	- returns json of amount of storage used / expirationc/acl
	- only for admin of a reservation
- adminSet($admin_IYO_UID,$admin_IYO_UID,$secret)
	- only the NOS admin itself (user of admin group or admin (user/app)) can call this method
	- this marks in the database on key admin which UID has NOS admin rights & remembers secret
- stats($admin_IYO_UID,$secret,$reserveid)
	- returns json with
		- nr of requests per hour
		- nr of objects stored
		- size of the data
	- only NOS admin can call this

```

#### acl

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

other dbengines are: rocksdb,volume, #TODO:

### Volume backend (phase2)

- this is a special high performance backend made for HD's
- it opens HD as a volume & uses our own datastructure (see doc NOS_backend_vol.md	)
