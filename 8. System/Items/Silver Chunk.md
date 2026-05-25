---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Precious]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Silver weapons are a bane to creatures ranging from devils to werewolves. Silver items are less durable than steel items, and low-grade silver items are usually merely silver-plated.

Silver ItemsSilver ItemsHardnessHPBT**Thin Items**Low-grade3126Standard-grade52010High-grade83216**Items**Low-grade52010Standard-grade72814High-grade104020**Structure**Low-grade104020Standard-grade145628High-grade208040

**Source:** `= this.source` (`= this.source-type`)
