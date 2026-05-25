---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Duskwalker]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Thanks to an ancient bargain, your soul has been reborn as a duskwalker, a planar scion with a connection to psychopomps and the Boneyard. You gain the duskwalker trait. You also gain low-light vision, or you gain darkvision if your ancestry already has low-light vision. Neither your body nor your spirit can ever become undead. You can select from duskwalker feats and feats from your ancestry whenever you gain an ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
