from crewai_tools import BaseTool
import json

class PoseMappingTool(BaseTool):
    """
    A tool to map pose data into a structured format for 3D animation and save it to a JSON file.
    """

    def save_pose_data(self, pose_data, music_data=None, output_file='pose_mapping.json'):
        """
        Save pose data and optional music synchronization data to a JSON file.

        Args:
            pose_data: List of dictionaries with 'frame', 'position', and 'rotation' keys.
            music_data: List of dictionaries with time-stamped beats (optional).
            output_file: Filename for the output JSON file.

        Returns:
            The path to the output JSON file.
        """
        animation_data = {
            'pose_data': pose_data,
            'music_data': music_data if music_data else []
        }

        with open(output_file, 'w') as f:
            json.dump(animation_data, f, indent=4)

        return output_file

    @staticmethod
    def format_pose_data(pose_list):
        """
        Format pose data into the required structure for 3D animation.

        Args:
            pose_list: List of tuples containing (x, y, z) coordinates.

        Returns:
            A list of dictionaries formatted for 3D animation.
        """
        return [{'frame': i, 'position': {'x': x, 'y': y, 'z': z}, 'rotation': {'x': 0, 'y': 0, 'z': 0}}
                for i, (x, y, z) in enumerate(pose_list)]
