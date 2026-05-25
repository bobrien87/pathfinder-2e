---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Disarm]]", "[[Finesse]]", "[[Free hand]]", "[[Monk]]", "[[Parry]]"]
price: "{'sp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Four curved blades attached to a sturdy handlebar give the wielder of this close-combat weapon the illusion of having claws that extend from their fist. Adherents of [[Bastet]] favor the tekko-kagi for catching their foes off guard.

**Source:** `= this.source` (`= this.source-type`)
