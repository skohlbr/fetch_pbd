#!/usr/bin/env python
'''Abstract class defining an interface to primitives
'''

from abc import ABCMeta, abstractmethod

class Primitive:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def build_from_json(self, json):
        pass

    @abstractmethod
    def get_json(self):
        pass

    @abstractmethod
    def get_pre_condition(self):
        pass

    @abstractmethod
    def get_post_condition(self):
        pass

    @abstractmethod
    def make_marker(self, click_cb, delete_cb, pose_change_cb):
        pass

    @abstractmethod
    def delete_marker(self):
        pass

    @abstractmethod
    def update_ref_frames(self):
        pass

    @abstractmethod
    def get_ref_name(self):
        pass

    @abstractmethod
    def is_control_visible(self):
        pass

    @abstractmethod
    def set_control_visible(self, visible=True):
        pass

    @abstractmethod
    def update_viz(self):
        pass

    @abstractmethod
    def get_primitive_number(self):
        pass

    @abstractmethod
    def set_primitive_number(self):
        pass

    @abstractmethod
    def is_object_required(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def is_reachable(self):
        pass

    @abstractmethod
    def get_absolute_position(self, use_final=True):
        pass

    @abstractmethod
    def decrease_id(self):
        pass

    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


