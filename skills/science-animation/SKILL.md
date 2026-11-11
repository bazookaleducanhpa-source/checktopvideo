---
name: science-animation
description: Design and animate original layered 2D science explainers, including vector characters, biological cutaways, diagrams, storyboards and motion studies. Use for the user's illustrated educational videos and animation requests based on the four studied references.
---

# Science animation

Use the user's four-video study as visual design guidance, not a promise of pixel-identical reproduction. Read [the drawing and motion guide](references/drawing-guide.md) before authoring; use [the evidence notes](references/video-study.md) when comparing to a reference.

## Detailed drawing and animation resources

- For constructing individual artwork, read [art recipes](references/art-recipes.md): silhouette, Bézier shapes, human faces, cells, membranes, DNA, mechanical environments, lighting and layer order.
- For source-frame comparisons, read [frame study](references/frame-study.md). It records 132 consecutive decoded frames across four references, separates observations from reconstruction hypotheses, and links local contact sheets. This is sampled research, not an exhaustive annotation of all four videos.
- For animating new artwork, read [motion recipes](references/motion-recipes.md): frame-numbered exercises, interpolation, pivots, deformation, transitions and troubleshooting. Suggested numbers are production exercises, not recovered source keyframes.
- For further local inspection, run `scripts/frame_probe.py VIDEO OUTPUT --start SECONDS --count 24`. Requires Python, Pillow and imageio-ffmpeg. It creates consecutive-frame sheets and an index manifest, refuses an existing output folder, and labels time estimates. Read the frame study for example commands and limitations.

Write user-facing teaching material in Vietnamese unless another language is requested. Give concrete construction steps and pose/timing tables when the user asks for detail; a list of animation principles alone is insufficient. Maintain separate categories for observed source features, inferred implementation and proposed original design. Reuse locally available reference media before paying for an external analysis.

## Make the idea visible

Translate the script into visible causes and effects. Each shot needs a subject, an action, a consequence and a clear focal point. A label alone is not an explanation. Reuse a visual metaphor after introducing it: a barrier, courier, signal, reward or checkpoint should retain its meaning across scenes.

Choose the appropriate visual mode rather than applying a dark neon palette everywhere:
- Human narrative: warm rooms, readable poses, restrained effects, close-ups for reactions.
- Biological mechanism: organic silhouettes, cutaways, stable color coding, particles and scale transitions.
- Abstract systems: modular geometric actors, networks and spatial groupings.
- Emotional conclusion: fewer elements, more negative space, longer visual holds.

## Production decisions

Create a small visual specification: aspect ratio, palette roles, silhouette language, shading direction, type hierarchy and a recurring character sheet. Choose dimensions from the requested destination; for ordinary landscape YouTube, 1920×1080 is a reasonable starting point, not a claimed reference specification.

Draw original assets in SVG when separate shapes must deform, rotate or change expression. Use raster images only when the intended visual requires them; a single painted image cannot substitute for a fully rigged scene. Separate joints and expressive parts. Set pivots deliberately. Give complex organisms a rigid core plus independently deformable membranes or appendages.

Choose implementation based on the deliverable. A deterministic React/Remotion composition is suitable for a rendered video; SVG/Canvas suits a small browser motion study. Use a 3D scene only if actual perspective changes justify its complexity. Check current official documentation before adding a framework. Do not imply the references were made with the chosen tool.

Before animating a full video, make a representative style frame and a short motion study. This is a production checkpoint, not a mandatory user-approval gate. Continue within the user's authorized scope. A request to learn or analyze does not itself require building a complete video.

## Motion and review

For longer animation, vary the visual construction of successive shots, not only object positions or background colors. The user specifically expects diverse scenes like the references. Plan changes in scale, camera angle, silhouette arrangement, palette role and visual mode (human action, prop close-up, mechanism, spatial journey, diagram, tissue overview). Reuse a recognizable object to connect the changes. Avoid padding duration with a two-scene loop or prolonged idle motion. Review a storyboard contact sheet for variety before rendering; choose shot lengths from the action rather than making every future shot a fixed duration.

Animate important actions first. Secondary motion must support rather than compete with them. Use gaze before head movement, head before body, and trailing motion after a stop where appropriate. Keep particles visually subordinate and make simulations reproducible with seeded randomness and frame-derived time.

A camera move must reveal scale, relationships or a new focal point. Preserve a recognizable object across scale transitions. Don't zoom the whole picture endlessly or crossfade every shot. Prefer a motivated cut, occlusion, match shape or continuous travel when the story calls for it.

Check silhouettes at thumbnail size, readability at phone size, overlap at extreme poses and motion at both normal and slow playback. Check several actual frames and the rendered sequence; a contact sheet does not establish smoothness, easing curves or audio synchronization. Report the precise inspection coverage and any unverified audio or frames.

Keep factual validation separate from animation research. On-screen graphs and medical metaphors must not make stronger claims than their supporting sources. Preserve the user's chosen subject and originality; do not reuse reference footage, branded mascots or extracted artwork as original production assets.
