#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import orm
import models
from models import User
import asyncio


async def test():
    await orm.create_pool(loop=loop, user='root',
                          password='password', db='awesome')
    u = User(name='Test3', email='test3@example.com',
             passwd='1234567890', image='about:blank')

    await u.save()

# test()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    loop.close()
