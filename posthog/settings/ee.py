EE_AVAILABLE = True

try:
    from ee.apps import EnterpriseConfig  # noqa: F401
except ImportError:
    pass
else:
    EE_AVAILABLE = True
