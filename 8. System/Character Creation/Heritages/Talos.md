---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Talos]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your physical features reflect the influence a zuhra or other metal elemental has had over your bloodline. Your skin likely has a metallic sheen, ranging from the dull luster of raw ore to the gleaming polish of a new blade, with the wear of age or hardship taking the form of tarnish, rust, or scouring. Your hair might resemble spun gold, coiled steel, copper wiring, or braided chains. You gain the talos trait, in addition to the traits from your ancestry. You gain resistance to electricity equal to half your level (minimum 1). You can cast the [[Detect Metal]] cantrip as an arcane innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

You can choose from talos feats, geniekin feats, and feats from your ancestry whenever you gain an ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
