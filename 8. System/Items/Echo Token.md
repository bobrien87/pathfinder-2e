---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Visitors to the Echo Repository always emerge with one of these silver coins, stamped with the visage of a faceless queen, somewhere on their person. An *echo token* carries a minute shard of the Echo Repository's mission to impart lost information.

**Activate—Flip Coin** `pf2:1` (manipulate)

**Effect** When flipped, the coin disintegrates into a glittery mist. You learn and memorize one random fact about a specific type of Lore (such as Architecture Lore, Elf Lore, Astral Plane Lore) that you didn't previously know, chosen by the GM. The next time you attempt a check to Recall Knowledge on this type of Lore within the next year, you gain a +1 status bonus on the check. You can benefit from only one *echo token* at a time in this way; if you Flip another *echo token*, the Lore skill changes. However, the memorized fact will remain perfectly in your memory forever unless magically altered or removed.

**Source:** `= this.source` (`= this.source-type`)
