<h1 align="center">Image management system</h1>

## API calls
All calls except calls to crate_user/ enpoint should be authorized using headers = {'Authorization': 'Bearer your token'}


### Create new Image instance `images/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d     "{'id':id, 'image':image}"
"<hostname>/api/v1/images/?id=instance's id"
```
Response:

```
{
    "message": "The Image instance has been created"
}
```


### Create new User instance `crate_user/` 

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d     "{'admin':True}"
"<hostname>/api/v1/crate_user"
```

Response:

```
{
    "Token": "179965567450641667934392721119362596563"
}
```

### Retrieve all Images's instances `images/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/images"
```

Response:

```
[
{'id': 1, 'image': '/media/test.jpg'}  - can be retrieved on <hostname>/media/test.jpg"
]
```

### Delete Image instance `images/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/images/?id=instance's id"
```

Response:

```
{
    "message": "The Image instance with id 4 has been deleted"
}
```

### Update Image instance `images/?id=instance's id`

Method: `PUT`

```
curl -XPUT
-H "Content-Type: application/json"
-d     "{'id':id, 'image':image}"
"<hostname>/api/v1/images/?id=instance's id"
```
Response:

```
{
    "message": "The Image instance with id 4 has been updated"
}
```

### Delete All Image instances `delete_images/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
"<hostname>/api/v1/delete_images"
```
Response:

```
{
    "message": "All Image instances have been deleted"
}
```