---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]"]
price: "{'gp': 150}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather armor has been treated with extract from oozes, which can be reactivated in the presence of a strong acid. A receptacle in the armor can hold an Acid Flask, which takes 3 Interact actions to install.

**Activate** `pf2:1` (manipulate)

**Requirements** An acid flask is installed in the armor

**Effect** The leather weeps slippery protoplasm, granting an item bonus to [[Escape]] and [[Squeeze]] checks equal to the acid flask's item bonus. The protoplasm also irritates the skin on prolonged contact, causing any creature that grapples or swallows you to take acid damage equal to the acid flask's splash damage. Ooze skin remains activated for a number of rounds equal to the level of the acid flask installed. The activation uses up the acid flask, and the armor can't be activated again until a new one is installed.

**Source:** `= this.source` (`= this.source-type`)
