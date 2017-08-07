# Flask-Restful

### 1.安装

```
pip install Flask-Restful
```

### 2.注册组件

```
from flask_restful import Api
rest_api=Api()
rest_api.init_app(app)
```

### 3.GET/POST/PUT/DELETE请求

```python
from flask_restful import Resource
class PostApi(Resource):
    #get请求
    def get(self):
        pass
    #post请求
    def post(self):
        pass
    #put请求
    def put(self):
        pass
    #delete请求
    def delete(self):
        pass
```

### 4.注册路由

```python
rest_api.add_resource(PostApi,
                          '/api/post',
                          '/api/post/<int:post_id>',
                          endpoint='api'
                          )
```

### 5.格式化输出

```python
from flask_retful import fields,marshal_with
#构建格式
post_fields={
    'title':fields.String(),
    'text':fields.String(),
    'publish_date':fields.DateTime()
}
#注册格式
class PostApi(Resource):
    @marshal_with(post_fields)
    def get(self,post_id=None):
        if post_id:
            print(post_id)
            post=Post.objects(id=post_id).get_or_404()
            return post
        else:
            args=post_get_parser.parse_args()
            page=args['page'] or 1
            posts=Post.objects.paginate(page=page,per_page=10).items
            return posts
```

### 6.请求参数获取与限制

```python
from flask_retful import reqparse
post_get_parser=reqparse.RequestParser()
#参数名,类型限制,获取参数的位置,是否可选,错误提示
post_get_parser.add_argument(
    'page',
    type=int,
    location=['args','headers'],
    required=False,
    help='page out of index'
)
class PostApi(Resource):
    @marshal_with(post_fields)
    def get(self,post_id=None):
        if post_id:
            print(post_id)
            post=Post.objects(id=post_id).get_or_404()
            return post
        else:
            #获取参数
            args=post_get_parser.parse_args()
            page=args['page'] or 1
            posts=Post.objects.paginate(page=page,per_page=10).items
            return posts
```





