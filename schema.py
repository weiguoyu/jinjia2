# -*- coding: utf-8 -*-
"""
	Schema模块
"""

from marshmallow import Schema, fields

class EntrySchema(Schema):
	""" 文章的Schema类
	"""
	id = fields.Int()
	title = fields.Str()
	text = fields.Str()




