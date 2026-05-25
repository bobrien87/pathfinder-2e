---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Fortune]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 750}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:r` (concentrate)

**Trigger** You fail to save against a death or void effect.

An acolyte accidentally left fulu paper outdoors overnight during a divine ceremony to Tsukiyo conducted only during a supermoon, creating the first reflected moonlight fulu. When you Activate this fulu, you reroll your saving throw against the triggering effect and take the better result. If this new roll is a critical success, the effect is reflected on its creator, who's treated as the effect's target, with any void damage converted to vitality damage. A reflected effect or spell affects only the original creator, even if it was an area spell or one that affects more than one creature.

**Source:** `= this.source` (`= this.source-type`)
