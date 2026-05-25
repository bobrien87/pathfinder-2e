---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Gadget]]", "[[Sonic]]"]
price: "{'gp': 2500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

One of the stranger devices to come out of the University of Lepidstadt is a twisted glass contraption that hums with electricity. This vibration is harmless to most but is massively disruptive to the locomotion of incorporeal creatures. When activated, one incorporeal creature within 15 feet must attempt a DC 35 [[Fortitude]] save saving throw. Once used, the vibrations cause the glass to shatter.
- **Success** The target is unaffected.
- **Failure** The target is [[Immobilized]] for 1 round.
- **Critical Failure** The target is immobilized and [[Off Guard]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
