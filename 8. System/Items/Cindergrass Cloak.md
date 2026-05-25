---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 250}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hooded cloak woven of long, waxy grass is designed so it can close over your entire body. While wearing this cloak, you have resistance 5 to fire.

**Shed Cinders** `pf2:r` (manipulate)

**Frequency** once per hour

**Trigger** You would take fire damage

**Effect** With a flick of the cloak, you deflect and smother the flames. The cloak's resistance to fire increases to 15 against the triggering effect. Until the end of your next turn, your flat check to remove persistent fire damage is 10 instead of 15, which is reduced to 5 if another creature uses a particularly appropriate action to help. If you take at least 5 points of fire damage after applying the fire resistance, the cloak gains the [[Broken]] condition.

> [!danger] Effect: Shed Cinders

**Source:** `= this.source` (`= this.source-type`)
