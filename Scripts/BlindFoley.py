import bpy

# 定义场景属性以保存面板状态 (现在不需要这些属性了)
# def init_scene_properties():
#     bpy.types.Scene.video_detection_expanded = bpy.props.BoolProperty(
#         name="Expand Video Detection",
#         default=False,
#     )
#     bpy.types.Scene.sound_synthesis_expanded = bpy.props.BoolProperty(
#         name="Expand Sound Synthesis",
#         default=False,
#     )

# init_scene_properties()

class BLIND_FOLEY_PT_MainPanel(bpy.types.Panel):
    bl_label = "Blind Foley"
    bl_idname = "BLIND_FOLEY_PT_MainPanel"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Blind Foley'

    def draw(self, context):
        layout = self.layout
        # 主面板可以包含其他UI元素或保持为空

class BLIND_FOLEY_PT_VideoDetection(bpy.types.Panel):
    bl_label = "Video Detection"
    bl_idname = "BLIND_FOLEY_PT_VideoDetection"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = "BLIND_FOLEY_PT_MainPanel"  # 设置父面板ID
    bl_options = {'DEFAULT_CLOSED'}  # 默认关闭子面板

    def draw_header(self, context):
        # 不再需要在这里放置任何东西，因为我们将依赖于自动展开/折叠功能
        pass

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is where Video Detection content goes.")
        # 在这里添加 Video Detection 的内容
        # 示例操作符或属性
        # layout.operator("sequencer.some_video_operator")
        # layout.prop(scene, "some_video_property")

class BLIND_FOLEY_PT_SoundSynthesis(bpy.types.Panel):
    bl_label = "Sound Synthesis"
    bl_idname = "BLIND_FOLEY_PT_SoundSynthesis"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = "BLIND_FOLEY_PT_MainPanel"  # 设置父面板ID
    bl_options = {'DEFAULT_CLOSED'}  # 默认关闭子面板

    def draw_header(self, context):
        # 不再需要在这里放置任何东西，因为我们将依赖于自动展开/折叠功能
        pass

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is where Sound Synthesis content goes.")
        # 在这里添加 Sound Synthesis 的内容
        # 示例操作符或属性
        # layout.operator("sequencer.some_sound_operator")
        # layout.prop(scene, "some_sound_property")

def register():
    bpy.utils.register_class(BLIND_FOLEY_PT_MainPanel)
    bpy.utils.register_class(BLIND_FOLEY_PT_VideoDetection)
    bpy.utils.register_class(BLIND_FOLEY_PT_SoundSynthesis)

def unregister():
    bpy.utils.unregister_class(BLIND_FOLEY_PT_MainPanel)
    bpy.utils.unregister_class(BLIND_FOLEY_PT_VideoDetection)
    bpy.utils.unregister_class(BLIND_FOLEY_PT_SoundSynthesis)

if __name__ == "__main__":
    register()