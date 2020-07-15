<div class="container">

<div class="row">

<div class="col-md-9" role="main">

<div class="page-header">

# Shopping API documentation <small>version 1</small>

http://example.com/{version}

*   **version**: _<span class="required">required</span>(1)_

### [Welcome](#welcome)

Welcome to the Shopping API Documentation. This API allows you to interact with a DB to store recipes an their ingredients.

</div>

<div class="panel panel-default">

<div class="panel-heading">

### /units

</div>

<div class="panel-body">

<div class="top-resource-description">

URI for everything related to the Units class.

</div>

<div class="panel-group">

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent"></span>/units](#panel_units) <span class="methods">[<span class="badge badge_get">get</span>](#units_get) [<span class="badge badge_post">post</span>](#units_post) [<span class="badge badge_delete">delete</span>](#units_delete)</span>

</div>

<div id="panel_units" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#units_get'" class="list-group-item"><span class="badge badge_get">get</span></div>

<div onclick="window.location.href = '#units_post'" class="list-group-item"><span class="badge badge_post">post</span></div>

<div onclick="window.location.href = '#units_delete'" class="list-group-item"><span class="badge badge_delete">delete</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="units_get">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_get">get</span> <span class="parent"></span>/units

</div>

<div class="modal-body">

*   [Response](#units_get_response)

<div class="tab-content">

<div class="tab-pane active" id="units_get_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "type": "array",
      "items": {
        "type": "string"
      }
    }

**Example**:

<div class="examples">

    [
      "slices",
      "floz",
      "tons",
      "tbsp",
      "cubic_meters"
    ]

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="units_post">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_post">post</span> <span class="parent"></span>/units

</div>

<div class="modal-body">

*   [Request](#units_post_request)
*   [Response](#units_post_response)

<div class="tab-content">

<div class="tab-pane active" id="units_post_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
          "units": {"type": ["string", "array"]}
      }
    }

**Example**:

<div class="examples">

    {
      "units": "g"
    }

</div>

</div>

<div class="tab-pane" id="units_post_response">

## HTTP status code [201](http://httpstatus.es/201)

### Body

**Media type**: application/json

**Type**:

    {
      "units": [
          "g"
      ]
    }

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="units_delete">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_delete">delete</span> <span class="parent"></span>/units

</div>

<div class="modal-body">

*   [Request](#units_delete_request)
*   [Response](#units_delete_response)

<div class="tab-content">

<div class="tab-pane active" id="units_delete_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
          "units": {"type": ["string", "array"]}
      }
    }

**Example**:

<div class="examples">

    {
      "units": "g"
    }

</div>

</div>

<div class="tab-pane" id="units_delete_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "units": [
          "g"
      ]
    }

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="panel panel-default">

<div class="panel-heading">

### /supermarkets

</div>

<div class="panel-body">

<div class="top-resource-description">

URI for everything related to the Supermarket class.

</div>

<div class="panel-group">

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent"></span>/supermarkets](#panel_supermarkets) <span class="methods">[<span class="badge badge_get">get</span>](#supermarkets_get) [<span class="badge badge_post">post</span>](#supermarkets_post) [<span class="badge badge_delete">delete</span>](#supermarkets_delete)</span>

</div>

<div id="panel_supermarkets" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#supermarkets_get'" class="list-group-item"><span class="badge badge_get">get</span></div>

<div onclick="window.location.href = '#supermarkets_post'" class="list-group-item"><span class="badge badge_post">post</span></div>

<div onclick="window.location.href = '#supermarkets_delete'" class="list-group-item"><span class="badge badge_delete">delete</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="supermarkets_get">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_get">get</span> <span class="parent"></span>/supermarkets

</div>

<div class="modal-body">

*   [Response](#supermarkets_get_response)

<div class="tab-content">

<div class="tab-pane active" id="supermarkets_get_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "type": "array",
      "items": {
        "type": "string"
      }
    }

**Example**:

<div class="examples">

    [
      "edeka",
      "aldi"
    ]

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="supermarkets_post">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_post">post</span> <span class="parent"></span>/supermarkets

</div>

<div class="modal-body">

*   [Request](#supermarkets_post_request)
*   [Response](#supermarkets_post_response)

<div class="tab-content">

<div class="tab-pane active" id="supermarkets_post_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
          "supermarkets": {"type": ["string", "array"]}
      }
    }

**Example**:

<div class="examples">

    {
      "supermarkets": "aldi"
    }

