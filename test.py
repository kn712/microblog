import unittest
from app import create_app, db
from config import TestConfig
from app.models import User  

class UserModelCase(unittest.TestCase):
    def setUp(self):
        
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        # 示例测试：创建用户
        user = User(username='test', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
