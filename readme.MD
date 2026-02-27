# Description

The **Render Editor** extension for Inkscape visualizes the nodes and handles of selected paths, mimicking the appearance of the built-in Node Editor. It allows you to clearly see the structure of paths, including corners, smooth points, and auto-smooth points, along with the control handles for curves.  

This visualization is useful for several purposes:  

- **Learning and tutorials**: Helps beginners understand how paths are constructed and how node types affect the shape of curves.  
- **Precision editing**: Makes it easier to spot misplaced nodes or handles, especially in complex vector illustrations.  
- **Design review**: Quickly assess the structure of paths before exporting or sharing, ensuring clean and consistent geometry.  

With customizable options, you can choose which elements to render (nodes, handle lines, handle ends) and control the visual size and stroke thickness, making it adaptable for both small icons and large-scale illustrations.

# Installing

1. **Locate your Inkscape extensions folder**:

   - **Windows:**  
     `%APPDATA%\Inkscape\extensions`  
     (zwykle `C:\Users\<YourUsername>\AppData\Roaming\Inkscape\extensions`)
   - **Linux:**  
     `~/.config/inkscape/extensions/`
   - **macOS:**  
     `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/`

2. **Copy files**:

   Place the following files into the extensions folder:

   - `path_render_editor.py` (the main Python script)
   - `path_render_editor.inx` (the XML extension definition)

3. **Restart Inkscape**:

   Close and reopen Inkscape so it recognizes the new extension.

4. **Access the extension**:

   You can now find it in Inkscape under `Extensions → Visualize Path → Render Editor`

## Parameters

- **Draw nodes** (`draw_nodes`)  
  Toggle whether the nodes themselves are drawn. When enabled, each node is rendered according to its type:
  - Corner nodes: diamond
  - Smooth nodes: square
  - Auto-smooth nodes: circle  

- **Draw handle lines** (`draw_handle_lines`)  
  Toggle whether the handles (control lines for curves) are drawn. Handles are only rendered if a segment has control points, and lines are not drawn when start and end points coincide.

- **Draw handle circles** (`draw_handle_circles`)  
  Toggle whether small circles are drawn at the end of handle lines. These indicate the exact handle positions. Circles are drawn only at handle ends, not on every node.

- **Node size (px)** (`node_size`)  
  Sets the visual size of nodes. The value is used to determine the diameter of circles and the size of squares/diamonds. Default is `1.0 px`.

- **Stroke width (px)** (`stroke_size`)  
  Sets the thickness of node outlines and handle lines. This parameter is used only if automatic stroke width is not applied. Default is `0.25 px`.

- **Auto stroke width** (`auto_stroke`)  
  When enabled, the stroke width for nodes and handles is automatically set to **¼ of the node size**. This produces visually balanced rendering without requiring manual adjustment.

## ☕ Support the effort
If this tool saved your time (and your sanity) while cleaning up your photo library, consider supporting the development. 

The **HOPE** philosophy means I build tools that are helpful and free. Your support helps me keep it that way!

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/krzysiunet)

**Every bit helps. Thanks for being part of the community!**