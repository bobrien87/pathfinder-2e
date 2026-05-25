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

You were once a powerful celestial before an escape or great punishment left you trapped in a mortal shell, with only vague memories and limited power. Due to your residual divine power, the tradition of any spells or magical abilities you gain from a yaoguai heritage or ancestry feat is divine instead of its normal tradition (usually occult).

- **Humanoid Form** Fragments of divine memory still litter your mind. You gain a +1 circumstance bonus to Religion checks.
- **Yaoguai Form** Celestial power flows through you. Choose one cantrip from the divine spell list. You can cast this spell as an innate divine cantrip at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
