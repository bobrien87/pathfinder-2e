---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Missive]]"]
price: "{'gp': 13}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

An explosive missive is slightly warm to the touch, regardless of the surrounding environment. When composed and then activated, the missive explodes. The tenor of what you write or the theme of your illustration determines the damage type and adds the corresponding trait to the missive: @Damage[4d6[acid]|options:area-damage]{acid} for a caustic inscription, @Damage[4d6[cold]|options:area-damage]{cold} for an aloof one, @Damage[4d6[electricity]|options:area-damage]{electricity} for an energetic one, @Damage[4d6[fire]|options:area-damage]{fire} for an angry one, or @Damage[4d6[sonic]|options:area-damage]{sonic} for an overly emphatic one. The missive deals 4d6 damage to each creature in a @Template[burst|distance:5] from a corner of the missive's space (DC 18 [[Reflex]] save). A creature who rolls a critical failure also takes 1d4 persistent damage of the same type. The missive burns to ash while releasing its magic.

1d4 persistent,acid 1d4 persistent,cold 1d4 persistent,electricity 1d4 persistent,fire 1d4 persistent,sonic

**Source:** `= this.source` (`= this.source-type`)
