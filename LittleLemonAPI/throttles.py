from rest_framework.throttling import UserRateThrottle

class WriteUserThrottle(UserRateThrottle):
    scope = 'write_user'

class WriteManagerThrottle(UserRateThrottle):
    scope = 'write_manager'

class WriteDeliveryThrottle(UserRateThrottle):
    scope = 'write_delivery'

class ReadUserThrottle(UserRateThrottle):
    scope = 'read_user'

class ReadManagerThrottle(UserRateThrottle):
    scope = 'read_manager'

class ReadDeliveryThrottle(UserRateThrottle):
    scope = 'read_delivery'