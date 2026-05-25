---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Adjustment]]", "[[Alchemical]]"]
price: "{'gp': 10}"
usage: "applied-to-a-non-injection-melee-weapon-piercing-damage"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This reservoir and spring-loaded needle can be attached to a weapon to let it inject deadly poisons. Additionally, the reservoir can be filled with an injury poison. Immediately after a successful attack with the adjusted weapon, you can inject the target with the loaded poison by activating the reservoir with an Interact action. Refilling the reservoir with a new poison requires 3 Interact actions and uses both hands.

Adding an injection reservoir to a weapon throws off its balance, causing the multiple attack penalty with the weapon to be one greater than usual (usually –6 on a second attack and –11 on a third; or –5 and –10 with an agile weapon).

**Source:** `= this.source` (`= this.source-type`)
