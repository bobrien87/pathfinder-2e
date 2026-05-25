---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

*Skyfisher vapors* are only visible via their effect on a [[Toxic Cloud]] spell, or apparent lack thereof. These gases cause the conjured cloud to be as transparent as a skyfisher. The cloud is invisible, meaning it does not provide concealment, but it requires a successful [[Perception]] check against your spell DC to notice the cloud by faint distortions in the air. Your magical connection to the cloud means you always know where it is. This has no effect on its damage.

**Source:** `= this.source` (`= this.source-type`)
