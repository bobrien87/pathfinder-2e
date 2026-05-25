---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 24000}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

With lenses set in a silver frame, spectacles of piercing sight grant you a +3 item bonus to visual Perception checks.

**Activate** `pf2:1` (concentrate)

**Frequency** once per hour

**Effect** You can see into and through solid matter for 1 minute. This vision can pierce through solid materials up to 20 feet away as if looking at something in normal light even if no illumination is available. You can see through up to 1 foot of stone, 1 inch of metal, or 3 feet of wood or dirt. A thin sheet of lead blocks this vision entirely.

**Source:** `= this.source` (`= this.source-type`)