</div>

</div>

<div class="tab-pane" id="supermarkets_post_response">

## HTTP status code [201](http://httpstatus.es/201)

### Body

**Media type**: application/json

**Type**:

    {
      "supermarkets": [
          "aldi"
      ]
    }

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="supermarkets_delete">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_delete">delete</span> <span class="parent"></span>/supermarkets

</div>

<div class="modal-body">

*   [Request](#supermarkets_delete_request)
*   [Response](#supermarkets_delete_response)

<div class="tab-content">

<div class="tab-pane active" id="supermarkets_delete_request">

### Body

**Media type**: application/json

**Type**:

    {
    "type": "object",
      "properties": {
          "supermarkets": {"type": ["string", "array"]}
      }
    }

**Example**:

<div class="examples">

    {
      "supermarkets": "aldi"
    }

</div>

</div>

<div class="tab-pane" id="supermarkets_delete_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "supermarkets": [
          "aldi"
      ]
    }

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="panel panel-default">

<div class="panel-heading">

### /ingredients

</div>

<div class="panel-body">

<div class="top-resource-description">

URI for everything related to the Ingredients class.

</div>

<div class="panel-group">

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent">/ingredients</span>/all](#panel_ingredients_all) <span class="methods">[<span class="badge badge_get">get</span>](#ingredients_all_get)</span>

</div>

<div id="panel_ingredients_all" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#ingredients_all_get'" class="list-group-item"><span class="badge badge_get">get</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="ingredients_all_get">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_get">get</span> <span class="parent">/ingredients</span>/all

</div>

<div class="modal-body">

*   [Response](#ingredients_all_get_response)

<div class="tab-content">

<div class="tab-pane active" id="ingredients_all_get_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "name": {"type": "string"},
          "category": {"type": "string"},
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Onion",
        "category": "Vegetable/Fruit",
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      },
      "-M9HqlUQnD7MS-DS53cKJ": {
        "name": "...",
        "category": "...",
        "supermarkets": [],
        "units": []
      },
      "-M9HqlUQnD7MS-LKH4c8": {},
      "-M9HqlUQnHJGF-5KJHF4": {}
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent">/ingredients</span>/single](#panel_ingredients_single) <span class="methods">[<span class="badge badge_get">get</span>](#ingredients_single_get) [<span class="badge badge_post">post</span>](#ingredients_single_post) [<span class="badge badge_put">put</span>](#ingredients_single_put) [<span class="badge badge_delete">delete</span>](#ingredients_single_delete)</span>

</div>

<div id="panel_ingredients_single" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#ingredients_single_get'" class="list-group-item"><span class="badge badge_get">get</span></div>

<div onclick="window.location.href = '#ingredients_single_post'" class="list-group-item"><span class="badge badge_post">post</span></div>

<div onclick="window.location.href = '#ingredients_single_put'" class="list-group-item"><span class="badge badge_put">put</span></div>

<div onclick="window.location.href = '#ingredients_single_delete'" class="list-group-item"><span class="badge badge_delete">delete</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="ingredients_single_get">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_get">get</span> <span class="parent">/ingredients</span>/single

</div>

<div class="modal-body">

*   [Request](#ingredients_single_get_request)
*   [Response](#ingredients_single_get_response)

<div class="tab-content">

<div class="tab-pane active" id="ingredients_single_get_request">

### Query Parameters

*   **id**: _<span class="required">required</span>(string)_

</div>

<div class="tab-pane" id="ingredients_single_get_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "name": {"type": "string"},
          "category": {"type": "string"},
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Onion",
        "category": "Vegetable/Fruit",
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      }
    }

</div>

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="ingredients_single_post">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_post">post</span> <span class="parent">/ingredients</span>/single

</div>

<div class="modal-body">

*   [Request](#ingredients_single_post_request)
*   [Response](#ingredients_single_post_response)

<div class="tab-content">

<div class="tab-pane active" id="ingredients_single_post_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
          "name": {"type": "string"},
          "units": {"type": ["array", "string"]},
          "supermarkets": {"type": ["array", "string"]},
          "category": {"type": "string"}
      }
    }

**Example**:

<div class="examples">

    {
      "name": "pepper",
      "units": "tsp",
      "supermarkets": "chinos",
      "category": "spices"
    }

</div>

</div>

<div class="tab-pane" id="ingredients_single_post_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "name": {"type": "string"},
          "category": {"type": "string"},
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Onion",
        "category": "Vegetable/Fruit",
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      }
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

