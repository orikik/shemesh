define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/doc/main.js",
    "group": "C__work_shemesh_doc_doc_main_js",
    "groupTitle": "C__work_shemesh_doc_doc_main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/main.js",
    "group": "C__work_shemesh_doc_main_js",
    "groupTitle": "C__work_shemesh_doc_main_js",
    "name": ""
  },
  {
    "type": "post",
    "url": "/new_name_dir",
    "title": "Change the name of the directory",
    "name": "ChangeDir",
    "group": "Directories",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "path",
            "description": "<p>The place where you want to change the directory name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "old_name",
            "description": "<p>The name of the directory you want to change</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "new_name",
            "description": "<p>New directory name</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/directory_change_name.py",
    "groupTitle": "Directories"
  },
  {
    "type": "post",
    "url": "/get_dir",
    "title": "List of files in the directory",
    "name": "GetFilesDir",
    "group": "Directories",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "path",
            "description": "<p>Path to the directory</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name of the directory</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/directory_getNameFiles.py",
    "groupTitle": "Directories"
  },
  {
    "type": "post",
    "url": "/new_dir",
    "title": "Create a new directory",
    "name": "NewDir",
    "group": "Directories",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "path",
            "description": "<p>The place where you want to create the directory</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name of the directory</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/directory_new.py",
    "groupTitle": "Directories"
  },
  {
    "type": "post",
    "url": "/remove_dir",
    "title": "Removing directory",
    "name": "RemoveDir",
    "group": "Directories",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "path",
            "description": "<p>The place where you want to remove the directory</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name of the directory</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/directory_remove.py",
    "groupTitle": "Directories"
  },
  {
    "type": "post",
    "url": "/get_file",
    "title": "Getting the file",
    "name": "GetFile",
    "group": "Files",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "storage_path",
            "description": "<p>The place from where you want to get the file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "my_path",
            "description": "<p>A place where to save the file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name of the file</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/file_get.py",
    "groupTitle": "Files"
  },
  {
    "type": "post",
    "url": "/remove_file",
    "title": "Delete the file",
    "name": "RemoveFile",
    "group": "Files",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "storage_path",
            "description": "<p>The place where you want to delete the file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name of the file</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/file_deleting.py",
    "groupTitle": "Files"
  },
  {
    "type": "post",
    "url": "/file_update",
    "title": "Update the file",
    "name": "UpdateFile",
    "group": "Files",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "storage_path",
            "description": "<p>The place from where you want to get the file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "my_path",
            "description": "<p>The path to the file</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/file_update.py",
    "groupTitle": "Files"
  },
  {
    "type": "post",
    "url": "/upload",
    "title": "Upload the file",
    "name": "UploadFile",
    "group": "Files",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "cookie",
            "description": "<p>User cookies after authorization(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "storage_path",
            "description": "<p>A place where to save the file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "my_path",
            "description": "<p>The path to the file</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/file_upload.py",
    "groupTitle": "Files"
  },
  {
    "type": "post",
    "url": "/remove",
    "title": "User deletion",
    "name": "DelUser1",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Users name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Users password</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/remove.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/remove",
    "title": "User deletion",
    "name": "DelUser2",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cookie",
            "description": "<p>Users cookie(automatically)</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/remove.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/registration",
    "title": "New User Registration",
    "name": "GetUser",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Users name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Users password</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/register.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/login",
    "title": "User login",
    "name": "LoginUser",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Users name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Users password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "cookie",
            "description": "<p>Users cookie</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/login.py",
    "groupTitle": "User"
  },
  {
    "type": "get, post",
    "url": "/logout",
    "title": "User logout",
    "name": "LogoutUser",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cookie",
            "description": "<p>Users cookie(automatically)</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/logout.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/update",
    "title": "User update",
    "name": "UpdateUser",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cookie",
            "description": "<p>Users cookie(automatically)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "username",
            "description": "<p>Users new name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "password",
            "description": "<p>Users new password</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/update.py",
    "groupTitle": "User"
  }
] });
