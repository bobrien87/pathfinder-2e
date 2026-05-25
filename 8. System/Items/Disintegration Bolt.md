---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 1300}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The shaft of this bolt is scorched and blackened, and handling it coats your fingers with a fine black powder. When an activated *disintegration bolt* hits a target, it is subject to a [[Disintegrate]] spell requiring a DC 34 [[Fortitude]] save. As with the spell, a critical hit on the attack roll causes the target's saving throw outcome to be one degree worse.

**Craft Requirements** Supply one casting of *disintegrate*.

**Source:** `= this.source` (`= this.source-type`)
