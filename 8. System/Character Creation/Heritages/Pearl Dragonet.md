---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dragonet|Dragonet]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have pearlescent scales and a round body, with short legs, small wings, and a long tail. The shape of your body lets you absorb a blow and roll away.

**[[Bounce Away]]**`pf2:r`

@Embed[Compendium.pf2e.actionspf2e.Item.OpiIzr7h1EKY8wKh inline]

**Source:** `= this.source` (`= this.source-type`)
