---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

The mixture of reagents, liquid djezet, and solid metal shrapnel inside this grenade explodes on contact with air. A *spellsap grenade* deals 4d4 slashing damage and 4 slashing splash damage. You gain a +3 item bonus to attack rolls. On a hit against a prepared or spontaneous spellcaster, the target must succeed at a DC 38 [[Will]] save saving throw or lose one prepared spell or one spontaneous spell slot. The spell is randomly selected from among the caster's highest three spell ranks (and then from among the spells prepared in that rank, for a prepared spellcaster).

**Source:** `= this.source` (`= this.source-type`)
