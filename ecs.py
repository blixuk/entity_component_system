# file: ecs.py
# Entity Component System

import shelve
from uuid import uuid4

class Scene:

	def __init__(self, scene_id=uuid4().hex):
		self.id = scene_id
		self.entities = {}
		self.componets = {}
		self.systems = {}

	def __repr__(self):
		'''return scene'''
		return f'<{self.__class__.__name__}:{self.id}>'

	def __str__(self):
		'''return scene'''
		return str(self.id)

	# Entities

	def is_entity(self, entity_id):
		'''check if an entity exist'''
		return entity_id in self.entities
	
	def is_entities(self, *entities):
		'''check if multiple entities exist'''
		for entity in entities:
			if not self.is_entity(entity.id):
				raise Exception(f"Entity '{entity.id}' doesn't exist!")
		return True

	def add_entity(self, entity):
		'''add an existing entity to the scene'''
		if not self.is_entity(entity.id):
			if self.is_components(entity):
				self.entities[entity.id] = entity
		else:
			raise Exception(f"Entity '{entity.id}' exists!")

	def create_entity(self, entity_id=uuid4().hex, **components):
		'''create a new entity in the scene'''
		entity = Entity(entity_id, components)
		self.add_entity(entity)

	def add_entity_components(self, entity_id, **components):
		'''add components to an existing entity'''
		if self.is_entity(entity_id):
			if self.is_components(**components):
				self.entities[entity_id] = components
		else:
			raise Exception(f"Entity '{entity_id}' doesn't exists!")
	
	def update_entity(self, entity_id, **components):
		if self.is_entity(entity_id):
			self.add_entity_components(entity_id, **components)
		else:
			raise Exception(f"Entity '{entity_id}' doesn't exists!")

	def list_entities(self):
		'''list all entities in the scene'''
		return list(self.entities.keys())

	def list_entity_components(self, entity_id):
		'''list all an entities components'''
		return list(self.entities[entity_id].keys())

	# Components

	def is_component(self, component_id):
		'''check if an component exist'''
		return component_id in self.componets

	def is_components(self, *components):
		'''check if multiple components exist'''
		for component in components:
			if not self.is_Component(component.id):
				raise Exception(f"Component: '{component.id}' doesn't exist!")
		return True

	def is_component_propity(self, component_id, propity_id):
		'''check if a component has an propity'''
		return propity_id in self.componets[component_id]

	def is_component_propities(self, component_id, **properties):
		'''check if a component has muliple propities'''
		for propity_id in properties:
			if not self.is_component_propity(component_id, propity_id):
				raise Exception(f"Propity: '{propity_id}' doesn't exist!")
		return True

	def add_component(self, component):
		'''add an existing component to the scene'''
		if not self.is_component(component.id):
			self.componets[component.id] = component
		else:
			raise Exception(f"Component: '{component.id}' exist!")

	def create_component(self, component_id=uuid4().hex, **components):
		'''create a new component in the scene'''
		component = Component(component_id, components)
		self.add_component(component)

	def update_component(self, component_id, **properties):
		if self.is_component(component_id):
			if self.is_component_propities(component_id, **properties):
				self.componets[component_id] = properties
		else:
			raise Exception(f"Component: '{component_id}' doesn't exist!")

	def list_components(self):
		'''list all components in the scene'''
		return list(self.componets.keys())

	def list_component_propities(self, component_id):
		'''list all propities of a component'''
		return list(self.componets[component_id].keys())

class Entity:
	
	def __init__(self, entity_id=uuid4().hex, **components):
		self.id = entity_id
		self.components = components
	
	def __repr__(self):
		'''return entity'''
		return f'<{self.__class__.__name__}:{self.id}>'

	def __str__(self):
		'''return entity components'''
		return str(self.components)

class Component:

	def __init__(self, component_id=uuid4().hex, **properties):
		self.id = component_id
		self.properties = properties

	def __repr__(self):
		'''return component'''
		return f'<{self.__class__.__name__}:{self.id}>'

	def __str__(self):
		'''return component properties'''
		return str(self.properties)

class System:

	def __init__(self, system_id=uuid4().hex, **entities):
		self.id = system_id
		self.entities = entities

	def update(self):
		raise NotImplementedError

	def __repr__(self):
		'''return system'''
		return f'<{self.__class__.__name__}:{self.id}>'

	def __str__(self):
		'''return system entities'''
		return str(self.entities)
