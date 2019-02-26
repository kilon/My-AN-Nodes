import bpy
from bpy.props import *
from mathutils import Vector
from ... base_types import AnimationNode

class cumNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_cumNode"
    bl_label = "Accumulate Node"
    bl_width_default = 200

    str_f = IntProperty(name="Reset Frame #")
    cum_v = FloatProperty(name="Cumulative Float")

    def create(self):
        self.newInput("Float","Input Plus","num_p")
        self.newInput("Float","Input Minus","num_m")
        self.newOutput("Float","Output","c_num")

    def draw(self,layout):
        layout.prop(self, "cum_v")
        layout.prop(self, "str_f")

    def execute(self,num_p,num_m):
        if bpy.context.scene.frame_current == self.str_f:
            self.cum_v = 0
        elif num_p > 0 and num_m == 0:
            self.cum_v = self.cum_v + num_p
        elif num_p == 0 and num_m > 0:
            self.cum_v = self.cum_v - num_m
        return self.cum_v
