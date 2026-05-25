---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Surki|Surki]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your carapace is much denser than that of other surkis, offering you a suit of your very own armor. Your carapace is medium armor in the plate armor group that grants a +4 item bonus to AC, a Dex cap of +1, a check penalty of –2, a Speed penalty of –5 feet, a Strength value of +3, and has the comfort trait. You can never wear other armor or remove your carapace. You can etch armor runes onto your carapace.

- **Evolution** The magical circulatory system that runs between your nodes has become a reinforcing network that strengthens your carapace with magical energy. If you're struck by a critical hit that deals physical damage, you can use your reaction to attempt a DC 17 flat check. If successful, the attack becomes a normal hit.

- **Evolution** Your abdominal nodes can project a field around you that guards you against the type of magic you're most familiar with. You gain the [[Dampening Harmonics]] action.

**Source:** `= this.source` (`= this.source-type`)
