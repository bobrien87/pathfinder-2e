---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Yaoguai|Yaoguai]]"
traits: ["[[Yaoguai]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were a plant or fungi until the rain gifted you a mind. You gain your choice of the plant or fungus trait.

- **Humanoid Form** With fresh vegetation, you can better aid those in need. You gain a +1 circumstance bonus to Medicine checks to [[Administer First Aid]].
- **Yaoguai Form** When anyone uses the Medicine skill to [[Treat your Wounds]], add your level to the Hit Points you regain from that treatment. Additionally, the creature attempting the check gains a +1 circumstance bonus if you have the plant trait and are in bright light, or the fungus trait and are in darkness.

**Source:** `= this.source` (`= this.source-type`)
