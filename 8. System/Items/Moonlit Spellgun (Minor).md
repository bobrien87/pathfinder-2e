---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Consumable]]", "[[Fire]]", "[[Light]]", "[[Magical]]", "[[Spellgun]]"]
price: "{'gp': 7}"
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

Elegant silver filigree contains the body of this ephemeral item, which is made of solid light. Its shape resembles a pistol, and it's often carried by hunters of werecreatures and vampires. You Activate the spellgun by aiming it at one creature and making your choice of a spell attack roll or a firearm attack roll against the target's AC. This spellgun has a range increment of 30 feet. The spellgun emits a silvery ray of pure moonlight that deals fire damage depending on its type. The spellgun's damage is treated as silver for the purposes of weaknesses, resistances, and the like.
- **Critical Success** The target takes double damage and is [[Dazzled]] until the start of your next turn. If it has a weakness to silver or a resistance that can be bypassed by silver, it's also [[Enfeebled]] 1 for 1 minute.
- **Success** The target takes full damage and is dazzled until the start of your next turn.

The damage is @Damage[1d8[fire]|options:damage:material:silver]{1d8 fire damage} at night, or @Damage[1d6[fire]|options:damage:material:silver]{1d6 fire damage} at other times.

**Source:** `= this.source` (`= this.source-type`)
