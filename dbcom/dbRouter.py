class DbRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'classicmodels':
            return 'classicmodels'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'classicmodels':
            return 'classicmodels'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'classicmodels' or obj2._meta.app_label == 'classicmodels':
            return True
        elif 'classicmodels' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'classicmodels':
            return db == 'classicmodels'
        return None