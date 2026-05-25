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

You were an aspect of nature—the rain, the wind, a ray of light—until the wild essences gave you a soul. Due to your natural connection, the tradition of any spells or magical abilities you gain from a yaoguai heritage or ancestry feat is primal instead of its normal tradition (usually occult).

- **Humanoid Form** You remain attuned to the natural world. You gain a +1 circumstance bonus to Survival checks to [[Sense Direction]], and you don't take a penalty if you don't have a compass.
- **Yaoguai Form** The power of nature flows through you, ready to lash out. Choose [[Electric Arc]], [[Frostbite]], [[Ignition]], [[Needle Darts]], [[Timber]], [[Scatter Scree]], [[Slashing Gust]], or [[Spout]]. You can cast this spell as an innate primal cantrip at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