## HTTP status code [409](http://httpstatus.es/409)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 409,
      "message": "The element already exists in the database"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="ingredients_single_put">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_put">put</span> <span class="parent">/ingredients</span>/single

</div>

<div class="modal-body">

*   [Request](#ingredients_single_put_request)
*   [Response](#ingredients_single_put_response)

<div class="tab-content">

<div class="tab-pane active" id="ingredients_single_put_request">

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "supermarkets": [
          "Aldi"
        ],
        "units": [
          "u"
        ]
      }
    }

</div>

</div>

<div class="tab-pane" id="ingredients_single_put_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      }
    }

</div>

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="ingredients_single_delete">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_delete">delete</span> <span class="parent">/ingredients</span>/single

</div>

<div class="modal-body">

*   [Request](#ingredients_single_delete_request)
*   [Response](#ingredients_single_delete_response)

<div class="tab-content">

<div class="tab-pane active" id="ingredients_single_delete_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
        "id": {"type": "string"}
      }
    }

**Example**:

<div class="examples">

    {
      "id": "-M9HqlUQnD7MS-W6kySH"
    }

</div>

</div>

<div class="tab-pane" id="ingredients_single_delete_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "name": {"type": "string"},
          "category": {"type": "string"},
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Onion",
        "category": "Vegetable/Fruit",
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      }
    }

</div>

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="panel panel-default">

<div class="panel-heading">

### /recipes

</div>

<div class="panel-body">

<div class="top-resource-description">

URI for everything related to the Recipes class

</div>

<div class="panel-group">

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent">/recipes</span>/all](#panel_recipes_all) <span class="methods">[<span class="badge badge_get">get</span>](#recipes_all_get)</span>

</div>

<div id="panel_recipes_all" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#recipes_all_get'" class="list-group-item"><span class="badge badge_get">get</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="recipes_all_get">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_get">get</span> <span class="parent">/recipes</span>/all

</div>

<div class="modal-body">

