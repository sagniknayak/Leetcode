class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        units_per_box = {}
        for [x,y] in boxTypes:
            units_per_box[y] = units_per_box.get(y, 0) + x
        max_upb = list(units_per_box.keys())
        max_upb.sort(reverse=True)
        count_units = 0
        for upb in max_upb:
            if truckSize > units_per_box[upb]:
                count_units += upb*units_per_box[upb]
                truckSize -= units_per_box[upb]
            else:
                count_units += upb * truckSize
                truckSize = 0
                break
      
        return count_units