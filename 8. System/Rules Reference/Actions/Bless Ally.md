---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Fortune]]", "[[Mythic]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Requirements** Your nimbus is active

**Target** a willing ally within the bright light of your nimbus

**Effect** Your radiance grants an ally some of your celestial grace. That ally can roll twice and use the higher result for the next Will save they attempt before the beginning of your next turn.

> [!danger] Effect: Bless Ally

**Source:** `= this.source` (`= this.source-type`)