*   [Response](#recipes_all_get_response)

<div class="tab-content">

<div class="tab-pane active" id="recipes_all_get_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Recipes response",
      "type": "object",
      "patternProperties": {
        "^.*$": {
          "properties": {
            "name": {"type": "string"},
            "description": {"type": "string"},
            "link": {"type": "string"},
            "ingredients": {
              "type": "object",
              "patternProperties": {
                "^.*$": {
                  "anyOf": [{"type": "object"}],
                  "properties": {
                    "quantity": {"type": "number"},
                    "units": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Pizza",
        "description": "Aldi pizza with home vegetables",
        "link": "http://www.mypizza.com",
        "ingredients": {
          "-M9HqlJkjgu85S-HGbl58": {
            "quantity": 2,
            "units": "g"
          }
        }
      },
      "-M9HqlUQnD7MS-DS53cKJ": {
        "name": "...",
        "description": "...",
        "link": "...",
        "ingredients": {}
      },
      "-M9HqlUQnD7MS-LKH4c8": {},
      "-M9HqlUQnHJGF-5KJHF4": {}
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent">/recipes</span>/single](#panel_recipes_single) <span class="methods">[<span class="badge badge_get">get</span>](#recipes_single_get) [<span class="badge badge_post">post</span>](#recipes_single_post) [<span class="badge badge_put">put</span>](#recipes_single_put) [<span class="badge badge_delete">delete</span>](#recipes_single_delete)</span>

</div>

<div id="panel_recipes_single" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#recipes_single_get'" class="list-group-item"><span class="badge badge_get">get</span></div>

<div onclick="window.location.href = '#recipes_single_post'" class="list-group-item"><span class="badge badge_post">post</span></div>

<div onclick="window.location.href = '#recipes_single_put'" class="list-group-item"><span class="badge badge_put">put</span></div>

<div onclick="window.location.href = '#recipes_single_delete'" class="list-group-item"><span class="badge badge_delete">delete</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="recipes_single_get">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_get">get</span> <span class="parent">/recipes</span>/single

</div>

<div class="modal-body">

*   [Request](#recipes_single_get_request)
*   [Response](#recipes_single_get_response)

<div class="tab-content">

<div class="tab-pane active" id="recipes_single_get_request">

### Query Parameters

*   **id**: _<span class="required">required</span>(string)_

</div>

<div class="tab-pane" id="recipes_single_get_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Recipes response",
      "type": "object",
      "patternProperties": {
        "^.*$": {
          "properties": {
            "name": {"type": "string"},
            "description": {"type": "string"},
            "link": {"type": "string"},
            "ingredients": {
              "type": "object",
              "patternProperties": {
                "^.*$": {
                  "anyOf": [{"type": "object"}],
                  "properties": {
                    "quantity": {"type": "number"},
                    "units": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Pizza",
        "description": "Aldi pizza with home vegetables",
        "link": "http://www.mypizza.com",
        "ingredients": {
          "-M9HqlJkjgu85S-HGbl58": {
            "quantity": 2,
            "units": "g"
          },
          "-M9HqlUQnD7MS-DS53cKJ": {
            "quantity": 5,
            "units": "cups"
          },
          "-M9HqlUQnD7MS-LKH4c8": {},
          "-M9HqlUQnHJGF-5KJHF4": {}
        }
      }
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="recipes_single_post">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_post">post</span> <span class="parent">/recipes</span>/single

</div>

<div class="modal-body">

*   [Request](#recipes_single_post_request)
*   [Response](#recipes_single_post_response)

<div class="tab-content">

<div class="tab-pane active" id="recipes_single_post_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "link": {"type": "string"},
        "ingredients": {
          "patternProperties": {
            "^.*$": {
              "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "link": {"type": "string"},
                "ingredients": {
                  "type": "object",
                  "patternProperties": {
                    "^.*$": {
                      "anyOf": [{"type": "object"}],
                      "properties": {
                        "quantity": {"type": "number"},
                        "units": {"type": "string"}
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "new_ingredients": {
          "type": "array",
          "items": {
            "properties": {
              "name": {"type": "string"},
              "category": {"type": "string"},
              "supermarkets": {"type": "string"},
              "quantity": {"type": "number"},
              "units": {"type": "string"}
            }
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "name": "Pizza",
      "description": "Supermarket pizza with home vegetables",
      "link": "http://www.mypizza.com",
      "ingredients": {
        "-M9HqlJkjgu85S-HGbl58": {
          "quantity": 2,
          "units": "g"
        },
        "-M9HqlUQnD7MS-DS53cKJ": {
          "quantity": 5,
          "units": "cups"
        },
        "-M9HqlUQnD7MS-LKH4c8": {
          "quantity": 7,
          "units": "hand"
        },
        "-M9HqlUQnHJGF-5KJHF4": {
          "quantity": 4,
          "units": "piles"
        }
      },
      "new_ingredients": [
        {
          "name": "Onion",
          "category": "Vegetables/Fruits",
          "supermarkets": "aldi",
          "quantity": 4,
          "units": "piles"
        },
        {
          "name": "Tomato",
          "category": "Vegetables/Fruits",
          "supermarkets": "aldi",
          "quantity": 7,
          "units": "tons"
        }
      ]
    }

</div>

</div>

<div class="tab-pane" id="recipes_single_post_response">

## HTTP status code [201](http://httpstatus.es/201)

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "link": {"type": "string"},
        "ingredients": {
          "patternProperties": {
            "^.*$": {
              "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "link": {"type": "string"},
                "ingredients": {
                  "type": "object",
                  "patternProperties": {
                    "^.*$": {
                      "anyOf": [{"type": "object"}],
                      "properties": {
                        "quantity": {"type": "number"},
                        "units": {"type": "string"}
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "new_ingredients": {
          "type": "array",
          "items": {
            "properties": {
              "name": {"type": "string"},
              "category": {"type": "string"},
              "supermarkets": {"type": "string"},
              "quantity": {"type": "number"},
              "units": {"type": "string"}
            }
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "name": "Pizza",
      "description": "Supermarket pizza with home vegetables",
      "link": "http://www.mypizza.com",
      "ingredients": {
        "-M9HqlJkjgu85S-HGbl58": {
          "quantity": 2,
          "units": "g"
        },
        "-M9HqlUQnD7MS-DS53cKJ": {
          "quantity": 5,
          "units": "cups"
        },
        "-M9HqlUQnD7MS-LKH4c8": {
          "quantity": 7,
          "units": "hands"
        },
        "-M9HqlUQnHJGF-5KJHF4": {
          "quantity": 4,
          "units": "piles"
        }
      },
      "new_ingredients": [
        {
          "name": "Onion",
          "category": "Vegetables/Fruits",
          "supermarkets": "aldi",
          "quantity": 4,
          "units": "piles"
        },
        {
          "name": "Tomato",
          "category": "Vegetables/Fruits",
          "supermarkets": "aldi",
          "quantity": 7,
          "units": "tons"
        }
      ]
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="recipes_single_put">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_put">put</span> <span class="parent">/recipes</span>/single

</div>

<div class="modal-body">

*   [Request](#recipes_single_put_request)
*   [Response](#recipes_single_put_response)

<div class="tab-content">

<div class="tab-pane active" id="recipes_single_put_request">

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "supermarkets": [
          "Aldi"
        ],
        "units": [
          "u"
        ]
      }
    }

</div>

</div>

<div class="tab-pane" id="recipes_single_put_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      }
    }

</div>

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="recipes_single_delete">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_delete">delete</span> <span class="parent">/recipes</span>/single

</div>

<div class="modal-body">

*   [Request](#recipes_single_delete_request)
*   [Response](#recipes_single_delete_response)

<div class="tab-content">

<div class="tab-pane active" id="recipes_single_delete_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
        "id": {"type": "string"}
      }
    }

**Example**:

<div class="examples">

    {
      "id": "-M9HqlUQnD7MS-W6kySH"
    }

</div>

</div>

<div class="tab-pane" id="recipes_single_delete_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "title": "Ingredients response",
      "type": "object",
      "patternProperties": {
      "^.*$": {
        "properties": {
          "name": {"type": "string"},
          "category": {"type": "string"},
          "supermarkets": {"type": "array"},
          "units": {"type": "array"}
          }
        }
      }
    }

**Example**:

<div class="examples">

    {
      "-M9HqlUQnD7MS-W6kySH": {
        "name": "Onion",
        "category": "Vegetable/Fruit",
        "supermarkets": [
          "Aldi",
          "Edeka"
        ],
        "units": [
          "u",
          "g"
        ]
      }
    }

</div>

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

## HTTP status code [404](http://httpstatus.es/404)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "Reference not found in the data base"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="panel panel-white resource-modal">

<div class="panel-heading">

#### [<span class="parent">/recipes</span>/summary](#panel_recipes_summary) <span class="methods">[<span class="badge badge_post">post</span>](#recipes_summary_post)</span>

</div>

<div id="panel_recipes_summary" class="panel-collapse collapse">

<div class="panel-body">

<div class="list-group">

<div onclick="window.location.href = '#recipes_summary_post'" class="list-group-item"><span class="badge badge_post">post</span></div>

</div>

</div>

</div>

<div class="modal fade" tabindex="0" id="recipes_summary_post">

<div class="modal-dialog modal-lg">

<div class="modal-content">

<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>

#### <span class="badge badge_post">post</span> <span class="parent">/recipes</span>/summary

</div>

<div class="modal-body">

*   [Request](#recipes_summary_post_request)
*   [Response](#recipes_summary_post_response)

<div class="tab-content">

<div class="tab-pane active" id="recipes_summary_post_request">

### Body

**Media type**: application/json

**Type**:

    {
      "type": "object",
      "properties": {
        "recipes_ids": {
            "type": "array",
            "items": {"type": "string"}
        }
      }
    }

**Example**:

<div class="examples">

    {
      "recipes_ids": [
        "-M9vmiffPqRjN3zZwFyN",
        "-M9vnZ4nYZ5sJXcariko"
      ]
    }

</div>

</div>

<div class="tab-pane" id="recipes_summary_post_response">

## HTTP status code [200](http://httpstatus.es/200)

### Body

**Media type**: application/json

**Type**:

    {
      "patternProperties": {
        "^.*$": {
          "type": "number"
        }
      }
    }

**Examples**:

<div class="examples">

**banana tons**:  

    14

**ham slices**:  

    4

**oregano tbsp**:  

    7

**pinaple floz**:  

    4

**pinaple u**:  

    4

</div>

## HTTP status code [400](http://httpstatus.es/400)

### Body

**Media type**: application/json

**Type**: object

**Properties**

*   **message**: _<span class="required">required</span>(string)_
*   **code**: _<span class="required">required</span>(number)_

**Example**:

<div class="examples">

    {
      "code": 400,
      "message": "'u' is not of type 'array'"
    }

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="col-md-3">

<div id="sidebar" class="hidden-print affix" role="complementary">

*   [/units](#units)
*   [/supermarkets](#supermarkets)
*   [/ingredients](#ingredients)
*   [/recipes](#recipes)

</div>

</div>

</div>

</div>