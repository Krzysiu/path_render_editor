#!/usr/bin/env python3
# coding=utf-8

import inkex
from inkex import Circle, Vector2d, Polygon, PathElement
from inkex.paths import Curve, Quadratic, Move, Line

class PathRenderEditor(inkex.EffectExtension):
    """Render nodes and handles like Node Editor with checkbox options and proper defaults"""

    def add_arguments(self, pars):
        pars.add_argument("--draw_nodes", type=inkex.Boolean, default=True)
        pars.add_argument("--draw_handle_lines", type=inkex.Boolean, default=True)
        pars.add_argument("--draw_handle_circles", type=inkex.Boolean, default=True)
        pars.add_argument("--node_size", type=float, default=1.0)
        pars.add_argument("--auto_stroke", type=inkex.Boolean, default=True)
        pars.add_argument("--stroke_size", type=float, default=0.25)
        pars.add_argument("--tab", help="Active tab in GUI")

    def effect(self):
        selected_paths = self.svg.selection.filter(inkex.PathElement)
        if not selected_paths:
            raise inkex.AbortExtension("Please select at least one path object.")

        stroke_width = self.options.stroke_size
        if self.options.auto_stroke:
            stroke_width = self.options.node_size / 4

        for path_elem in selected_paths:
            if self.options.draw_nodes:
                self.draw_nodes(path_elem, stroke_width)
            if self.options.draw_handle_lines or self.options.draw_handle_circles:
                self.draw_handles(path_elem, stroke_width)

    def draw_nodes(self, path_elem, stroke_width):
        group = path_elem.getparent().add(inkex.Group(id="nodes_group"))
        group.transform = -path_elem.getparent().composed_transform()
        path = path_elem.path.transform(path_elem.composed_transform())
        size = self.svg.unittouu(f"{self.options.node_size}px")

        nodetypes_str = path_elem.get("{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}nodetypes")
        if not nodetypes_str:
            nodetypes_str = "c" * len(path)
        nodetypes = list(nodetypes_str)

        prev_point = None
        first_point = None
        nodes = []

        for i, seg in enumerate(path):
            if seg.letter == "M":
                prev_point = Vector2d(seg.end_point(Vector2d(0,0), Vector2d(0,0)))
                if first_point is None:
                    first_point = prev_point
                continue
            if prev_point is None:
                first_point = Vector2d(0,0)
                prev_point = first_point

            end = Vector2d(seg.end_point(first_point, prev_point))
            prev_point = end

            nt = nodetypes[i] if i < len(nodetypes) else "c"
            nodes.append((end, nt))

        seen = {}
        for pt, nt in nodes:
            key = (round(pt.x,3), round(pt.y,3))
            if key not in seen:
                seen[key] = nt

        half = size / 2
        for (x, y), nt in seen.items():
            if nt == "c":
                points = [(x, y-half),(x+half, y),(x, y+half),(x-half, y)]
            elif nt in ("s","z"):
                points = [(x-half,y-half),(x+half,y-half),(x+half,y+half),(x-half,y+half)]
            elif nt == "a":
                c = Circle(cx=str(x), cy=str(y), r=str(half))
                c.style = {"stroke": "#000000", "fill": "#FFFFFF", "stroke-width": str(stroke_width)}
                group.add(c)
                continue
            points_str = " ".join(f"{px},{py}" for px, py in points)
            poly = Polygon(points=points_str)
            poly.style = {"stroke": "#000000", "fill": "#FFFFFF", "stroke-width": str(stroke_width)}
            group.add(poly)

    def draw_handles(self, path_elem, stroke_width):
        group = path_elem.getparent().add(inkex.Group(id="handles_group"))
        group.transform = -path_elem.getparent().composed_transform()
        prev = Vector2d()
        start = None
        handle_dot_size = self.svg.unittouu(f"{self.options.node_size}px")

        for seg in path_elem.path.to_absolute():
            if start is None:
                start = seg.end_point(start, prev)

            def draw_handle_line(x1, y1, x2, y2):
                # ignore zero-length handles
                if (x2-x1)**2 + (y2-y1)**2 < 0.0001:
                    return
                if self.options.draw_handle_lines:
                    path_line = PathElement()
                    path_line.path = [Move(x1, y1), Line(x2, y2)]
                    path_line.style = {
                        "stroke-linejoin": "miter",
                        "stroke-linecap": "butt",
                        "stroke-width": str(stroke_width),
                        "stroke": "#000000",
                        "fill": "none",
                    }
                    group.add(path_line)
                if self.options.draw_handle_circles:
                    c = Circle(cx=str(x2), cy=str(y2), r=str(handle_dot_size/2))
                    c.style = {"stroke": "#000000", "fill": "#FFFFFF", "stroke-width": str(stroke_width)}
                    group.add(c)

            if isinstance(seg, Curve):
                draw_handle_line(prev.x, prev.y, seg.x2, seg.y2)
                draw_handle_line(seg.x4, seg.y4, seg.x3, seg.y3)
            elif isinstance(seg, Quadratic):
                draw_handle_line(prev.x, prev.y, seg.x2, seg.y2)
                draw_handle_line(seg.x3, seg.y3, seg.x2, seg.y2)

            prev = seg.end_point(start, prev)

if __name__ == "__main__":
    PathRenderEditor().run()