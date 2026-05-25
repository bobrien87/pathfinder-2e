---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Illusion]]", "[[Magical]]", "[[Visual]]"]
price: "{'gp': 80}"
usage: "held-in-one-or-two-hands"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These weapons consist mostly of illusions, except in the spots where the weapon would be held. A sword, for example, would consist only of a physical handle with the permanent illusion of a blade. *Weapons of false wounds* come in all shapes and sizes to help accurately reenact both historic and theatrical combat without risk of injury. The most amazing property of these items is the fact the illusions become partially physical when interacting with other *weapons of false wounds*, allowing blades to clash and parry as they would in actual combat. As a *weapon of false wounds* is designed specifically to interact with other illusions, paying attention to subtle changes in the weapon's appearance can help alert the wielder to nearby illusions. While using this item, you gain a +1 item bonus to Perception checks to disbelieve an illusion.

**Source:** `= this.source` (`= this.source-type`)
