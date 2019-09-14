class point:
    def __init__ (self,name,x,y,building,floor):
        self.name=name
        self.cor=(x,y)
        self.building=building
        self.floor=floor

#     static def deserialize(obj):
#         return point(obj.name, obj.cor[0], obj.cor[1], obj.building, obj.floor)

    def serialize(self):
        return {'name': self.name, 'cor': self.cor, 'building': self.building, 'floor': self.floor}

WEH_4_BR = point("WEH_4_BR",-8899521.265573261, 4930502.10545075 , 'WEH', 4)
WEH_4_ST = point("WEH_4_ST",-8899532.595407214, 4930478.221784166, 'WEH', 4)

WEH_5_NW = point("WEH_5_NW",-8899569.754751803, 4930502.827296127, 'WEH', 5)
WEH_5_NE = point("WEH_5_NE",-8899463.298251083, 4930477.217477555, 'WEH', 5)
WEH_5_SW = point("WEH_5_SW",-8899578.414170982, 4930484.515191141, 'WEH', 5)
WEH_5_SE = point("WEH_5_SE",-8899472.839163882, 4930445.330742669, 'WEH', 5)
WEH_5_ST = point("WEH_5_ST",-8899532.595407214, 4930478.221784166, 'WEH', 5)

WEH_6_NW = point("WEH_6_NW",-8899569.754751803, 4930502.827296127, 'WEH', 6)
WEH_6_NE = point("WEH_6_NE",-8899463.298251083, 4930477.217477555, 'WEH', 6)
WEH_6_SW = point("WEH_6_SW",-8899578.414170982, 4930484.515191141, 'WEH', 6)
WEH_6_SE = point("WEH_6_SE",-8899472.839163882, 4930445.330742669, 'WEH', 6)
WEH_6_ST = point("WEH_6_ST",-8899532.595407214, 4930478.221784166, 'WEH', 6)

WEH_7_NW = point("WEH_7_NW",-8899569.754751803, 4930502.827296127, 'WEH', 7)
WEH_7_NE = point("WEH_7_NE",-8899463.298251083, 4930477.217477555, 'WEH', 7)
WEH_7_SW = point("WEH_7_SW",-8899578.414170982, 4930484.515191141, 'WEH', 7)
WEH_7_SE = point("WEH_7_SE",-8899472.839163882, 4930445.330742669, 'WEH', 7)
WEH_7_ST = point("WEH_7_ST",-8899532.595407214, 4930478.221784166, 'WEH', 7)

WEH_8_NW = point("WEH_8_NW",-8899569.754751803, 4930502.827296127, 'WEH', 8)
WEH_8_NE = point("WEH_8_NE",-8899463.298251083, 4930477.217477555, 'WEH', 8)
WEH_8_SW = point("WEH_8_SW",-8899578.414170982, 4930484.515191141, 'WEH', 8)
WEH_8_SE = point("WEH_8_SE",-8899472.839163882, 4930445.330742669, 'WEH', 8)
WEH_8_ST = point("WEH_8_ST",-8899532.595407214, 4930478.221784166, 'WEH', 8)

NSH_4_WBR = point("NSH_4_WBR",-8899509.182509353, 4930549.088169376, 'NSH', 4)
NSH_4_GBR = point("NSH_4_GBR",-8899461.352407023, 4930580.347212631, 'NSH', 4)

points = [WEH_5_NW, WEH_5_NE, WEH_5_SW, WEH_5_SE, WEH_5_ST, 
            WEH_6_NW, WEH_6_NE, WEH_6_SW, WEH_6_SE, WEH_6_ST,
            WEH_7_NW, WEH_7_NE, WEH_7_SW, WEH_7_SE, WEH_7_ST,
            WEH_8_NW, WEH_8_NE, WEH_8_SW, WEH_8_SE, WEH_8_ST]

cmap = {
        WEH_4_BR:[WEH_4_ST, NSH_4_WBR],
        WEH_4_ST:[WEH_5_ST],

        WEH_5_NW:[WEH_5_ST, WEH_5_SW, WEH_5_NE],
        WEH_5_NE:[WEH_5_ST, WEH_5_NW, WEH_5_SE],
        WEH_5_SW:[WEH_5_ST, WEH_5_NW, WEH_5_SE],
        WEH_5_SE:[WEH_5_ST, WEH_5_NE, WEH_5_SW],
        WEH_5_ST:[WEH_6_ST, WEH_5_NW, WEH_5_NE, WEH_5_SW, WEH_5_SE],

        WEH_6_NW:[WEH_6_ST, WEH_6_SW, WEH_6_NE],
        WEH_6_NE:[WEH_6_ST, WEH_6_NW, WEH_6_SE],
        WEH_6_SW:[WEH_6_ST, WEH_6_NW, WEH_6_SE],
        WEH_6_SE:[WEH_6_ST, WEH_6_NE, WEH_6_SW],
        WEH_6_ST:[WEH_7_ST, WEH_5_ST, WEH_6_NW, WEH_6_NE, WEH_6_SW, WEH_6_SE],

        WEH_7_NW:[WEH_7_ST, WEH_7_SW, WEH_7_NE],
        WEH_7_NE:[WEH_7_ST, WEH_7_NW, WEH_7_SE],
        WEH_7_SW:[WEH_7_ST, WEH_7_NW, WEH_7_SE],
        WEH_7_SE:[WEH_7_ST, WEH_7_NE, WEH_7_SW],
        WEH_7_ST:[WEH_8_ST, WEH_6_ST, WEH_7_NW, WEH_7_NE, WEH_7_SW, WEH_7_SE],

        WEH_8_NW:[WEH_8_ST, WEH_8_SW, WEH_8_NE],
        WEH_8_NE:[WEH_8_ST, WEH_8_NW, WEH_8_SE],
        WEH_8_SW:[WEH_8_ST, WEH_8_NW, WEH_8_SE],
        WEH_8_SE:[WEH_8_ST, WEH_8_NE, WEH_8_SW],
        WEH_8_ST:[WEH_7_ST, WEH_8_NW, WEH_8_NE, WEH_8_SW, WEH_8_SE],

        NSH_4_WBR:[WEH_4_BR],
        NSH_4_GBR:[NSH_4_WBR]
}

def getData():
    return points, cmap