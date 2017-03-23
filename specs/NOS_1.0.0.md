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

[Raml API HTML description](https://rawgit.com/Jumpscale/NOS/master/specs/api.html)
See spec draft from Kristof for historical reference: [https://github.com/Jumpscale/NOS/blob/master/specs/API_spec_draft.md](https://github.com/Jumpscale/NOS/blob/master/specs/API_spec_draft.md)


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
dbengine: rocksdb
maxsizemb: 1024
dbpath: /storage/db/1/
```

### implementation ideas

- rocksdb backend to start with
- api in goraml, generate the server/client
- asyncio/sanic implementation
- create tests in ays
- deployment only on top of G8OS, per disk


### questions/assumptions:
- We use only secrets to control access. Any user if he knows proper secret can access reservation. 
- If acess set for "" (empty) dataSecret it means reservation is open for anyone. 
- We use IYO_IDs to identify consumers. 
- Data structure contains MD5 hashes of IYO_IDs.
- On put if we put new data content with the same key, data gets rewrited but consumer list remains the same.
- For now we pass data as strings to the API.

