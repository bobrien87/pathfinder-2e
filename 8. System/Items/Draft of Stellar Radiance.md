---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Light]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This potion's bottle glows softly with shimmering silver light. Upon drinking this potion, you're surrounded by a nimbus of blazing starlight that lasts for 1 minute. You emanate a field of bright light with a 20-foot radius (and dim light for another 20 feet, like a torch). You take a –20 penalty to Stealth checks. Any creature that targets you with an attack or an ability must succeed at a DC 17 [[Fortitude]] save or be [[Dazzled]] for 1 round. A creature who succeeds at this save is immune to the effect for 24 hours.

> [!danger] Effect: Draft of Stellar Radiance

**Source:** `= this.source` (`= this.source-type`)
