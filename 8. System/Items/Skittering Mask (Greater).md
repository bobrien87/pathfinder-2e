---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "wornmask"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *skittering mask* is a hand-carved, wooden, full-head mask that sports several holes along each side of the face. The first time each day that you begin your turn unconscious and within 25 feet of an enemy, metallic insect legs emerge from the holes in the mask and Step 15 feet away from the nearest enemy, dragging your body along with the mask. For 1 minute, each time you begin your turn unconscious and within 25 feet of an enemy, the mask Steps 15 feet away from the nearest enemy again. An ally can signal the mask with a single action, which has the auditory and concentrate traits. If the mask hears the signal, it attempts to move you towards that ally when it Steps away from the nearest enemy.

If more than one enemy is equidistant, the mask Steps away from one of them at random. The mask possesses no special senses and does not react to [[Hidden]] or [[Undetected]] enemies, nor can it distinguish that a creature not acting openly hostile is an enemy.

**Source:** `= this.source` (`= this.source-type`)
