---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 500}"
usage: "affixed-to-a-shield"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:r` (concentrate)

**Trigger** You are targeted by a spell of 5th rank or lower

**Requirements** You're a master in Athletics, and you have the affixed shield raised.

This mirrored metal fragment is bolted or welded to the face of the affixed shield. When you Activate it, you attempt to reflect the triggering spell back at its caster with [[Spell Riposte]], using your [[Athletics]] check modifier for the counteract check. The talisman's counteract rank is 7th.

**Source:** `= this.source` (`= this.source-type`)
