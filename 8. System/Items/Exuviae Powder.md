---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Earth]]"]
price: "{'gp': 750}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

*Exuviae powder* comes from cast-off shells of cicada-like insects native to the Plane of Earth, crushed to dust. You sprinkle this powder over your body, leaving an iridescent layer reminiscent of insect chitin. After you do so, for 8 hours, you double the time you can hold your breath. During this time, you also have access to the shed chitin activation.

**Activate—Shed Chitin** R (concentrate)

**Trigger** You would be petrified

**Effect** The powder petrifies like a shell around you instead, and its other effects end. The powder causes you to become [[Quickened]] for 1 minute as well as [[Doomed]] 1 and [[Restrained]] (`act escape show-dc=all dc=25`). You can use the extra action each round only for Escape and Stride actions.

**Source:** `= this.source` (`= this.source-type`)
