---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Oni]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

One of your parents was an oni or a hungerseed. You possess a pair of horns, ranging in size from conical nubs to lengthy protrusions. You might have other signs of your parentage, such as colorful skin, fangs and claws, or a third eye in your forehead. You gain the oni trait. You gain a horns unarmed attack that deals 1d6 piercing damage and is in the brawling group. You can select from hungerseed feats and feats from your other parent's ancestry whenever you gain an ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
