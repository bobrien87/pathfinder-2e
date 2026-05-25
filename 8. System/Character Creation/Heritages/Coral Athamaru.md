---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Athamaru|Athamaru]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Coral covers patches of your body, which provides a natural layer of defense. Coral athamarus often choose Coral Symbiotes and other related ancestry feats. The coral plates are medium armor in the plate armor group that grant a +4 item bonus to AC, a Dex cap of +1, a check penalty of –2, a Speed penalty of –5 feet, a Strength value of +3, and have the aquadynamic and comfort traits. You can never wear other armor or remove the coral. You can etch armor runes onto the coral.

**Source:** `= this.source` (`= this.source-type`)
