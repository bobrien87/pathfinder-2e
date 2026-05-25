---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 135}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These goggles feature highly reflective lenses. While wearing the goggles, you gain a +1 item bonus to visual Perception checks and to saving throws against visual effects.

**Activate** R (manipulate)

**Trigger** A creature within 60 feet targets you with a visual effect

**Effect** You turn your head to reflect aspects of the triggering effect back at its creator. The creature must attempt a DC 20 [[Fortitude]] save as it becomes disoriented by this reflection. On a failure, the creature is [[Sickened]] 1 ([[Sickened]] 2 on a critical failure). The creature is temporarily immune for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
