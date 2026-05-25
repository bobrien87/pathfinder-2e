---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 245}"
bulk: "1"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A favorite of Hellknights, this steel shield is often emblazoned with the symbol of a Hellknight order and often notched with the number of times it has absorbed damage.

**Activate—Terrifying Block** `pf2:f` (concentrate, emotion, fear, mental)

**Frequency** once per 10 minutes

**Trigger** You Shield Block

**Effect** When a weapon strikes an imposing shield, the sigil glows with a chilling light. The creature that made the attack that triggered your Shield Block becomes [[Frightened]] 2. If the Shield Block reduced the incoming damage to 0, the creature instead becomes [[Frightened]] 3.

HardnessHPBT63618

**Source:** `= this.source` (`= this.source-type`)
