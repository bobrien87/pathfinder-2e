---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This dark *+1 resilient shadow studded leather armor* is frequently used to bypass enemy positions or quickly travel around battlefield obstacles as it allows you to partially transit through the Netherworld.

**Activate—Shroud Stride** `pf2:1` (concentrate, shadow)

**Frequency** once per day

**Effect** You slip into the Netherworld for a moment, allowing you to Stride twice your speed. This movement doesn't trigger reactions and ignores difficult and hazardous terrain. Shadows lingers on the armor, causing you to become [[Concealed]] for 1 round afterward.

**Source:** `= this.source` (`= this.source-type`)
