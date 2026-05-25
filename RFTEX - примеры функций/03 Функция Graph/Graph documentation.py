import MGPH
import RFSE

MGPH.ClearGraph()

name = 'Plot 1'
ArrOx = [0, 1, 2, 3, 4]
ArrOy = [0, 1, 2, 3, 4]
LineWidth = '1'
Color = '00FFFF'
Visible = 'Yes'
MGPH.AddLine(name, ArrOy, ArrOx, LineWidth, Color, Visible)
RFSE.Report('Params_Add_Line', 'set', 'string', "name = 'Plot 1'\\narrox = [0, 1, 2, 3, 4]\\narroy = [0, 1, 2, 3, 4]\\n"
                                                "linewidth = 1\\ncolor = '00FFFF'\\nvisible = 'Yes'")
RFSE.Report('Example_Add_Line', 'set', 'string', 'graph.add_line(name, arroy, arrox, linewidth, color, visible)')

MGPH.WriteGraph()
RFSE.Report('Write_Graph', 'set', 'string', 'graph.write_graph()')

RFSE.EndScript()




