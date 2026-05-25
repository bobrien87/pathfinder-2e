---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]", "[[Spellgun]]", "[[Water]]"]
price: "{'gp': 1250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Strike

Carved of seashell, a *torrent spellgun* is damp to the touch, and seaweed wraps around its grip. You Activate the spellgun by aiming it at one creature and making your choice of a spell attack roll or a firearm attack roll against the target's AC. This spellgun has a range increment of 30 feet. The spellgun blasts a powerful jet of water that deals 16d6 bludgeoning, then disintegrates into sand.
- **Critical Success** The target takes double damage and is knocked back 10 feet.
- **Success** The target takes full damage and is knocked back 5 feet.

**Source:** `= this.source` (`= this.source-type`)
