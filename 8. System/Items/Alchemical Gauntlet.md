---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Agile]]", "[[Alchemical]]", "[[Free hand]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An alchemical gauntlet emits small alchemical detonations when it makes contact with a foe. As an Interact action, you can place a bomb into a metal bracket near the wrist of the gauntlet. The bomb must be one that deals energy damage, such as an acid flask, alchemist's fire, blasting stone, bottled lightning, or frost vial. The next three attacks made with the gauntlet deal 1d4 damage of the bomb's damage type in addition to the gauntlet's normal damage. If the second and third attacks aren't all made within 1 minute of the first attack, the bomb's energy is wasted. These attacks never deal splash damage or other special effects of the bomb and aren't modified by any abilities that add to or modify a bomb's effect.

**Source:** `= this.source` (`= this.source-type`)
