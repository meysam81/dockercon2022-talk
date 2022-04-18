import abc


class BaseCache(metaclass=abc.ABCMeta):
    """
    Base class for caching.
    """

    @abc.abstractmethod
    async def get(self, key):
        """
        Get value from cache.
        :param key: key to get value from cache.
        :return: value from cache.
        """

    @abc.abstractmethod
    async def set(self, key, value, expiry: int):
        """
        Set value to cache.
        :param key: key to set value to cache.
        :param value: value to set to cache.
        """

    @abc.abstractmethod
    def delete(self, key):
        """
        Delete value from cache.
        :param key: key to delete value from cache.
        """
