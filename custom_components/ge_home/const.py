"""Constants for the gehome integration."""
from gehomesdk.clients.const import LOGIN_URL

DOMAIN = "ge_home"

EVENT_ALL_APPLIANCES_READY = 'all_appliances_ready'

UPDATE_INTERVAL = 30
ASYNC_TIMEOUT = 30
MIN_RETRY_DELAY = 15
MAX_RETRY_DELAY = 1800
RETRY_OFFLINE_COUNT = 5

