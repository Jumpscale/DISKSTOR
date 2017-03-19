## UFS_NOS 1.0:

- NOS = Network Object Stor
- services objects over network from a chosen data structure e.g. SophiaDB...

### format of object (only relevant when option2)

```
- binary bytestr
- $byte1= nr of references stored, 0 means is deleted, 255 means permanent
- $bytes2 (max 160): array of 16bytes (16 bytes per consumer, = someone using data=reference)
- $bytes3 (4): CRC of payload behind
- $bytes4 (max 1MB): payload = the data
```

- consumer is IYO UID
- special $byte1's (if used the $bytes2=="")
	- 0: no consumers, marked for deletion but is still there
	- 255: permanent = cannot be deleted

### Option 1

- implemented as ARDB server on top of SSD or HD
- security
	- full access (all redis cmds)
	- R/W access when keys known (SET/GET)
- question
	- need to test which storage engine is the best to work on SSD/HD (prob different)
- how
	- some LUA stored procedures in ARDB speed up & provide some additional features
-  is a temporary solution until we have option 2

### Option 2

- network server using capnp or nanomsg in nimlang
- backend sophia db or ?
- behaviour on DB implemented in nim
- if nanomsg then create client in nim & bind to python/golang
- format of return = capnp objects (to be defined: TODO*1)

### methods

```
- reserve($IYO_UID,$id,$nrMB,$expirationEpoch=0, acl = ...)
	- makes a reservation for amount of storage in this NOS
	- $id is unique id (upto 16 chars) which identifies the reservation
- unreserve($IYO_UID,$id,$secret)
	- secret needs to be the admin one

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
