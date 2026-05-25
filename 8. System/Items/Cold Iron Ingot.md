---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Precious]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Weapons made from cold iron are deadly to demons and fey alike. Cold iron looks like normal iron but is mined from particularly pure sources and shaped with little or no heat. This process is extremely difficult, especially for high-grade cold iron items.

Cold Iron ItemsCold Iron ItemsHardnessHPBT**Thin Items**Low-grade52010Standard-grade72814High-grade104020**Items**Low-grade93618Standard-grade114422High-grade145628**Structure**Low-grade187236Standard-grade228844High-grade2811256

**Source:** `= this.source` (`= this.source-type`)
