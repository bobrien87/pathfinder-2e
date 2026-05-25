---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]"]
price: "{'gp': 9000}"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *floating shield* is usually carved with wing motifs. This buckler (Hardness 6, HP 24, BT 12) can protect you on its own.

**Activate—Float** A (manipulate)

**Frequency** at will

**Effect** The shield magically releases itself and floats off your arm into the air next to you, granting you its bonus automatically, as if you had Raised the Shield.

Because you're not wielding the shield, you can't use reactions such as Shield Block with the shield, but you gain its benefits even when using both of your hands.

After 1 minute, the shield drops to the ground, ending its floating effect. While the shield is adjacent to you, you can Interact to grasp it, ending its floating effect early.

**Source:** `= this.source` (`= this.source-type`)
