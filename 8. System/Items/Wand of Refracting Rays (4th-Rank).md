---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Light]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 1400, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand is short and wide with a hexagonal, crystal shaft and a leather-wrapped handle. The wand refracts direct bright light into a rainbow.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 4th-rank [[Chromatic Ray]]. After you cast the spell, if you hit the target, the light refracts to another creature within 30 feet of the first target. Roll your spell attack roll and to determine the ray's color separately for each target. The ray continues to refract each time it hits. The refraction ceases if you miss any target, and you can end the refraction at any point. You can't target the same creature more than once, and you must have line of effect to all targets.

**Craft Requirements** Supply a casting of *chromatic ray* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
