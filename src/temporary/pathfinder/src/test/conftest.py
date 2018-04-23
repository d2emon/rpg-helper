#! /usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import web

@pytest.fixture
def app():
    app = web.app
    return app