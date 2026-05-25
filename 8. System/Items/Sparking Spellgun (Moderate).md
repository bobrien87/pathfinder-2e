---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Attack]]", "[[Consumable]]", "[[Fire]]", "[[Magical]]", "[[Spellgun]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Strike

A broad wooden tube with a handle, a *sparking spellgun* radiates warmth. You Activate the spellgun by aiming it at one creature and making your choice of a spell attack roll or a firearm attack roll against the target's AC. This spellgun has a range increment of 30 feet. The spellgun fires a small ball of sparks and fire, then crumbles to ash. The ball explodes in a flash when it hits, dealing 7d6 fire damage and 3d4 persistent,fire damage.
- **Critical Success** The target takes double damage, takes double persistent damage, is [[Blinded]] for 1 round, and is [[Dazzled]] while the persistent damage lasts.
- **Success** The target takes full damage, full persistent damage, and is dazzled while the persistent damage lasts.

**Source:** `= this.source` (`= this.source-type`)
