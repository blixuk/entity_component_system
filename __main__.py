#!/usr/bin/env python

from doctest import testmod
from ecs import Scene, Entity, Component, System

if __name__ == "__main__":
	pass
	#from doctest import testmod
	#testmod()

	# # create new world for storing all entities and components
	# world = Scene('WORLD')
	# #print(world) # print world name
	# # add entities to the world
	# world.addEntity('Bob') # add a new entity named bob
	# world.addEntity() # add a new entity with a random id
	# #print(world.entities) # print all entities in the world
	# # add components to the world
	# world.addComponent('Attack', min=1, max=100) # add a new component named: Attack with propities
	# world.addComponent('Defence', min=1, max=100)
	# world.addComponent('Health', current=100, min=1, max=100)
	# #print(world.componets) # print all components in the world

	# world.addEntityWithComponents('Player', 
	# Attack={'min':5, 'max':100},
	# Defence={'min':5, 'max':100})
	# world.addEntityWithComponents('Enemy', 
	# Attack={'min':1, 'max':10},
	# Defence={'min':1, 'max':10})

	# #world.addEntityWithComponents('Enemy', Attack={'min':1, 'max':5})
	# #world.updateEntity('Bob', Attack={'min':10, 'max':100})

	# # for entity in world.entities:
	# # 	print(entity)
	# # 	for component in world.entities[entity]:
	# # 		print(f'- {component}')
	# # 		for propity in world.entities[entity][component]:
	# # 			print(f'  - {propity}: {world.entities[entity][component][propity]}')
	# # 	print()
	
	# #print(world.listEntities())
	# #print(world.listEntityComponents('Player'))
	# #print(world.listComponents())
	# #print(world.listComponentPropities('Attack'))
	
	# print(world.entities['Player'])

	# class Fight(System):
	# 	def __init__(self, entityA, entityB):
	# 		super().__init__('Fight')
	# 		self.entityA = entityA
	# 		self.entityB = entityB
	# 		self.update()
		
	# 	def update(self):
	# 		self.fight(self.entityA, self.entityB)
		
	# 	def fight(self, entityA, entityB):
	# 		entityA['Attack']['max'] = 10000
	# 		entityB['Attack']['max'] = 100

	# Fight(world.entities['Player'], world.entities['Enemy'])
	
	# print(world.entities['Player'])
	# print(world.entities['Enemy'])

	# #print(world.entities)