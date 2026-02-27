
A posh version of readme!
# Description

The **Render Editor** extension for Inkscape affords a most refined visualization of path nodes and their attendant handles, elegantly mirroring the venerable Node Editor. One may discern with clarity the architecture of paths, encompassing corner nodes, smooth nodes, and the distinguished auto-smooth nodes, accompanied by their delicate control handles.

<img width="1196" height="863" alt="info" src="https://github.com/user-attachments/assets/c9c83985-389b-48cd-b963-6a5be29689d0" />

Such exquisite visualization serves a variety of genteel pursuits:

- **Pedagogical demonstration**: Illuminates for neophytes the underlying construction of paths, and how the subtlety of node types influences the curvature and elegance of the vector form.  
- **Meticulous refinement**: Facilitates the identification of nodes or handles that might be askew, particularly within complex and sophisticated illustrations.  
- **Design appraisal**: Provides an instant appraisal of path structure prior to exportation or presentation, ensuring geometry that is both immaculate and harmonious.

With thoughtfully customisable options, one may elect which elements to render—nodes, handle lines, or handle termini—and regulate both the visual magnitude of nodes and the stroke thickness, rendering it suitable for dainty iconography as well as grand-scale artistic compositions.

# Installation

1. **Locate the Inkscape extensions repository**:

   - **Windows:**  
     `%APPDATA%\Inkscape\extensions`  
     (ordinarily `C:\Users\<YourUsername>\AppData\Roaming\Inkscape\extensions`)  
   - **Linux:**  
     `~/.config/inkscape/extensions/`  
   - **macOS:**  
     `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/`

2. **Deposit the artefacts**:

   Kindly place the following masterpieces within the aforementioned directory:

   - `path_render_editor.py` — the principal Python script  
   - `path_render_editor.inx` — the XML definition of the extension

3. **Reinvigorate Inkscape**:

   Close and subsequently relaunch Inkscape, thus ensuring recognition of the newly installed extension.

4. **Discover the extension**:

   You shall now encounter it under `Extensions → Visualize Path → Render Editor`.

## Parameters

- **Draw nodes** (`draw_nodes`)  
  Dictates whether nodes themselves are rendered. Upon activation, each node is depicted with aristocratic distinction:  
  - Corner nodes: diamond  
  - Smooth nodes: square  
  - Auto-smooth nodes: circle  

- **Draw handle lines** (`draw_handle_lines`)  
  Governs the depiction of handle lines for curves. Such lines are rendered solely when segments possess control points, and are prudently omitted when start and end points coincide.

- **Draw handle circles** (`draw_handle_circles`)  
  Determines whether minute circles are placed at the termini of handle lines, signifying the precise locus of control. These embellishments appear exclusively at handle extremities, not at every node.

- **Node size (px)** (`node_size`)  
  Establishes the visual magnitude of nodes. Utilised to determine the diameters of circles and the breadth of squares and diamonds. Default: `1.0 px`.

- **Stroke width (px)** (`stroke_size`)  
  Specifies the thickness of node outlines and handle lines. Considered only when automatic stroke width is not engaged. Default: `0.25 px`.

- **Auto stroke width** (`auto_stroke`)  
  When enabled, the stroke width is elegantly calculated as **¼ of the node size**, yielding a balanced and aesthetically pleasing rendering without recourse to manual adjustment.

## ☕ Patronage of the Effort

Should this instrument have saved both your time and composure whilst refining your vector illustrations, consider lending support to its continued development.

The **HOPE** philosophy dictates the creation of tools both utilitarian and gratuitous. Your support ensures their ongoing refinement and availability.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/krzysiunet)

**Every contribution is appreciated. We thank you most heartily for your participation in this cultured endeavour.**