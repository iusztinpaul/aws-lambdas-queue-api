import os

REDIS_SETUP = {
'host' : os.environ['REDIS_ENDPOINT'],
'port': os.environ['REDIS_PORT'],
'db': 0,
}

REDIS_QUEUE_NAMESPACE = 'listeners'
REDIS_LOBBY_NAMESPACE = 'lobby'
REDIS_LOBBY_READY_FOR_LISTENER_NAMESPACE = 'ready'
REDIS_LOBBY_CREATE_FLAG = '$created$'

REDIS_MAX_LOBBY_NUMBER = 1

USER_QUERY_STRING = os.environ['USER_QUERY_STRING']
LISTENER_QUERY_STRING = 'listener'