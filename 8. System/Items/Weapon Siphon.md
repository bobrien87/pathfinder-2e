---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Adjustment]]", "[[Alchemical]]"]
price: "{'gp': 10}"
usage: "attached-to-melee-weapon"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This set of tubing snakes down the striking surface of a weapon to deliver alchemical explosives. A single lesser alchemical bomb can be fitted to the weapon siphon as an Interact action. The bomb must be one that deals energy damage, such as an Acid Flask, Alchemist's Fire, Blasting Stone, Bottled Lightning, or Frost Vial. The next three attacks made with the weapon deal 1d4 damage of the bomb's damage type in addition to the weapon's normal damage. If the second and third attacks aren't all made within 1 minute of the first attack, the bomb's energy is wasted. These attacks never deal splash damage or other special effects of the bomb and aren't modified by any abilities that add to or modify a bomb's effect.

Adding a weapon siphon to a weapon throws off its balance, causing the multiple attack penalty with the weapon to be one greater than usual (usually –6 on a second attack and –11 on a third; or –5 and –10 with an agile weapon).

> [!danger] Effect: Weapon Siphon

> [!danger] Effect: Weapon Siphon Bomb Fitted

**Source:** `= this.source` (`= this.source-type`)
