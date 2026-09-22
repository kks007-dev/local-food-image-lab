# Hyper-specific realistic food photography prompts

## Prompt recipe

Write one coherent description in this order:

1. **Hero subject and identity** — exact dish, ingredients, doneness, cut, and temperature cues.
2. **Plating geometry** — vessel, camera-facing orientation, negative space, garnish placement, and portion scale.
3. **Material detail** — crisp edges, pores, crumb, browning, gloss, condensation, sauce viscosity, and believable contact shadows.
4. **Surface and setting** — table material, napkin/utensil placement, background distance, and restrained color palette.
5. **Light** — direction, size, softness, color temperature, highlight behavior, and shadow density.
6. **Camera language** — editorial food photograph, focal length, aperture, focus plane, depth of field, and angle.
7. **Realism constraints** — natural asymmetry, tiny imperfections, physically plausible reflections, and no distracting props.

## Reusable template

`A photorealistic editorial food photograph of [dish], [exact ingredients and preparation], plated [geometry] in/on [vessel]. Show [3–6 material cues]. The scene is on [surface] with [minimal supporting props]. Light from [direction] with [modifier/softness], producing [highlight/shadow behavior]. Shot at [angle] on an [focal length] lens, [aperture], focus on [specific plane], shallow but believable depth of field. Natural asymmetry, realistic moisture and contact shadows, subtle imperfections, restrained color grade, high micro-contrast, true-to-life food texture.`

## Food-specific controls

- Name the **state**, not just the adjective: “freshly cut, still glistening at the cut face” is more useful than “juicy”.
- Use **localized cues**: “oil sheen only on the chili crisp” prevents the whole plate becoming glossy.
- Specify **one focus plane** and one supporting blur plane; too many “sharp details” fight each other.
- Describe **imperfections** positively: uneven browning, one broken yolk edge, a few loose crumbs, irregular herb placement.
- Keep the negative prompt short. Overloaded negatives can erase desired texture. Use: `illustration, CGI, plastic food, waxy texture, floating objects, duplicated utensils, unreadable text, oversaturated colors, harsh HDR, extreme bokeh`.

## Example prompt

`A photorealistic editorial food photograph of a thick-cut pork chop, bone-in, pan-seared with a deeply browned mahogany crust and a warm blush-pink center, resting on a shallow matte ivory ceramic plate. A small pool of glossy cider pan sauce gathers beneath the chop, with visible reduction streaks; charred apple wedges sit at the bone, and three sage leaves are placed irregularly. Show crisp rendered fat, fine muscle grain at the cut face, tiny black pepper flecks, and a few coarse salt crystals. The plate sits on dark walnut with a loosely folded oatmeal linen napkin at the rear right. Large soft window light from camera left, slightly warm, with a gentle specular edge on the sauce and dense but open contact shadows. Shot three-quarter overhead at 55mm, f/4, focus on the cut face and front crust, background falling softly out of focus. Natural asymmetry, restrained editorial color grade, realistic moisture, believable reflections, subtle imperfections, no extra garnish.`

## Iteration loop

Change one variable at a time: composition → doneness/texture → light → lens/focus → props. Save prompt, seed, steps, and output filename together so successful variations can be reproduced.
