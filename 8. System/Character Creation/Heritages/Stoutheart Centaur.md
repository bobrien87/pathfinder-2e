---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Centaur|Centaur]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're a hardy centaur, firm of stance and strong of heart. You gain 10 Hit Points from your ancestry instead of 8 and gain a +1 circumstance bonus to Acrobatics checks to [[Balance]] and to your Reflex DC to avoid being tripped.

**Source:** `= this.source` (`= this.source-type`)
