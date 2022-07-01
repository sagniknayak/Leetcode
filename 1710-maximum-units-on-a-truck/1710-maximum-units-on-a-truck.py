class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count_units = 0
        while truckSize != 0:
            max_unit_per_box = [0,0]
            for no_of_boxes, unit_per_box in boxTypes:
                if unit_per_box > max_unit_per_box[1]:
                    max_unit_per_box = [no_of_boxes, unit_per_box]
            if boxTypes == []:
                break
            elif max_unit_per_box[0] <= truckSize:
                truckSize -= max_unit_per_box[0]
                count_units += max_unit_per_box[0]*max_unit_per_box[1]
            else:
                count_units += truckSize*max_unit_per_box[1]
                truckSize = 0
            boxTypes.remove(max_unit_per_box)
                
        return count_units