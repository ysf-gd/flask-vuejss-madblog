from flask import Flask
from flask_cors import CORS
from config import Config

# 使用应用工厂函数创建Flask应用
def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    # enable CORS
    CORS(app)

    # 注册blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app




'''
# 传统方式
# app.py
from flask import Flask
app = Flask(__name__) # 直接创建应用实例

@app.route('/')
def index():
    return 'Hello'
# 问题：
# 1. 配置固定
# 2. 难以测试
# 3. 可能产生循环导入


# 工厂方式
# __init__.py
from flask import Flask

def create_app(config_class=None):
    app = Flask(__name__)
    
    # 可以传入不同的配置
    if config_class:
        app.config.from_object(config_class)
    
    # 注册路由
    @app.route('/')
    def index():
        return 'Hello'
    
    return app


# 使用示例：
# 开发环境
app = create_app(DevelopmentConfig)
# 测试环境
test_app = create_app(TestingConfig)
# 生产环境
prod_app = create_app(ProductionConfig)

'''